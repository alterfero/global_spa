__author__ = 'thor'

import ms_utils as ms
import os


class DefaultDataAccessParams(object):
    def __init__(self, location='loc', data_root_folder=None):
        if location == 'loc':
            self.data_root_folder = data_root_folder or os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
            self.facc = ms.pfile.accessor.for_local(self.data_root_folder)

            self.data_folders = dict()
            self.data_folders['root'] = self.data_root_folder
            self.data_folders['slurps'] = os.path.join(self.data_root_folder, 'slurps')
            self.data_folders['parse_dicts'] = os.path.join(self.data_root_folder, 'parse_dicts')
            self.data_folders['slurp_images'] = os.path.join(self.data_root_folder, 'slurp_images')


