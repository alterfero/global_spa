__author__ = 'thor'

import functional

import ms_utils as ms
from ms_utils.webscrape.yboss import YbossText
from ms_utils.semantics.text_processors import TermReplacer
from global_spa.data_access.default_data_access_params import DefaultDataAccessParams


class Semantics(object):
    def __init__(self):
        params = dict()
        ddap = DefaultDataAccessParams()
        params['term_map'] = dict()
        for w in ddap.deaf_synonyms:
            params['term_map'] = dict(params['term_map'], **{w: '_' + w.replace(' ', '_')})
        self.text_processor = functional.compose(
            TermReplacer(params['term_map'], term_padding_exp=r'\b').replace_terms, YbossText.toascii_lower)

    def tc_flat_from_yb(self, yb):
        return YbossText.tc_flat(yb, self.text_processor)


