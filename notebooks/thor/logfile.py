# IPython log file


get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
from ms_utils.util.imports.ipython_utils import *
import glob
import urllib
import re

from ms_utils.util.imports.scraping_imports import *
import ms_utils as ms
import ms_utils.daf.get
from ms_utils.slurp.yboss import Yboss
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker
import ms_utils.daf.gr
import ms_utils.util.log

sda = ScrapesDataAccess()
yb = Yboss(default_save_folder=sda.data_folders['yboss_df_slurps'])

print "root folder: %s" % sda.facc('')
print "yboss_df_slurps folder: %s" % sda.data_folders['yboss_df_slurps']
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
from ms_utils.util.imports.ipython_utils import *
import requests
from bs4 import BeautifulSoup
import BeautifulSoup as bs3_BeautifulSoup
import ms_utils.parse.util
import time
from selenium import webdriver
driver = webdriver.PhantomJS() # or add to your PATH
driver.desired_capabilities
w = webdriver.Firefox()
w.desired_capabilities
w.close()
import requests
from bs4 import BeautifulSoup
import BeautifulSoup as bs3_BeautifulSoup
import ms_utils.parse.util
import time
from selenium import webdriver
driver = webdriver.PhantomJS() # or add to your PATH
def filepath_for_url(url):
    return os.path.join('facebook_slurps', sda.filename_from_url(url))

def get_html(url, pause_seconds_before_slurp=1):
    file_path = filepath_for_url(url)
    if os.path.exists(file_path):
        return sda.facc.load(html, file_path)
    else:
        time.sleep(pause_seconds_before_slurp)
        html = get_html_from_url(url)
        sda.facc.save(html, file_path)
        return html

def get_html_from_url(url):
    driver.get(url)
    return driver.page_source

def get_num_of_likes(b):
    try:
        return b.find('span', attrs={'class':re.compile('stats')}).text
    except:
        try:
            return re.compile('[\d,\.]+').match(b.find('div', "fsm fwn fcg").find('div', "fsm fwn fcg").text).group(0)
        except:
            return None
d = pd.read_pickle(sda.facc('pickles/stripped_url_tail_counts.df'))
d.head()
d = pd.read_pickle(sda.facc('pickles/url_tail_counts.df'))
print "number of rows: %d" % len(d)
d['likes'] = None
d.head()
lidx = np.array(map(bool, [x for x in map(re.compile('/pages/').match, d['url_tail'])]))
d = pd.concat([d[lidx],d[~lidx]])
print d.head(2)
print d.tail(2)
sda = ScrapesDataAccess()
sda.data_folders['facebook_slurps']
n = len(d)
pause_seconds_before_slurp = 3
root_url = 'https://www.facebook.com'
for i in range(0, n):
    
    try:
        url = root_url + d.iloc[i]['url_tail']
        logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i,n,url)))
        html = get_html(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
        b = BeautifulSoup(html)
    except Exception as e:
        logging.exception("first part of processing: %s" % url)
        
    try:
        d['likes'].iloc[i] = get_num_of_likes(b)
    except Exception as e:
        logging.exception("second part of processing: %s" % url)
        continue
    
#     if mod(i+1,10) == 0:
#         sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
d.head(10)
n = len(d)
pause_seconds_before_slurp = 3
root_url = 'https://www.facebook.com'
for i in range(0, 10):
    
    try:
        url = root_url + d.iloc[i]['url_tail']
        logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i,n,url)))
        html = get_html(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
        b = BeautifulSoup(html)
    except Exception as e:
        logging.exception("first part of processing: %s" % url)
        
    try:
        d['likes'].iloc[i] = get_num_of_likes(b)
    except Exception as e:
        logging.exception("second part of processing: %s" % url)
        continue
    
#     if mod(i+1,10) == 0:
#         sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
def filepath_for_url(url):
    return os.path.join('facebook_slurps', sda.filename_from_url(url))

def get_html(url, pause_seconds_before_slurp=1):
    file_path = filepath_for_url(url)
    if os.path.exists(file_path):
        return sda.facc.load(file_path)
    else:
        time.sleep(pause_seconds_before_slurp)
        html = get_html_from_url(url)
        sda.facc.save(html, file_path)
        return html

def get_html_from_url(url):
    driver.get(url)
    return driver.page_source

def get_num_of_likes(b):
    try:
        return b.find('span', attrs={'class':re.compile('stats')}).text
    except:
        try:
            return re.compile('[\d,\.]+').match(b.find('div', "fsm fwn fcg").find('div', "fsm fwn fcg").text).group(0)
        except:
            return None
def filepath_for_url(url):
    return os.path.join('facebook_slurps', sda.filename_from_url(url))

def get_html(url, pause_seconds_before_slurp=1):
    file_path = filepath_for_url(url)
    if os.path.exists(file_path):
        print 'yep!"
        return sda.facc.load(file_path)
    else:
        time.sleep(pause_seconds_before_slurp)
        html = get_html_from_url(url)
        sda.facc.save(html, file_path)
        return html

def get_html_from_url(url):
    driver.get(url)
    return driver.page_source

def get_num_of_likes(b):
    try:
        return b.find('span', attrs={'class':re.compile('stats')}).text
    except:
        try:
            return re.compile('[\d,\.]+').match(b.find('div', "fsm fwn fcg").find('div', "fsm fwn fcg").text).group(0)
        except:
            return None
n = len(d)
pause_seconds_before_slurp = 3
root_url = 'https://www.facebook.com'
for i in range(0, 10):
    
    try:
        url = root_url + d.iloc[i]['url_tail']
        logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i,n,url)))
        html = get_html(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
        b = BeautifulSoup(html)
    except Exception as e:
        logging.exception("first part of processing: %s" % url)
        
    try:
        d['likes'].iloc[i] = get_num_of_likes(b)
    except Exception as e:
        logging.exception("second part of processing: %s" % url)
        continue
    
#     if mod(i+1,10) == 0:
#         sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
url
print url
file_path = filepath_for_url(url)
print file_path
def filepath_for_url(url):
    return os.path.join('facebook_slurps', sda.filename_from_url(url))

def get_html(url, pause_seconds_before_slurp=1):
    file_path = filepath_for_url(url)
    if os.path.exists(sda.facc(file_path)):
        print 'yep!"
        return sda.facc.load(file_path)
    else:
        time.sleep(pause_seconds_before_slurp)
        html = get_html_from_url(url)
        sda.facc.save(html, file_path)
        return html

def get_html_from_url(url):
    driver.get(url)
    return driver.page_source

def get_num_of_likes(b):
    try:
        return b.find('span', attrs={'class':re.compile('stats')}).text
    except:
        try:
            return re.compile('[\d,\.]+').match(b.find('div', "fsm fwn fcg").find('div', "fsm fwn fcg").text).group(0)
        except:
            return None
print url
file_path = filepath_for_url(url)
print file_path
os.path.exists(sda.facc(file_path))
def filepath_for_url(url):
    return os.path.join('facebook_slurps', sda.filename_from_url(url))

def get_html(url, pause_seconds_before_slurp=1):
    file_path = filepath_for_url(url)
    if os.path.exists(sda.facc(file_path)):
        return sda.facc.load(file_path)
    else:
        time.sleep(pause_seconds_before_slurp)
        html = get_html_from_url(url)
        sda.facc.save(html, file_path)
        return html

def get_html_from_url(url):
    driver.get(url)
    return driver.page_source

def get_num_of_likes(b):
    try:
        return b.find('span', attrs={'class':re.compile('stats')}).text
    except:
        try:
            return re.compile('[\d,\.]+').match(b.find('div', "fsm fwn fcg").find('div', "fsm fwn fcg").text).group(0)
        except:
            return None
n = len(d)
pause_seconds_before_slurp = 3
root_url = 'https://www.facebook.com'
for i in range(0, 10):
    
    try:
        url = root_url + d.iloc[i]['url_tail']
        logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i,n,url)))
        html = get_html(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
        b = BeautifulSoup(html)
    except Exception as e:
        logging.exception("first part of processing: %s" % url)
        
    try:
        d['likes'].iloc[i] = get_num_of_likes(b)
    except Exception as e:
        logging.exception("second part of processing: %s" % url)
        continue
    
#     if mod(i+1,10) == 0:
#         sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
n = len(d)
pause_seconds_before_slurp = 3
root_url = 'https://www.facebook.com'
for i in range(10, n):
    
    try:
        url = root_url + d.iloc[i]['url_tail']
        logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i,n,url)))
        html = get_html(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
        b = BeautifulSoup(html)
    except Exception as e:
        logging.exception("first part of processing: %s" % url)
        
    try:
        d['likes'].iloc[i] = get_num_of_likes(b)
    except Exception as e:
        logging.exception("second part of processing: %s" % url)
        continue
    
#     if mod(i+1,10) == 0:
#         sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
d.head()
filter(None, d['likes'])
sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
dd = d[d['likes'].notnull()]
print len(dd)
dd.tail()
dd.head()
sda.facc.save(d, 'pickles/url_tail_counts_and_likes.df')
d.head(20)
