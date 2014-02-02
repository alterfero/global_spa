__author__ = 'thor'

import glob
import os

import ms_utils as ms
from global_spa.data_access.default_data_access_params import DefaultDataAccessParams
import ms_utils.util.pobj
import ms_utils.pfile.accessor
from ms_utils.pfile.name import ensure_slash_suffix


class ScrapesDataAccess(DefaultDataAccessParams):
    def __init__(self, **kwargs):
        self = ms.util.pobj.set_attributes(self, kwargs, DefaultDataAccessParams().__dict__)

    def get_accessor(self, accessor_name, **kwargs):
        if accessor_name == 'slurps':
            return ms.pfile.accessor.for_local(self.data_folders[accessor_name],
                                               extension='.html', force_extension=True)
        elif accessor_name == 'parse_dicts':
            return ms.pfile.accessor.for_local(self.data_folders[accessor_name],
                                               extension='.dict_list', force_extension=True)
        elif accessor_name in self.data_folders:  # if accessor_name name is listed in data_folders
            return ms.pfile.accessor.for_local(self.data_folders[accessor_name])
        elif os.path.exists(accessor_name):  # if not, check if the file/folder exists
            return glob.iglob(ensure_slash_suffix(self.data_folders[accessor_name]) + '*')
        else:
            raise ValueError("Unknown accessor_name")

    def get_file_location_generator(self, generator_name):
        if generator_name in self.data_folders:  # if generator name is listed in data_folders
            return glob.iglob(ensure_slash_suffix(self.data_folders[generator_name]) + '*')
        elif os.path.exists(generator_name):  # if not, check if the file/folder exists
            return glob.iglob(ensure_slash_suffix(generator_name) + '*')
        else:
            raise ValueError("Unknown generator_name")