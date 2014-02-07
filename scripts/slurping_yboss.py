__author__ = 'thor'

import os

import global_spa.slurp.search_term_maker as search_term_maker
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess

from ms_utils.slurp.yboss import Yboss

sda = ScrapesDataAccess

yb = Yboss()

search_term_maker.mk_who_what_how()
search_term_maker.mk_who_what_how_where()


n_pages = 10



