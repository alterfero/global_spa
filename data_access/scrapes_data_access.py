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

    def get_accessor(self, folder_name, **kwargs):
        if folder_name == 'slurps':
            kwargs = dict({'extension': '.html', 'force_extension': True}, **kwargs)
            return ms.pfile.accessor.for_local(root_folder=self.data_folders[folder_name], **kwargs)
        elif folder_name == 'parse_dicts':
            kwargs = dict({'extension': '.dict_list', 'force_extension': True}, **kwargs)
            return ms.pfile.accessor.for_local(root_folder=self.data_folders[folder_name], **kwargs)
        else:
            return ms.pfile.accessor.for_local(root_folder=self.get_data_folder(folder_name), **kwargs)

    def get_file_location_generator(self, folder_name, path_name_suffix_re='*.*'):
        return glob.iglob(
            ensure_slash_suffix(self.get_data_folder(folder_name))
            + self.get_attr_dict_value_or_self('glob_filters', path_name_suffix_re))

    def get_data_folder(self, data_folder_name):
        if data_folder_name in self.data_folders.keys():
            return self.data_folders[data_folder_name]
        elif os.path.exists(data_folder_name):
            return data_folder_name
        elif os.path.exists(os.path.join(self.data_root_folder, data_folder_name)):
            return os.path.join(self.data_root_folder, data_folder_name)
        else:
            raise ValueError("Unknown data_folder: %s" % data_folder_name)

    def get_attr_dict_value_or_self(self, param_name, key_name):
        if not hasattr(self, param_name):
            raise ValueError("There is no %s attribute" % param_name)
        elif not isinstance(getattr(self, param_name), dict):
            raise ValueError("attribute %s should be a dict to do that!" % param_name)
        elif key_name in getattr(self, param_name).keys():
            return getattr(self, param_name)[key_name]
        else:
            return key_name

    @classmethod
    def filename_from_url(cls, url):
        return url.replace('/', '~').replace(':', '{') + '.html'

    @classmethod
    def url_from_filename(cls, filename):
        filename = os.path.basename(filename)
        return filename.replace('.html', '').replace('~', '/').replace('{', ':')

##################################################################
        ### OLD


    # def file_path(self, folder_name, filename=''):
    #     if folder_name in self.data_folders:
    #         return os.path.join(self.data_folders[folder_name], filename)
    #     else:
    #         raise ValueError("Unknown folder_name")
    #
    #
    # def get_file_name(self, key_name, param_name):
    #     """
    #     IF param_name doesn't exist or is not a dict, will return an error
    #     ELIF self.(param_name) has key_name as a key, will return that value
    #     ELIF key_name exists as a name of a file, and will be returned
    #     ELSE raise error
    #     """
    #     if not hasattr(self, param_name):
    #         raise ValueError("There is no %s attribute" % param_name)
    #     elif not isinstance(getattr(self, param_name), dict):
    #         raise ValueError("attribute %s should be a dict to do that!" % param_name)
    #     elif key_name in param_name.keys():
    #         return ensure_slash_suffix(getattr(self, param_name)[key_name])
    #     elif os.path.exists(param_name):
    #         return ensure_slash_suffix(param_name)
    #     elif os.path.exists(os.path.join(self.data_root_folder, param_name)):
    #         return ensure_slash_suffix(os.path.join(self.data_root_folder, param_name))
    #     else:
    #         raise ValueError("Unknown %s: %s" (param_name, key_name))
    #

    # def get_accessor(self, accessor_name, **kwargs):
    #     if accessor_name == 'slurps':
    #         kwargs = dict({'extension': '.html', 'force_extension': True}, **kwargs)
    #         return ms.pfile.accessor.for_local(root_folder=self.data_folders[accessor_name], **kwargs)
    #     elif accessor_name == 'parse_dicts':
    #         kwargs = dict({'extension': '.dict_list', 'force_extension': True}, **kwargs)
    #         return ms.pfile.accessor.for_local(root_folder=self.data_folders[accessor_name], **kwargs)
    #     elif accessor_name in self.data_folders:  # if accessor_name name is listed in data_folders
    #         return ms.pfile.accessor.for_local(root_folder=self.data_folders[accessor_name], **kwargs)
    #     elif os.path.exists(accessor_name):  # if not, check if the file/folder exists
    #         return ms.pfile.accessor.for_local(root_folder=accessor_name, **kwargs)
    #     else:
    #         raise ValueError("Unknown accessor_name")
    #
    # def get_file_location_generator(self, generator_name, path_name_suffix_re=None):
    #     if generator_name in self.data_folders:  # if generator name is listed in data_folders
    #         path_name_suffix_re = path_name_suffix_re or '*.*'
    #         return glob.iglob(ensure_slash_suffix(self.data_folders[generator_name]) + path_name_suffix_re)
    #     elif os.path.exists(generator_name):  # if not, check if the file/folder exists
    #         path_name_suffix_re = path_name_suffix_re or '*'
    #         return glob.iglob(ensure_slash_suffix(generator_name) + path_name_suffix_re)
    #     else:
    #         raise ValueError("Unknown generator_name")
