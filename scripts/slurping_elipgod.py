__author__ = 'thor'



import os
from bs4 import BeautifulSoup
import requests
import re
import urlparse
import urllib
from datetime import datetime



##########
# SETTINGS
save_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
user_agent = 'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/532.2 ' \
             '(KHTML, like Gecko) Chrome/4.0.222.5 Safari/532.2'

################################################
# UTILS

html_re = re.compile('\.html$')

def url_encode(query):
    # look at urlparse for cleaner ways to do this
    return urllib.urlencode({'':query})[1:]

def hms_message(msg=''):
    t = datetime.now().time()
    return "%d:%d:%d - %s" % (t.hour, t.minute, t.second, msg)

def save_text_to_file(s, filepath):
    text_file = open(filepath, "w")
    text_file.write(s.encode('utf-8'))
    text_file.close()

def filename_from_url(url):
    return url.replace('/', '§').replace(':', '{') + '.html'

def url_from_filename(filename):
    return html_re.sub('', filename.replace('§', '/').replace('{', ':'))


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


################################################
# GENERAL METHODS

def get_url_from_seed(seed):
    return get_dogpile_request_url(seed)

def get_html_from_seed(seed):
    url = get_url_from_seed(seed)
    return get_html_of_url(url)

def get_html_of_url(url):
#     headers = {'User-Agent': user_agent}
#     response = requests.get(url=url, headers=headers)
    response = requests.get(url=url)
    if response and response.ok:
        return response.text
    else:
        return None

def html_is_valid(html):
    if html:
        return True
    else:
        return False

def log_progress(msg):
    print hms_message(msg)

def log_error(msg):
    print hms_message('ERROR: ' + msg)

def file_path_of_slurp(slurp_spec):
    return os.path.join(save_folder, filename_from_url(slurp_spec))

def save_html_of_slurp(html, slurp_spec):
    save_text_to_file(s=html, filepath=file_path_of_slurp(slurp_spec))


####### Parsing


def get_link_from_results(results_soup):
    urlpane = results_soup.find('div', attrs={'class': 'resultDisplayUrlPane'})
    return urlparse.parse_qs(urlpane.find('a', attrs='resultDisplayUrl').attrs['href'])['ru'][0]


def get_title_text_from_results(results_soup):
    return results_soup.find('div', attrs={'class': 'resultTitlePane'}).get_text()


def get_description_text_from_results(results_soup):
    return results_soup.find('div', attrs={'class': 'resultDescription'}).get_text()


def get_web_results_dict_from_results_soup(results_soup):
    return {
            'link':get_link_from_results(results_soup),
            'title':get_title_text_from_results(results_soup),
            'description':get_description_text_from_results(results_soup)
            }


def parse_dogpile_html(html):
    b = BeautifulSoup(html)

    result_tags = ['resultsAdsTop', 'resultsMain', 'resultsAdsBottom']
    parse_dict = {k: b.find('div',attrs={'id':k}) for k in result_tags}

    parse_dict['resultsAdsTop'] = parse_dict['resultsAdsTop'].findAll('div',attrs={'class':'searchResult adResult'})
    parse_dict['resultsMain'] = parse_dict['resultsMain'].findAll('div',attrs={'class':'searchResult webResult'})
    parse_dict['resultsAdsBottom'] = parse_dict['resultsAdsBottom'].findAll('div',attrs={'class':'searchResult adResult'})

    parse_dict['resultsMain'] = [get_web_results_dict_from_results_soup(r) for r in parse_dict['resultsMain']]

    return parse_dict


def diagnose_parse_dict(parse_dict):
    print "parse_dict_keys: %s" % parse_dict.keys()
    print "number of resultsMain: %d" % len(parse_dict['resultsMain'])
    print parse_dict['resultsMain'][0]