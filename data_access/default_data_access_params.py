__author__ = 'thor'

import ms_utils as ms
import os


class DefaultDataAccessParams(object):
    def __init__(self, location='loc', data_root_folder=None):
        if location == 'loc':
            self.data_root_folder = data_root_folder or os.path.join(os.environ['GD_FOLDER'], 'Shared/ms_otosense')
            self.facc = ms.pfile.accessor.for_local(self.data_root_folder)

            ##################################################################
            # data folders
            self.data_folders = dict()
            self.data_folders['root'] = self.data_root_folder
            self.data_folders['log'] = os.path.join(self.data_root_folder, 'log')
            self.data_folders['slurps'] = os.path.join(self.data_root_folder, 'slurps')
            self.data_folders['yboss_df_slurps'] = os.path.join(self.data_root_folder, 'yboss_df_slurps')
            self.data_folders['parse_dicts'] = os.path.join(self.data_root_folder, 'parse_dicts')
            self.data_folders['slurp_images'] = os.path.join(self.data_root_folder, 'slurp_images')
            self.data_folders['facebook_slurps'] = os.path.join(self.data_root_folder, 'facebook_slurps')
            self.data_folders['pickles'] = os.path.join(self.data_root_folder, 'pickles')

            ##################################################################
            # glob filters
            self.glob_filters = dict()
            self.glob_filters['elgoog'] = 'http*{**www.google.com*'
            self.glob_filters['yboss_df_slurps'] = self.data_folders['yboss_df_slurps'] + '/*'

            self.glob_filters['file_with_ext'] = '*.*'
            self.glob_filters['html'] = '*.html'

            self.glob_filters['gshop'] = self.glob_filters['elgoog'] + '*tbm=shop*'
            self.glob_filters['gblog'] = self.glob_filters['elgoog'] + '*tbm=blg*'
            self.glob_filters['gnews'] = self.glob_filters['elgoog'] + '*tbm=nws*'

            self.glob_filters['gfacebook'] = self.glob_filters['elgoog'] + '*site%3Afacebook.com*'
            self.glob_filters['gtwitter'] = self.glob_filters['elgoog'] + '*site%3Afacebook*'
            self.glob_filters['gyoutube'] = self.glob_filters['elgoog'] + '*site%3Ayoutube.com*'

            self.glob_filters['yboss_blogs'] = self.glob_filters['yboss_df_slurps'] + '*blogs=*'
            self.glob_filters['yboss_limitedweb'] = self.glob_filters['yboss_df_slurps'] + 'limitedweb=*'
            self.glob_filters['yboss_facebook'] = self.glob_filters['yboss_df_slurps'] + 'site*facebook.com*'

            self.deaf_synonyms = ['deaf', 'hearing impaired', 'hard of hearing',
                                  'hearing impairment', 'hearing loss',
                                  'deafened', 'earless', 'unable to hear']
