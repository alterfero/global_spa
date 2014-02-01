__author__ = 'thor'

from ms_utils import pfile
#import global_spa as gs
import global_spa.data_access.config as config


def parse_dicts_local():
    return pfile.accessor.for_local(config.parse_dicts_folder, extension='dict_list', force_extension=True)
