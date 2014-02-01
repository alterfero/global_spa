__author__ = 'thor'

import os
import ms_utils as ms
import ms_utils.pfile.accessor

data_root_folder = os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
parse_dicts_folder = os.path.join(data_root_folder, 'parse_dicts')

facc = ms.pfile.accessor.for_local(data_root_folder)



