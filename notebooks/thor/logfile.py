# IPython log file


d = pd.read_pickle(sda.facc('pickles/stripped_url_tail_counts.df'))
d.head()
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
from ms_utils.util.imports.ipython_utils import *
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
from ms_utils.util.imports.ipython_utils import *
import glob
import urllib
import re
import pandas as pd

from ms_utils.util.imports.scraping_imports import *
import ms_utils as ms
import ms_utils.daf.get
from ms_utils.slurp.yboss import Yboss
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker
import ms_utils.daf.gr
import ms_utils.util.log

from global_spa.webscrape.koobecaf import Koobecaf
koob = Koobecaf()

# sda = ScrapesDataAccess()
# yb = Yboss(default_save_folder=sda.data_folders['yboss_df_slurps'])

# print "root folder: %s" % sda.facc('')
# print "yboss_df_slurps folder: %s" % sda.data_folders['yboss_df_slurps']
d = pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))
d.head()
len(d)
import glob
f = glob.glob(koob.facc('facebook_slurps'))
f = glob.glob(koob.sda.facc('facebook_slurps'))
f
f = glob.glob(koob.sda.facc('facebook_slurps')+'*')
f
koob.sda.facc('facebook_slurps')+'*'
koob.sda.facc('facebook_slurps')+'/*'
f = glob.glob(koob.sda.facc('facebook_slurps/*'))
f = glob.glob(koob.sda.facc('facebook_slurps/*'))
len(f)
f[0]
f[-1]
f[-2]
f[-1]
re.compile('Icon\r').search(f[-1])
re.compile('Icon\r').search(f[-1]).group(0)
filter(re.compile('Icon\r').search, f)
set(f).difference(filter(re.compile('Icon\r').search, f))
f = set(f).difference(filter(re.compile('Icon\r').search, f))
f = glob.glob(koob.sda.facc('facebook_slurps/*'))
print len(f)
f = set(f).difference(filter(re.compile('Icon\r').search, f))
print len(f)
koob.sda.url_from_filename(f[0])
f = glob.glob(koob.sda.facc('facebook_slurps/*'))
print len(f)
f = list(set(f).difference(filter(re.compile('Icon\r').search, f)))
print len(f)
koob.sda.url_from_filename(f[0])
import glob
import urllib
import re
import pandas as pd

from ms_utils.util.imports.scraping_imports import *
import ms_utils as ms
import ms_utils.daf.get
from ms_utils.slurp.yboss import Yboss
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker
import ms_utils.daf.gr
import ms_utils.util.log

from global_spa.webscrape.koobecaf import Koobecaf
koob = Koobecaf()

# sda = ScrapesDataAccess()
# yb = Yboss(default_save_folder=sda.data_folders['yboss_df_slurps'])

# print "root folder: %s" % sda.facc('')
# print "yboss_df_slurps folder: %s" % sda.data_folders['yboss_df_slurps']
f = glob.glob(koob.sda.facc('facebook_slurps/*'))
print len(f)
f = list(set(f).difference(filter(re.compile('Icon\r').search, f)))
print len(f)
koob.sda.url_from_filename(f[0])
koob.sda.url_from_filename(f[0]).replace('https://www.facebook.com','')
import glob
import urllib
import re
import pandas as pd

from ms_utils.util.imports.scraping_imports import *
import ms_utils as ms
import ms_utils.daf.get
from ms_utils.slurp.yboss import Yboss
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker
import ms_utils.daf.gr
import ms_utils.util.log

from global_spa.webscrape.koobecaf import Koobecaf
koob = Koobecaf()
f = glob.glob(koob.sda.facc('facebook_slurps/*'))
print len(f)
f = list(set(f).difference(filter(re.compile('Icon\r').search, f)))
print len(f)
ff = map(koob.url_to_url_tail, f)
ff[0]
ff[1]
ff = map(koob.filename_to_url_tail, f)
ff[1]
ff[3]
import glob
import urllib
import re
import pandas as pd

from ms_utils.util.imports.scraping_imports import *
import ms_utils as ms
import ms_utils.daf.get
from ms_utils.slurp.yboss import Yboss
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker
import ms_utils.daf.gr
import ms_utils.util.log
import ms_utils.pfile.to

from global_spa.webscrape.koobecaf import Koobecaf
koob = Koobecaf()
dd = list()
for fi in f:
    ddi = {'url_tail': koob.filename_to_url_tail(fi)}
    ddi['likes'] = koob.get_num_of_likes(BeautifulSoup(ms.pfile.to.str(fi)))
    dd.append(ddi)
df = pd.DataFrame(dd)
len(df)
df.head()
filter(None, df['likes'])
dff = df[df['likes'].nonzero()]
print len(dff)
dff.head()
dff = df[np.array(df['likes']).nonzero()]
print len(dff)
dff.head()
df[likes].nonzero()
df['likes'].nonzero()
dff = df[df['likes'].nonzero()]
print len(dff)
dff.head()
dff = df.iloc[df['likes'].nonzero()]
print len(dff)
dff.head()
df = pd.DataFrame(dd)
print len(df)
df.head()
4[4]
#koob.slurp_non_existing(map(koob.url_tail_to_url, list(d['url_tail'])))

# n = len(d)
# pause_seconds_before_slurp = 3
# root_url = 'https://www.facebook.com'
# for i in range(10, n):
    
#     try:
#         url = root_url + d.iloc[i]['url_tail']
#         logging.info(ms.util.log.hms_message('(%d/%d) %s' % (i,n,url)))
#         html = get_html(url, pause_seconds_before_slurp)  # this function will get it from file if exists, or else, get it on the web and save it to file
#         b = BeautifulSoup(html)
#     except Exception as e:
#         logging.exception("first part of processing: %s" % url)
        
#     try:
#         d['likes'].iloc[i] = get_num_of_likes(b)
#     except Exception as e:
#         logging.exception("second part of processing: %s" % url)
#         continue
    
# #     if mod(i+1,10) == 0:
# #         sda.facc.save(d[:i], 'pickles/url_tail_counts_and_likes.df')
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df')))[['url_tail']])
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail']])
len(dfff)
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail']])
len(dfff)
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
len(dfff)
print len(dff)
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(dfff)
dfff.head()
print len(dff)
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(dfff)
dfff = dfff[['url_tail', 'likes', 'count']].sort(['count', 'likes'], ascending=False).reset_index(drop=True)
dfff.head()
print len(df)
dff = df.iloc[df['likes'].nonzero()]
print len(dff)
dff = dff.drop_duplicates('url_tail')
print (dff)
dff.head()
print len(df)
dff = df.iloc[df['likes'].nonzero()]
print len(dff)
dff = dff.drop_duplicates('url_tail')
print len(dff)
dff.head()
print len(dff)
dfff = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(dfff)
dfff = dfff[['url_tail', 'likes', 'count']].sort(['count', 'likes'], ascending=False).reset_index(drop=True)
dfff.head()
import glob
import urllib
import re
import pandas as pd

from ms_utils.util.imports.scraping_imports import *
import ms_utils as ms
import ms_utils.daf.get
from ms_utils.slurp.yboss import Yboss
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import global_spa.slurp.search_term_maker as search_term_maker
import ms_utils.daf.gr
import ms_utils.util.log
import ms_utils.pfile.to

from global_spa.webscrape.koobecaf import Koobecaf
koob = Koobecaf()
print len(dff)
d = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(d)
d = koob.process_df(d)
d = d[['url_tail', 'likes', 'count']].sort(['count', 'likes'], ascending=False).reset_index(drop=True)
d.head()
koob = Koobecaf()
print len(dff)
d = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(d)
d = koob.process_df(d)
d = d[['url_tail', 'likes', 'count']].sort(['count', 'likes'], ascending=False).reset_index(drop=True)
d.head()
print len(dff)
d = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(d)
d = koob.process_df(d)
d = d[['url_tail', 'likes', 'count']].sort(['count', 'likes'], ascending=False).reset_index(drop=True)
d.head()
df.columns
if 'likes' in df.columns:
    print "asdf"
if 'likesa' in df.columns:
    print "asdf"
if 'likes' in df.columns:
    print "asdf"
if 'likes' in df.columns and (isinstance(df.iloc['likes'][0], basestring)):
    print "boo"
if ('likes' in df.columns) and (isinstance(df.iloc['likes'][0], basestring)):
    print "boo"
if ('likes' in df.columns) && (isinstance(df.iloc['likes'][0], basestring)):
    print "boo"
if ('likes' in df.columns) & (isinstance(df.iloc['likes'][0], basestring)):
    print "boo"
print len(dff)
d = dff.merge(pd.read_pickle(koob.sda.facc('pickles/stripped_url_tail_counts.df'))[['url_tail', 'count']])
print len(d)
d = koob.process_df(d)
d = d[['url_tail', 'likes', 'count']].sort(['count', 'likes'], ascending=False).reset_index(drop=True)
d.head()
