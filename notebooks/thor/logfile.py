# IPython log file


get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
import global_spa as gs
import ms_utils as ms
import global_spa.data_access.accessors as gaccs
import glob
from global_spa.data_access.setup import *
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa as gs
import ms_utils as ms
import global_spa.data_access.accessors as gaccs
import glob
from global_spa.data_access.nb_setup import *
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
get_ipython().magic(u'whos ')
sda = ScrapesDataAccess()
sda = ScrapesDataAccess()
fg = sda.get_file_location_generator('slurp_images')
# fg = get_generator('slurp_images')
fg.next()
fg.next()
fg = sda.get_file_location_generator('slurp_images')
# fg = get_generator('slurp_images')
fg.next()
fg = sda.get_file_location_generator('slurp_images')
# fg = get_generator('slurp_images')
imfile = fg.next()
imfile
