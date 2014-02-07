__author__ = 'thor'

import os
from datetime import datetime
import urllib
import logging

import global_spa.slurp.search_term_maker as search_term_maker
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess

from ms_utils.slurp.yboss import Yboss

from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker

sda = ScrapesDataAccess()
yb = Yboss(default_save_folder=sda.data_folders['yboss_df_slurps'])

print "root folder: %s" % sda.facc('')
print "yboss_df_slurps folder: %s" % sda.data_folders['yboss_df_slurps']

save_folder = sda.data_folders['yboss_df_slurps']


def query_to_file(query, service):
    return urllib.urlencode({service: query}) + '.df'


def query_to_filepath(query, service, save_folder):
    return os.path.join(save_folder, query_to_file(query, service))


def hms_message(msg=''):
    t = datetime.now().time()
    return "%02.0f:%02.0f:%02.0f - %s" % (t.hour, t.minute, t.second, msg)

n_pages = 10
logging.basicConfig(filename=os.path.join(sda.data_folders['log'],'yboss.log'),level=logging.DEBUG)

save_folder = sda.data_folders['yboss_df_slurps']
service = 'limitedweb'

query_list = search_term_maker.mk_who_what_how_where()
len(query_list)

n = len(query_list)
yb = Yboss()

##########################################
#### limitedweb
service = 'limitedweb'
logging.basicConfig(filename=os.path.join(sda.data_folders['log'],'yboss.log'),level=logging.DEBUG)

query_list = search_term_maker.mk_who_what_how_where()
print "service: %s" % service
print "number of queries: %d" % len(query_list)

for i, query in enumerate(query_list):
    logging.debug(hms_message('%d/%d: %s' % (i, len(query_list), query)))
    df = yb.slurp_results_df_multiple_pages(query=query, service=service, n_pages=n_pages)
    df.to_pickle(query_to_filepath(query, service, save_folder))

##########################################
#### blogs
service = 'blogs'
logging.basicConfig(filename=os.path.join(sda.data_folders['log'],'yboss.log'),level=logging.DEBUG)

query_list = search_term_maker.mk_who_what_how()
print "service: %s" % service
print "number of queries: %d" % len(query_list)

for i, query in enumerate(query_list):
    logging.debug(hms_message('%d/%d: %s' % (i, len(query_list), query)))
    df = yb.slurp_results_df_multiple_pages(query=query, service=service, n_pages=n_pages)
    df.to_pickle(query_to_filepath(query, service, save_folder))