__author__ = 'thor'

import os

import ms_utils as ms
import ms_utils.pfile.to

from utils.list import peep_in_list

import parse.elgoog


# get the list of google shopping filenames into a file
shop_re = 'tbm=shop'
t = os.popen('ls "%s" | grep  %s > "%s"'
             % (parse.elgoog.slurps_folder, shop_re, parse.elgoog.list_of_gshop_text_filename))
print t

# creating a list of filenames
file_list = ms.pfile.to.str(parse.elgoog.list_of_gshop_text_filename).split('\n')[0:-1]
peep_in_list(file_list)


file_info_dict = [{'file':f, 'filepath':os.path.join(parse.elgoog.slurps_folder, f)} for f in file_list]
n = len(file_info_dict)
print n


parse.elgoog.gshop_file_list(file_list, from_idx=448 - 2)

