__author__ = 'thor'

import os
from ms_utils import pfile

root_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
parse_dicts_folder = os.path.join(root_folder, 'parse_dicts')

facc = pfile.accessor.for_local(root_folder)
dfacc = pfile.accessor.for_local(parse_dicts_folder, extension='dict_list', force_extension=True)

list_of_gshop_text_filename = os.path.join(root_folder, 'list_of_gshop_files.txt')