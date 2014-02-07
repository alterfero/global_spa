# IPython log file


from ms_utils.slurp.yboss import Yboss
yb = Yboss()
yb.url_encode_params({'aaa':'the en-us monkey is "gone"', 'a':34})
urllib.urlencode({'aaa':'the en-us monkey is "gone"', 'a':34})
import urllib
urllib.urlencode({'aaa':'the en-us monkey is "gone"', 'a':34})
import os
import os
f = os.path.join(save_folder, 'limitedweb=deaf+clock+vibrate.df')
n_pages = 10
root_folder = '/Users/thor/Google Drive/Shared/ms_otosense/'
save_folder = os.path.join(root_folder,'yboss_df_slurps/')
import os
f = os.path.join(save_folder, 'limitedweb=deaf+clock+vibrate.df')
import pandas as pd
pd.load(f)
df = pd.read_pickle(f)
len(df)
df.head()
import glob
ff = glob.iglob(save_folder + 'blogs=')
len(ff)
ff = glob.glob(save_folder + 'blogs=')
len(ff)
ff = glob.glob(save_folder + 'blogs')
len(ff)
ff = glob.glob(save_folder + '/blogs')
len(ff)
save_folder
ff = glob.glob(save_folder + 'blogs=*')
len(ff)
df = reduce(lambda x,y: pd.concat([x,pd.read_pickle(y)]), ff, pd.DataFrame())
len(df)
df.head()
dg = group_and_count(df[['dispurl']])
import ms_utils as ms
import ms_utils.daf.gr
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg.head()
print len(dg)
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort()
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort(ascending=False)
print len(dg)
dg.head()
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort(colmns=['count'], ascending=False)
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort(columns==['count'], ascending=False)
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort(columns=['count'], ascending=False)
print len(dg)
dg.head()
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort(columns=['count'], ascending=False)
dg = dg.reset_index(drop=False)
print len(dg)
dg.head()
dg = ms.daf.gr.group_and_count(df[['dispurl']])
dg = dg.sort(columns=['count'], ascending=False)
dg = dg.reset_index(drop=True)
print len(dg)
dg.head()
dg = dg.to_excel(os.path.join(root_folder, 'most_frequent_urls_in_blog_results.xlsx'))
import tldextract
t = tldextract.extract('http://www.google.com')
t
t['domain']
t.domain
t.domain + t.suffix
t.domain + '.' + t.suffix
import tldextract
def get_domain(url):
    t = tldextract.extract(url)
    return t.domain + '.' + t.suffix
d = df[['dispurl']]
d['domain'] = map(get_domain, d['dispurl'])
d.head()
t = tldextract.extract('http://suddensilence.wordpress.com/2009/06/15/')
t = tldextract.extract('http://suddensilence.wordpress.com/2009/06/15/')
t
import tldextract
def get_domain(url):
    t = tldextract.extract(url)
    return t.domain + '.' + t.suffix
def get_sub_domain(url):
    t = tldextract.extract(url)
    return t.subdomain + '.' + t.domain + '.' + t.suffix
d = df[['dispurl']]
d['domain'] = map(get_domain, d['dispurl'])
d['sub_domain'] = map(get_sub_domain, d['dispurl'])
d.head()
dg = d[['sub_domain']]
dg = ms.daf.gr.group_and_count(df[['sub_domain']])
dg = dg.sort(columns=['count'], ascending=False)
dg = dg.reset_index(drop=True)
dg.head(3)
dg = d[['sub_domain']]
dg = ms.daf.gr.group_and_count(dg[['sub_domain']])
dg = dg.sort(columns=['count'], ascending=False)
dg = dg.reset_index(drop=True)
dg.head(3)
dg = d[['sub_domain']]
dg = ms.daf.gr.group_and_count(dg[['sub_domain']])
dg = dg.sort(columns=['count'], ascending=False)
dg = dg.reset_index(drop=True)
print len(dg)
print dg.head(3)
dg.to_excel(os.path.join(root_folder, 'sub_domain_counts_in_blogs.xlsx'))
dg = d[['domain']]
dg = ms.daf.gr.group_and_count(dg[['domain']])
dg = dg.sort(columns=['count'], ascending=False)
dg = dg.reset_index(drop=True)
print len(dg)
print dg.head(3)
dg.to_excel(os.path.join(root_folder, 'domain_counts_in_blogs.xlsx'))
d = df[['author']]
d.head()
d.tail()
df.tail()
df.tail
len(df)
df.head()
df.iloc[0]['abstract']
df = reduce(lambda x,y: pd.concat([x,pd.read_pickle(y)]), ff, pd.DataFrame())
len(df)
df.head()
t = tldextract.extract('http://suddensilence.wordpress.com/2009/06/15/')
t
t = tldextract.extract('http://ellieyay.blogspot.com/2005/12/wellwellll.html')
t
t = tldextract.extract('ellieyay.blogspot.com/2005/12/wellwellll.html')
t
t = tldextract.extract('ellieyay.blogspot.com')
t
t = tldextract.extract('ellieyay.google.com')
t
t = tldextract.extract('ellieyay.blogspot.com')
t
df._totalresults
ff[0]
t = pd.read_pickle(ff[0])
t.head()
t = pd.read_pickle(ff[1])
t.head()
ff[0]
print len(pd.read_pickle(ff[0]))
print len(pd.read_pickle(ff[1]))
print len(pd.read_pickle(ff[2]))
print len(pd.read_pickle(ff[3]))
print len(pd.read_pickle(ff[0]))
print len(pd.read_pickle(ff[1]))
print len(pd.read_pickle(ff[2]))
print len(pd.read_pickle(ff[-1]))
print ff[0]
print ff[1]
