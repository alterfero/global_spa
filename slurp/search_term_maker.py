__author__ = 'thor'

import itertools
import global_spa as gs


def mk_url_list_from_queries(query_list, get_url_fun, result_page_number=0):
    return [get_url_fun(x, y) for x in query_list for y in range(result_page_number)]

# SEEDS
product_term_seeds_dict = dict()
product_term_seeds_dict['who'] = ['deaf', '"hard of hearing"', '"hearing impaired"',
          '"hearing impairment"', '"hearing loss"']
product_term_seeds_dict['what'] = ['clock', '"baby monitor"', '"fire alarm"', '"smoke alarm"', 'alarm']
product_term_seeds_dict['how'] = ['flash', 'flashing', 'vibrate', 'vibrating']
product_term_seeds_dict['where'] = ['site:facebook.com', 'site:youtube.com', 'site:twitter.com']


def mk_who_what_how_where():
    return [' '.join(x) for x in itertools.product(product_term_seeds_dict['who'],
                                             product_term_seeds_dict['what'],
                                             product_term_seeds_dict['how'],
                                             product_term_seeds_dict['where'])]


def mk_who_what_how():
    return [' '.join(x) for x in itertools.product(product_term_seeds_dict['who'],
                                             product_term_seeds_dict['what'],
                                             product_term_seeds_dict['how'])]

