__author__ = 'thor'

import os
import pstr.to
import requests
import re
import urlparse
import urllib
from datetime import datetime
import pfile.accessor
import time
from slurp.resource_access import get_random_user_agent



##########
# SETTINGS
root_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
save_folder = os.path.join(root_folder, 'slurps')
# save_folder = os.path.join(data_root_folder, 'slurps_test2')

log_file = os.path.join(root_folder, 'progress_log.log')
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 (KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2'

html_re = re.compile('\.html$')

################################################
# UTILS


def mk_url_list_from_queries(query_list, get_url_fun, result_page_number=0):
    return [get_url_fun(x, y) for x in query_list for y in range(result_page_number)]


def peep_in_list(a):
    print a[0]
    print a[1]
    print a[-2]
    print a[-1]


def cartesian_op(op, A, B):
    return [op(a, b) for a in A for b in B]


def log_to_file(filename, msg):
    with open(filename, "a") as myfile:
        myfile.write(hms_message() + msg + "\n")

def url_encode(query):
    # look at urlparse for cleaner ways to do this
    return urllib.urlencode({'':query})[1:]

def hms_message(msg=''):
    t = datetime.now().time()
    return "%02.0f:%02.0f:%02.0f - %s" % (t.hour, t.minute, t.second, msg)

def save_text_to_file(s, filepath):
    pstr.to.file(s, filepath)
#     text_file = open(filepath, "w")
#     text_file.write(s.encode('utf-8'))
#     text_file.close()

def filename_from_url_no_extension(url):
    return url.replace('/','§').replace(':','{')

def filename_from_url(url):
    return url.replace('/','§').replace(':','{') + '.html'

def url_from_filename(filename):
    return html_re.sub('', filename.replace('§','/').replace('{',':'))



# def get_dogpile_html_from_query(query):
#     dogpile_url_prefix = 'http://www.dogpile.com/search/web'
#     response = requests.get(dogpile_url_prefix, params={'q': query})
#     if response:
#         return response.text
#     else:
#         return None

# def acquire_query_result_from_dogpile(query, save_folder=os.path.join(os.environ['MS_DATA'], 'misc')):
#     html = get_dogpile_html_from_query(query)
#     if html:
#         file_name = url_encode_str(query) + '.html'
#         file_path = os.path.join(save_folder, file_name)
#         save_html(html, file_path)
#     else:
#         raise ValueError("There was a problem in acquiring %s" % query)

################################################
# SPECIFIC METHODS

dogpile_base_url = 'http://www.dogpile.com'
dogpile_search_url = '/search/web?'

google_base_url = 'http://www.google.com'
google_search_url = '/search?'
google_default_params = {
                        'num':'100', # number of results - maximum 100
                        'start': '0' # number of results to start with
                        }
gshop_default_params = dict(google_default_params, **{
                        'tbm':'shop', # the thing that makes it look on google shopping
                        'tbs':'p_ord:rv' # type of view - could be vw:g,p_ord%3Arv for gridded view
                        } )
gblogs_default_params = dict(google_default_params, **{
                        'tbm':'blg' # the thing that makes it look on google blogs
                        })
gnews_default_params = dict(google_default_params, **{
                        'tbm':'nws' # the thing that makes it look on google news
                        })

def qsi_from_result_page_number(page_number):
    return page_number*10 + 1

def get_dogpile_request_url(query, result_page_number=0):
    '''
    returns a url
    '''
    first_item_number = qsi_from_result_page_number(result_page_number)
    return urlparse.urljoin(base=dogpile_base_url,
                            url=dogpile_search_url
                            + urllib.urlencode(query={'q': query, 'qsi': first_item_number}))

def get_gsearch_request_url(query, result_page_number=0, number_of_results_per_page=100):
    '''
    returns a url to get a google shopping result page
    '''
    start_result_number = "%d" % (result_page_number*number_of_results_per_page)
    get_params = dict(google_default_params,
                      **{'start':start_result_number,
                         'num':number_of_results_per_page,
                         'q':query})
    return urlparse.urljoin(base=google_base_url,
                            url=google_search_url
                            + urllib.urlencode(query=get_params))

def get_gshop_request_url(query, result_page_number=0, number_of_results_per_page=100):
    '''
    returns a url to get a google shopping result page
    '''
    start_result_number = "%d" % (result_page_number*number_of_results_per_page )
    get_params = dict(gshop_default_params,
                      **{'start':start_result_number,
                         'num':number_of_results_per_page,
                         'q':query})
    return urlparse.urljoin(base=google_base_url,
                            url=google_search_url
                            + urllib.urlencode(query=get_params))

def get_gnews_request_url(query, result_page_number=0, number_of_results_per_page=100):
    '''
    returns a url to get a google shopping result page
    '''
    start_result_number = "%d" % (result_page_number*number_of_results_per_page)
    get_params = dict(gnews_default_params,
                      **{'start':start_result_number,
                         'num':number_of_results_per_page,
                         'q':query})
    return urlparse.urljoin(base=google_base_url,
                            url=google_search_url
                            + urllib.urlencode(query=get_params))

def get_gblogs_request_url(query, result_page_number=0, number_of_results_per_page=100):
    '''
    returns a url to get a google shopping result page
    '''
    start_result_number = "%d" % (result_page_number*number_of_results_per_page)
    get_params = dict(gblogs_default_params,
                      **{'start':start_result_number,
                         'num':number_of_results_per_page,
                         'q':query})
    return urlparse.urljoin(base=google_base_url,
                            url=google_search_url
                            + urllib.urlencode(query=get_params))


################################################
# GENERAL METHODS

# def get_url_from_seed(seed):
#     return get_dogpile_request_url(seed)

# def get_html_from_seed(seed):
#     url = get_url_from_seed(seed)
#     return get_html_of_url(url)


headers = { \
        "User-Agent": "Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate",
        "Connection": "close",
        "DNT": "1"
    }

ANONYMIZER_AUTH = requests.auth.HTTPProxyAuth('trial-otosense', 'ahR5shij')
ANONYMIZER_PROXIES = {'http': 'exploder.ion-access.com:80', 'https': 'exploder.ion-access.com:80'}

def url_slurper(url, timeout=7.0):
    headers['User-Agent'] = get_random_user_agent()
    response = requests.get(url, headers=headers, verify=False,
                 timeout=timeout, proxies=ANONYMIZER_PROXIES, auth=ANONYMIZER_AUTH)
    if response and response.ok:
        return response.text
    else:
        return None

def url_content_slurper(url, timeout=7.0):
    headers['User-Agent'] = get_random_user_agent()
    response = requests.get(url, headers=headers, verify=False,
                 timeout=timeout, proxies=ANONYMIZER_PROXIES, auth=ANONYMIZER_AUTH)
    if response and response.ok:
        return response.content
    else:
        return None

def url_response_slurper(url, timeout=7.0):
    headers['User-Agent'] = get_random_user_agent()
    response = requests.get(url, headers=headers, verify=False,
                 timeout=timeout, proxies=ANONYMIZER_PROXIES, auth=ANONYMIZER_AUTH)
    if response and response.ok:
        return response
    else:
        return None


import shutil
def image_slurper(url, timeout=7.0):
    headers['User-Agent'] = get_random_user_agent()
    response = requests.get(url, headers=headers, stream=True,
                 timeout=timeout, proxies=ANONYMIZER_PROXIES, auth=ANONYMIZER_AUTH)
    if response and response.ok:
        url_file = filename_from_url_no_extension(url)
        with open(facc('slurp_images/' + url_file + '.png'), 'wb') as out_file:
            shutil.copyfileobj(response.raw, out_file)
    else:
        return None



def html_is_valid(html):
    if html:
        return True
    else:
        return False

def log_progress(msg, filename='progress_log.log'):
#     print hms_message(msg)
    log_to_file(filename, msg)

def log_error(msg, filename='progress_log.log'):
#     print hms_message('ERROR: ' + msg)
    log_to_file(filename, 'ERROR: ' + msg)

def file_path_of_slurp(slurp_spec):
    return os.path.join(save_folder, filename_from_url(slurp_spec))

def save_html_of_slurp(html, slurp_spec):
    save_text_to_file(s=html, filepath=file_path_of_slurp(slurp_spec))

def slurp_already_saved(slurp_spec):
    return os.path.exists(file_path_of_slurp(slurp_spec))


###### MAKE SEARCH TERMS

# SEEDS
searchterms_dict = dict()
searchterms_dict['who'] = ['deaf', '"hard of hearing"', '"hearing impaired"',
          '"hearing impairment"', '"hearing loss"']
searchterms_dict['what'] = ['clock', '"baby monitor"', '"fire alarm"', '"smoke alarm"', 'alarm']
searchterms_dict['how'] = ['flash', 'flashing', 'vibrate', 'vibrating']
searchterms_dict['where'] = ['', 'site:facebook.com', 'site:youtube.com', 'site:twitter.com']


# GENERATION
import itertools
# QUERIES WITH SITES
query_list_with_sites = [' '.join(x) for x in itertools.product(searchterms_dict['who'],
                                             searchterms_dict['what'],
                                             searchterms_dict['how'],
                                             searchterms_dict['where']  )]
print len(query_list_with_sites)
peep_in_list(query_list_with_sites)


# QUERIES FOR GSERVICES
gservice_query_list = [' '.join(x) for x in itertools.product(searchterms_dict['who'],
                                             searchterms_dict['what'],
                                             searchterms_dict['how'])]
print len(gservice_query_list)
peep_in_list(gservice_query_list)


# AGGREGATE
num_of_pages_per_query = 5

url_list = []
shopping_url_list = mk_url_list_from_queries(gservice_query_list, get_gshop_request_url, num_of_pages_per_query)
url_list += shopping_url_list
url_list += mk_url_list_from_queries(query_list_with_sites, get_gsearch_request_url, num_of_pages_per_query)
url_list += mk_url_list_from_queries(gservice_query_list, get_gnews_request_url, num_of_pages_per_query)
url_list += mk_url_list_from_queries(gservice_query_list, get_gblogs_request_url, num_of_pages_per_query)
print len(url_list)
peep_in_list(url_list)


############ SLURP!

#### SLURP URLS
get_html_of_url = url_slurper
pause_between_slurps_in_seconds = 11.0
log_file = os.path.join(root_folder, 'progress_log.log')

if os.path.exists(log_file):
    os.remove(log_file)

skipped = 0
for i, url in enumerate(url_list):
    try:
#         # skip urls already slurped
#         if slurp_already_saved(url):
#             skipped += 1
#             continue # go to the next url
#         else:
#             if skipped > 0:
#                 log_progress('SKIPPED: %d urls skipped because we already had them.' % skipped, log_file)
#                 skipped = 0 # reset skipped counter
        # slurp
        log_progress('item %d: slurping %s' % (i, url), log_file)
        try:
            html = get_html_of_url(url)
        except BaseException as e:
            log_error('item %d: get_html_of_url(%s): error = %s' % (i, url, e.message), log_file)
            time.sleep(pause_between_slurps_in_seconds)
            continue # go to the next url
        # process
        if html_is_valid(html):
            save_html_of_slurp(html, url)
        else:
            log_error('html not valid: item %d, %s' % (i, url), log_file)
    except BaseException as e:
        log_error('II item %d: get_html_of_url(%s): error = %s' % (i, url, e.message), log_file)
    time.sleep(pause_between_slurps_in_seconds)

log_progress('!!!!!!!!!!!!!! I am DONE !!!!!!!!!!!', log_file)




#### SLURP IMAGES
root_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
parse_dicts_folder = os.path.join(root_folder, 'parse_dicts')

facc = pfile.accessor.for_local(root_folder)
# dfacc = pfile.accessor.for_local(parse_dicts_folder, extension='dict_list', force_extension=True)

list_of_gshop_text_filename = os.path.join(root_folder, 'list_of_gshop_files.txt')


pause_between_slurps_in_seconds = 11.0
log_file = os.path.join(root_folder, 'progress_log.log')

if os.path.exists(log_file):
    os.remove(log_file)

skipped = 0
for i, url in enumerate(url_list):
    try:
#         # skip urls already slurped
#         if slurp_already_saved(url):
#             skipped += 1
#             continue # go to the next url
#         else:
#             if skipped > 0:
#                 log_progress('SKIPPED: %d urls skipped because we already had them.' % skipped, log_file)
#                 skipped = 0 # reset skipped counter
        # slurp
        log_progress('item %d: slurping %s' % (i, url), log_file)
        try:
            image_slurper(url)
        except BaseException as e:
            log_error('item %d: image_slurper(%s): error = %s' % (i, url, e.message), log_file)
            time.sleep(pause_between_slurps_in_seconds)
            continue # go to the next url
    except BaseException as e:
        log_error('II item %d: get_html_of_url(%s): error = %s' % (i, url, e.message), log_file)
    time.sleep(pause_between_slurps_in_seconds)

log_progress('!!!!!!!!!!!!!! I am DONE !!!!!!!!!!!', log_file)



