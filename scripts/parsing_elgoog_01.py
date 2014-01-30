__author__ = 'thor'

import os

from bs4 import BeautifulSoup
from datetime import datetime

import pfile.to
import pstr.to
import pstr.trans
import pickle
import time

import pprint
ppr = pprint.PrettyPrinter(indent=4)

##########
# SETTINGS
root_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
slurps_folder = os.path.join(root_folder, 'slurps')
parse_dicts_folder = os.path.join(root_folder, 'parse_dicts')
list_of_gshop_text_filename = os.path.join(root_folder, 'list_of_gshop_files.txt')



###########
# UTILS

def peep_in_list(A):
    print "The list has %d elements" % len(A)
    print "Here are elements of indices 0, 1, -2, and -1:"
    print "-----------------------------------------------"
    print A[0]
    print A[1]
    print A[-2]
    print A[-1]

def log_to_file(filename, msg):
    with open(filename, "a") as myfile:
        myfile.write(hms_message() + msg + "\n")

def hms_message(msg=''):
    t = datetime.now().time()
    return "%02.0f:%02.0f:%02.0f - %s" % (t.hour, t.minute, t.second, msg)


def peep_in_results(file_info_dict, result_idx=0, item_idx=0):
    result = file_info_dict[result_idx]
    parsed_result = result['parse_dict']
    print result['file']
    print '------------------------'
    if item_idx < len(parsed_result):
        ppr.pprint(parsed_result[item_idx])
        return parsed_result[item_idx], parsed_result, result
    else:
        print "there's only %d items in that file" % len(parsed_result)



###########
# PARSING UTILS

def parse_gshop(soup):
    items = soup.findAll('li', attrs={'class':'g'})
    if items:
        items = [parse_gshop_item(t) for t in items]
    return items

def parse_gshop_item(t):
    parse_dict = dict()
    # psliimg section
    tt = t.find('div', attrs={'class':'psliimg'})
    if tt:
        ttt = tt.find('img')
        if ttt:
            x = ttt.get('alt')
            if x:
                parse_dict['img_alt'] = x
            x = ttt.get('src')
            if x:
                parse_dict['img_src'] = x
    # psliprice section
    tt = t.find('div', attrs={'class':'psliprice'})
    if tt:
        parse_dict['psliprice_divs_html'] = [x.renderContents() for x in tt.findAll('div')]
        parse_dict['psliprice_divs_text'] = [x.get_text() for x in tt.findAll('div')]
    # pslimain section
    tt = t.find('div', attrs={'class':'pslimain'})
    if tt:
        # title
        ttt = tt.find('h3')
        if ttt:
            x = ttt.find('a')
            parse_dict['href'] = x['href']
            parse_dict['href_text'] = x.get_text()
        # description
        ttt = tt.find('div')
        if ttt:
            parse_dict['desc'] = ttt.get_text()
    return parse_dict


# get the list of google shopping filenames into a file
shop_re = 'tbm=shop'
t = os.popen('ls "%s" | grep  %s > "%s"' % (slurps_folder, shop_re, list_of_gshop_text_filename))
print t


# creating a list of filenames
file_list = pfile.to.str(list_of_gshop_text_filename).split('\n')[0:-1]
peep_in_list(file_list)


file_info_dict = [{'file':f, 'filepath':os.path.join(slurps_folder, f)} for f in file_list]
n = len(file_info_dict)
print n

start_at = 448 - 2
file_list = file_list[start_at:]
n = len(file_list)
print n
print "_------------"
for i, fi in enumerate(file_list):
    try:
        target_file_path = os.path.join(parse_dicts_folder,
                                        pfile.name.replace_extension(fi, '.dict_list'))
        if not os.path.exists(target_file_path):
            log_to_file('log.log', "%d/%d: %s" % (i,n,fi))
            time.sleep(1.5)
            s = pfile.to.str(os.path.join(slurps_folder, fi))
            s = pstr.trans.str_to_unicode_or_bust(s)
            parse_dict = parse_gshop(BeautifulSoup(s))
            pickle.dump(parse_dict, open(target_file_path,'wb'))
        else:
            continue
    except BaseException as e:
        log_to_file('log.log', " - ERROR: %d/%d: %s: %s" % (i,n,fi,e.message))

