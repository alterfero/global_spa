__author__ = 'thor'


import os
import pickle
import time
import pandas as pd

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



def mk_item_info_dict(parse_dict_item):
    info_dict = dict()
    if 'desc' in parse_dict_item.keys():
        info_dict['desc'] = parse_dict_item['desc']
#     info_dict['href'] = parse_dict_item['href']
    if 'img_src' in parse_dict_item.keys():
        info_dict['img_src'] = parse_dict_item['img_src']
    if 'href_text' in parse_dict_item.keys():
        info_dict['title'] = parse_dict_item['href_text']
    if 'psliprice_divs_text' in parse_dict_item.keys():
        t = parse_dict_item['psliprice_divs_text']
        if len(t) >= 2:
            info_dict['price_str'] = t[0]
            info_dict['provider'] = t[1]
    return info_dict

def mk_item_info_df_from_parse_dict(parse_dict):
    return pd.DataFrame([mk_item_info_dict(dd) for dd in parse_dict])

def mk_item_info_df_from_multiple_parse_dicts(parse_dict_enum):
    df = pd.DataFrame()
    for parse_dict in parse_dict_enum:
        df = pd.concat([df, mk_item_info_df_from_parse_dict(parse_dict)])
    return df.reset_index(drop=True)

# class DictLoader:
#     def __init__(self, dict_source=None, max_idx=None):
#         self.dict_list = os.listdir(parse_dicts_folder)[:-1]
#         self.max_idx = max_idx or (len(self.dict_list)-1)
#         self.idx = -1
#         if dict_source:
#             if hasattr(dict_source, 'load'):
#                 self.dict_facc = dict_source
#             elif isinstance(dict_source, basestring):
#                 import ms_utils.pfile.accessor as faccessor
#                 self.dict_facc  = faccessor.for_local(dict_source)
#             else:
#                 raise TypeError("can't handle the type of dict_source")
#         else:
#             pass
#             # self.dict_facc = gacc.parse_dicts_local()
#
#     def __iter__(self):
#         return self
#
#     def next(self):
#         self.idx += 1
#         if self.idx > self.max_idx:
#             raise StopIteration
#         else:
#             return self.dict_facc.load(self.dict_list[self.idx])