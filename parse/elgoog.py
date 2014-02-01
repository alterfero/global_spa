__author__ = 'thor'


import os
import pickle
import time

from bs4 import BeautifulSoup

import ms_utils as ms
import ms_utils.pfile.to
import ms_utils.pstr.trans

from utils.log import log_to_file

import pprint
ppr = pprint.PrettyPrinter(indent=2)


##########
# SETTINGS
root_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
slurps_folder = os.path.join(root_folder, 'slurps')
parse_dicts_folder = os.path.join(root_folder, 'parse_dicts')
list_of_gshop_text_filename = os.path.join(root_folder, 'list_of_gshop_files.txt')


###########
# UTILS


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


def gshop_file_list(file_list, from_idx=0, to_idx=None):
    n = len(file_list)
    to_idx = to_idx or n
    # take subset of file_list
    file_list = file_list[from_idx:to_idx]
    print n
    print "-------- Will now parse %d files ------------" % n
    for i, fi in enumerate(file_list):
        try:
            target_file_path = os.path.join(parse_dicts_folder,
                                            ms.pfile.name.replace_extension(fi, '.dict_list'))
            if not os.path.exists(target_file_path):
                log_to_file('log.log', "%d/%d: %s" % (i, n, fi))
                time.sleep(1.5)
                s = ms.pfile.to.str(os.path.join(slurps_folder, fi))
                s = ms.pstr.trans.str_to_unicode_or_bust(s)
                parse_dict = parse_gshop(BeautifulSoup(s))
                pickle.dump(parse_dict, open(target_file_path, 'wb'))
            else:
                continue
        except BaseException as e:
            log_to_file('log.log', " - ERROR: %d/%d: %s: %s" % (i, n, fi, e.message))
