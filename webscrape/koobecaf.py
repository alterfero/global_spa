__author__ = 'thor'

import os
import re
import glob
import pandas as pd
import urllib
import logging
import requests
from bs4 import BeautifulSoup
import BeautifulSoup as bs3_BeautifulSoup

import ms_utils as ms
import ms_utils.pfile.accessor
# import ms_utils.util.pobj
from ms_utils.slurp.yboss import Yboss
import time

from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess


class Koobecaf(object):
    def __init__(self, **kwargs):
        self.sda = ScrapesDataAccess(**kwargs)
        self.yboss = Yboss(default_save_folder=self.sda.data_folders['yboss_df_slurps'])
        if not hasattr(self, 'webdriver'):
            from selenium import webdriver
            self.webdriver = webdriver.PhantomJS()
        if not hasattr(self, 'logging'):
            self.logging = logging.basicConfig(
                                filename=os.path.join(os.environ['DATA_LOG_FOLDER'], 'main.log'),
                                filemode='w',
                                level=logging.DEBUG)

    def filepath_for_url(self, url):
        return os.path.join('facebook_slurps', self.sda.filename_from_url(url))

    def get_and_save_html_if_not_saved_already(self, url, pause_seconds_before_slurp=1):
        file_sub_path = self.filepath_for_url(url)
        if self.facc.exists(file_sub_path):
            return self.facc.load(file_sub_path)
        else:
            time.sleep(pause_seconds_before_slurp)
            html = self.get_html_from_url(url)
            self.facc.save(html, file_sub_path)
            return html

    def get_html_from_url(self, url):
        self.webdriver.get(url)
        return self.webdriver.page_source

    def aggregate_saved_dfs(self, yboss_files=None):
        yboss_files = yboss_files or glob.glob(self.sda.glob_filters['yboss_facebook'])
        df = reduce(lambda x, y: pd.concat([x, self.filename_to_df_with_query(y)]), yboss_files, pd.DataFrame())
        df = self.yboss.process_df(df)
        return df.sort(columns=['query', 'position'], ascending=True).reset_index(drop=True)

    def filename_to_url_tail(self, filename):
        return Koobecaf.url_to_url_tail(self.sda.url_from_filename(filename))

    def slurp_non_existing(self, url_list, pause_seconds_before_slurp=3):
        if hasattr(url_list, '__getitem__'):
            n = len(url_list)
        else:
            n = -1
        i = -1
        for url in url_list:
            i += 1
            try:
                self.logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i, n, url)))
                self.get_html_from_url(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
            except Exception as e:
                self.logging.exception("first part of processing: %s" % url)

    @staticmethod
    def process_df(df):
        cols = df.columns
        if 'likes' in cols and (isinstance(df['likes'].iloc[0], basestring)):
            df['likes'] = map(lambda x: x.replace('k', '000'), df['likes'])
            df['likes'] = map(lambda x: re.compile('\D').sub('', x), df['likes'])
            df['likes'] = map(int, df['likes'])
        return df

    @staticmethod
    def url_tail_to_url(url_tail):
        return 'https://www.facebook.com' + url_tail

    @staticmethod
    def url_to_url_tail(filename):
        t = filename.split('facebook.com')
        try:
            return t[1]
        except Exception:
            return filename

    @staticmethod
    def filename_to_query(filename):
        return urllib.unquote_plus(re.findall('(?<=limitedweb=).*(?=\+site%3Afacebook\.com\.df)', filename)[0])

    @classmethod
    def filename_to_df_with_query(cls, filename):
        df = pd.read_pickle(filename)
        df['query'] = Koobecaf.filename_to_query(filename)
        df['num_of_slurped_results'] = len(df)
        return df

    @staticmethod
    def get_num_of_likes(b):
        try:
            return re.compile('[\d,\.]+').match(b.find('div', "fsm fwn fcg").find('div', "fsm fwn fcg").text).group(0)
        except Exception:
            try:
                return b.find('span', attrs={'class':re.compile('stats')}).text
            except Exception:
                return None



