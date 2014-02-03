# IPython log file


get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')
import numpy as np
import scipy as sp

import pprint
ppr = pprint.PrettyPrinter(indent=4)

import global_spa as gs
import ms_utils as ms
import glob
from global_spa.data_access.nb_setup import *
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
import PIL.Image
import ImageChops
import matplotlib.pyplot as plt

from scipy.misc import imread
get_ipython().magic(u'whos ')
sda = ScrapesDataAccess()  # where most of our parameters and access functions are
ppr.pprint(sda.__dict__)
# set up access to images
imfacc = sda.get_accessor('slurp_images')
def open_image(filepath):
    return PIL.Image.open(filepath)
# choose a few images (the first two are similar)
img = list()
img.append('http{§§t0.gstatic.com§shopping?q=tbn{ANd9GcQruvEIH0LiDP_kQSbHMNQmxZ7fPXxCyig_GhU3C48nmQoEdeBu05QK-B-b9L0bhdtInhZYFQ&usqp=CAE.png')
img.append('http{§§t0.gstatic.com§shopping?q=tbn{ANd9GcQTYJWmInTSU4Ip9AIb19kdn5rC5Xxxyr9iO5CQrvZwRtf-OhQ22AJ2JkpzC5ysCXq3Th8dlA&usqp=CAE.png')
img.append('http{§§t0.gstatic.com§shopping?q=tbn{ANd9GcQu0uo9SbTFPnnOCSSMY36niM1lzM9SYSUIuWvPujiIj1cfbWiO4QHzo4U08mBsNwF62nVrhA&usqp=CAE.png')
img = map(imfacc, img)
# wanna see the images?
fig=plt.figure()
for i, ima in enumerate(img):
    ax=fig.add_subplot(1,3,i+1)        
    ax.imshow(open_image(ima))
# plt.suptitle('The images')
plt.show()    
from ms_utils.pimg.misc import rmsdiff

def rmsdiff_comp(im_file_1,im_file_2):
    return rmsdiff(PIL.Image.open(im_file_1),PIL.Image.open(im_file_2))
from scipy.signal.signaltools import correlate2d

def cross_correlation_comp(im_file_1,im_file_2):
    return c2d(cross_correlation(im_file_1), cross_correlation(im_file_2), mode='same').max()

def cross_correlation(imfile):
    # get JPG image as Scipy array, RGB (3 layer)
    data = imread(imfile)
    # convert to grey-scale using W3C luminance calc
    data = sp.inner(data, [299, 587, 114]) / 1000.0
    # normalize per http://en.wikipedia.org/wiki/Cross-correlation
    return (data - data.mean()) / data.std()
# comp_fun = cross_correlation_comp
comp_fun = rmsdiff_comp
image_filepaths = img
# comp_fun = cross_correlation_comp
comp_fun = rmsdiff_comp
image_filepaths = img
n
# comp_fun = cross_correlation_comp
comp_fun = rmsdiff_comp
image_filepaths = img
n = len(img)
n
n = len(img)
compmat = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        compmat[i,j] = comp_fun(image_filepaths[i],image_filepaths[j])
n = len(img)
compmat = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        compmat[i,j] = comp_fun(image_filepaths[i],image_filepaths[j])
compmat
import numpy as np
import scipy as sp
import pandas as pd

import pprint
ppr = pprint.PrettyPrinter(indent=4)

import global_spa as gs
import ms_utils as ms
import glob
from global_spa.data_access.nb_setup import *
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
pd.DataFrame.from_records(compmat)
pd.DataFrame.from_records(compmat, nrows=9)
pd.DataFrame.from_records(compmat, nrows=8)
pd.DataFrame.from_records(compmat, columns=['aa','bb'])
pd.DataFrame.from_records(compmat, columns=['aa','bb','cc'])
compmat.flatten
compmat.flatten()
# comp_fun = cross_correlation_comp
comp_fun = rmsdiff_comp
image_filepaths = img
n = len(img)
n
n = len(img)
compmat = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        compmat[i,j] = comp_fun(image_filepaths[i],image_filepaths[j])
compmat + compmat.T
(compmat + compmat.T) / 2.
n = len(img)
compmat = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        compmat[i,j] = comp_fun(image_filepaths[i],image_filepaths[j])
compmat = (compmat + compmat.T) / 2.  # yep, because it turns out compmat isn't symetric! uh-oh...
n = len(img)
compmat = np.zeros([n,n])
for i in range(n):
    for j in range(n):
        compmat[i,j] = comp_fun(image_filepaths[i],image_filepaths[j])
compmat = (compmat + compmat.T) / 2.  # yep, because it turns out compmat isn't symetric! uh-oh...
compmat
compmat.flatten()
import itertools
import itertools
itertools.product(*compmat_flat)
compmat_flat = compmat.flatten()
compmat_flat
import itertools
itertools.product(*compmat_flat)
import itertools
itertools.product(*iter(compmat_flat))
import itertools
itertools.product(compmat_flat, compmat_flat)
import itertools
[x for x in itertools.product(compmat_flat, compmat_flat)]
[x for x in itertools.product(compmat, compmat)]
[x for x in itertools.product(compmat)]
import itertools
cart_prod = [x for x in itertools.product(compmat_flat, compmat_flat)]
cart_prod[:5]
import pickle
import numpy as np
import scipy as sp
import pandas as pd
import itertools
import pickle

import pprint
ppr = pprint.PrettyPrinter(indent=4)

import global_spa as gs
import ms_utils as ms
import glob
from global_spa.data_access.nb_setup import *
from global_spa.data_access.scrapes_data_access import ScrapesDataAccess
dist_mat = sda.facc.load(dist_mat, 'image_dist_mat.array')
dist_mat = sda.facc.load('image_dist_mat.array')
imshow(dist_mat[:30,:30], interpolation='none', cmap='hot')
dist_mat = (dist_mat + dist_mat.T) / 2.
sda.facc.save(dist_mat, 'image_dist_mat.array')
imshow(dist_mat[:30,:30], interpolation='none', cmap='hot')
import networkx as nx
import numpy as np
import string
import PIL
from IPython.display import Image

image_file = '/tmp/out.png'

dt = [('len', float)]
A = dist_mat
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

G = nx.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="blue", width="2.0")

G.draw(image_file, format='png', prog='neato')
Image(image_file)
import networkx as nx
import numpy as np
import string
import PIL
from IPython.display import Image

image_file = sda.facc('/images/sample_of_img_dist_matrix.png')
sample_size = 50

dt = [('len', float)]
A = dist_mat[:sample_size][:sample_size]
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

G = nx.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="blue", width="2.0")

G.draw(image_file, format='png', prog='neato')
Image(image_file)
import networkx as nx
import numpy as np
import string
import PIL
from IPython.display import Image

image_file = sda.facc('/images/sample_of_img_dist_matrix.png')
sample_size = 50

dt = [('len', float)]
A = dist_mat[:sample_size,:sample_size]
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

G = nx.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="blue", width="2.0")

G.draw(image_file, format='png', prog='neato')
Image(image_file)
import networkx as nx
import numpy as np
import string
import PIL
from IPython.display import Image

image_file = sda.facc('/images/sample_of_img_dist_matrix.png')
sample_size = 10

dt = [('len', float)]
A = dist_mat[:sample_size,:sample_size]
A = A.view(dt)

G = nx.from_numpy_matrix(A)
G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

G = nx.to_agraph(G)

G.node_attr.update(color="red", style="filled")
G.edge_attr.update(color="blue", width="2.0")

G.draw(image_file, format='png', prog='neato')
Image(image_file)
sda.facc('/images/sample_of_img_dist_matrix.png')
sda
sda.facc('')
sda.facc('images/sample_of_img_dist_matrix.png')
image_file = sda.facc('images/sample_of_img_dist_matrix.png')
import networkx as nx
import numpy as np
import string
import PIL
from IPython.display import Image

# image_file = sda.facc('images/sample_of_img_dist_matrix.png')
# sample_size = 10

# dt = [('len', float)]
# A = dist_mat[:sample_size,:sample_size]
# A = A.view(dt)

# G = nx.from_numpy_matrix(A)
# G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

# G = nx.to_agraph(G)

# G.node_attr.update(color="red", style="filled")
# G.edge_attr.update(color="blue", width="2.0")

G.draw(image_file, format='png', prog='neato')
Image(image_file)
A
import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and an orphan vector
n_points = 100
n_clusters = 3
data = numpy.random.randn(3*n_points,2)
data[:n_points] += 5
data[-n_points:] += 10
data[-1:] -= 20

# real data
n_points = 100
n_clusters = 3
data = dist_mat[:10,:10]
# data = numpy.random.randn(3*n_points,2)
# data[:n_points] += 5
# data[-n_points:] += 10
# data[-1:] -= 20

# clustering
thresh = 1.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

# plotting
plt.scatter(*numpy.transpose(data), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
clusters
import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and an orphan vector
n_points = 100
n_clusters = 3
data = numpy.random.randn(3*n_points,2)
data[:n_points] += 5
data[-n_points:] += 10
data[-1:] -= 20

# real data
n_points = 100
n_clusters = 3
data = dist_mat[:10,:10]
data = compmat_flat
# data = numpy.random.randn(3*n_points,2)
# data[:n_points] += 5
# data[-n_points:] += 10
# data[-1:] -= 20

# clustering
thresh = 1.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

# plotting
plt.scatter(*numpy.transpose(data), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
compmat_flat
import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and an orphan vector
n_points = 100
n_clusters = 3
data = numpy.random.randn(3*n_points,2)
data[:n_points] += 5
data[-n_points:] += 10
data[-1:] -= 20

# real data
n_points = 100
n_clusters = 3
data = dist_mat[:10,:10]
data = compmat
# data = numpy.random.randn(3*n_points,2)
# data[:n_points] += 5
# data[-n_points:] += 10
# data[-1:] -= 20

# clustering
thresh = 1.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

# plotting
plt.scatter(*numpy.transpose(data), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
clusters
import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and an orphan vector
n_points = 100
n_clusters = 3
data = numpy.random.randn(3*n_points,2)
data[:n_points] += 5
data[-n_points:] += 10
data[-1:] -= 20

# real data
n_points = 100
n_clusters = 2
data = dist_mat[:10,:10]
data = compmat
# data = numpy.random.randn(3*n_points,2)
# data[:n_points] += 5
# data[-n_points:] += 10
# data[-1:] -= 20

# clustering
thresh = 1.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

# plotting
plt.scatter(*numpy.transpose(data), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
clusters
import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and an orphan vector
n_points = 100
n_clusters = 3
data = numpy.random.randn(n_clusters*n_points,2)
data[:n_points] += 5
data[-n_points:] += 10
data[-1:] -= 20

# real data
n_points = 100
n_clusters = 2
data = dist_mat[:10,:10]
data = compmat
# data = numpy.random.randn(3*n_points,2)
# data[:n_points] += 5
# data[-n_points:] += 10
# data[-1:] -= 20

# clustering
thresh = 1.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

# plotting
plt.scatter(*numpy.transpose(data), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
clusters
import matplotlib.pyplot as plt
import numpy
import scipy.cluster.hierarchy as hcluster

# generate 3 clusters of each around 100 points and an orphan vector
n_points = 100
n_clusters = 3
data = numpy.random.randn(n_clusters*n_points,2)
data[:n_points] += 5
data[-n_points:] += 10
data[-1:] -= 20

# # real data
# n_points = 100
# n_clusters = 2
# data = dist_mat[:10,:10]
# data = compmat
# # data = numpy.random.randn(3*n_points,2)
# # data[:n_points] += 5
# # data[-n_points:] += 10
# # data[-1:] -= 20

# clustering
thresh = 1.5
clusters = hcluster.fclusterdata(data, thresh, criterion="distance")

# plotting
plt.scatter(*numpy.transpose(data), c=clusters)
plt.axis("equal")
title = "threshold: %f, number of clusters: %d" % (thresh, len(set(clusters)))
plt.title(title)
plt.show()
# import networkx as nx
# import numpy as np
# import string
# import PIL
# from IPython.display import Image

# image_file = sda.facc('images/sample_of_img_dist_matrix.png')
# sample_size = 10

# dt = [('len', float)]
# A = dist_mat[:sample_size,:sample_size]
# A = A.view(dt)

# G = nx.from_numpy_matrix(A)
# G = nx.relabel_nodes(G, dict(zip(range(len(G.nodes())),string.ascii_uppercase)))    

# G = nx.to_agraph(G)

# G.node_attr.update(color="red", style="filled")
# G.edge_attr.update(color="blue", width="2.0")

# G.draw(image_file, format='png', prog='neato')
# # Image(image_file)
hist(dist_mat.flatten())
hist(dist_mat.flatten(), 100)
hist(dist_mat.flatten(), 100);
sda.facc.save(im_filepaths, 'image_dist_mat_file_names.array')
from ms_utils.pimg.misc import rmsdiff

def rmsdiff_comp(im_file_1,im_file_2):
    return rmsdiff(PIL.Image.open(im_file_1),PIL.Image.open(im_file_2))
imgen = sda.get_file_location_generator('slurp_images')
im_filepaths = list(imgen)
n = len(im_filepaths)
n
sda.facc.save(im_filepaths, 'image_dist_mat_file_names.array')
sda.facc.save(im_filepaths, 'image_dist_mat_file_names.list')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
dist_mat = sda.facc.load('image_dist_mat.array')
dist_lidx = dist_mat < 50
len([x for x in dist_lidx if x])
dist_lidx[:50,:50]
sum(dist_lidx)
sum(dist_mat)
sum(dist_lidx)
dist_lidx = dist_mat < 50
sum(dist_lidx)
thresh = 50
dist_lidx = dist_mat < thresh
sum(dist_lidx)
thresh = 40
dist_lidx = dist_mat < thresh
sum(dist_lidx)
thresh = 50
dist_lidx = dist_mat < thresh
sum(dist_lidx)
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1))/2
thresh = 50
dist_lidx = dist_mat < thresh
sum(dist_lidx)
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
thresh = 50
dist_lidx = dist_mat < thresh
sum(dist_lidx)
len(dist_mat)
len(dist_mat)*len(dist_mat)
len(dist_mat)
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
thresh = 60
dist_lidx = dist_mat < thresh
sum(dist_lidx)
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
thresh = 50
dist_lidx = dist_mat < thresh
sum(dist_lidx)
thresh = 50
dist_lidx = dist_mat < thresh
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
print "thresh = %0.02f" % thresh
print "num above thresh = %d" % sum(dist_lidx)
thresh = 80
dist_lidx = dist_mat < thresh
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
print "thresh = %0.02f" % thresh
print "num above thresh = %d" % sum(dist_lidx)
sum(dist_lidx,2)
sum(dist_lidx,0)
sum(dist_lidx,axis=0)
group_sizes = sum(dist_lidx,axis=0)
hist(group_sizes, unique(group_sizes))
group_sizes = sum(dist_lidx,axis=0)
hist(group_sizes, unique(group_sizes));
hist(group_sizes, unique(group_sizes[group_sizes>1]));
group_sizes = sum(dist_lidx,axis=0)
hist(group_sizes, unique(group_sizes));
title('Group Size Histogram')
group_sizes = sum(dist_lidx,axis=0)
hist(group_sizes, unique(group_sizes));
plt.title('Group Size Histogram')
group_sizes = sum(dist_lidx,axis=0)
hist(group_sizes, unique(group_sizes));
plt.title('Group Size Histogram');
hist(group_sizes, unique(group_sizes[group_sizes>1]));
plt.title('Group Size Histogram (without the group_size==1)');
group_sizes==100
[x for x in group_sizes if x==100]
[x for x in group_sizes if x==99]
[x for x in group_sizes if x==98]
[x for x in group_sizes if x==97]
[x for x in group_sizes if x==2]
[x for x in group_sizes if x==90]
[x for x in group_sizes if x==101]
[x for x in group_sizes if x==102]
[x for x in group_sizes if x==10]
len(dist_lidx)
nrows(dist_lidx)
nrow(dist_lidx)
dist_lidx.ndim
dist_lidx.size
for i in iter(dist_lidx;:5]):
    print i
for i in iter(dist_lidx[:5]):
    print i
for r in iter(dist_lidx):
    print [ri for ri in r if ri]
n = len(dist_lidx)
for r in iter(dist_lidx):
    print [i for i in range(n) if r[i]]
n = len(dist_lidx)
for i,r in enumerate(iter(dist_lidx)):
    print [j for j in range(n) if r[j]]
n = len(dist_lidx)
for i,r in enumerate(iter(dist_lidx)):
    print [j for j in range(n) if r[j] and i!=j]
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += {'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}
d
d[0]
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += [{'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}]
d[0]
d[1]
df = pd.DataFrame(d)
df.head()
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += [{'im_idx':i, 'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}]
df = pd.DataFrame(d)
df.head()
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
# df = df[df['similar_im_idx']
df.head()
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df.head()
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index()
df.head()
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index(drop=True)
df.head()
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index(drop=True)
print "number of rows: %d" % len(df)
df.head()
group_idx = df['similar_im_idx'].iloc[0]
group_idx = df[df['im_idx']==10]['similar_im_idx']
group_idx = df[df['im_idx']==10]['similar_im_idx']
group_idx
group_idx = list(df[df['im_idx']==10]['similar_im_idx'])
group_idx
group_idx = list(df[df['im_idx']==10]['similar_im_idx'])[0]
group_idx
im_idx = 10
group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
group_idx
im_filepaths[0]
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = max([max_n_ims, len(group_idx)])
fig = plt.figure()
for i, idx in enumerate(group_idx[:t]):
    ax=fig.add_subplot(1, 3, i+1)        
    ax.imshow(open_image_idx(idx))
# plt.suptitle('The images')
plt.show()  
group_idx
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = min([max_n_ims, len(group_idx)])
fig = plt.figure()
for i, idx in enumerate(group_idx[:t]):
    ax=fig.add_subplot(1, 3, i+1)        
    ax.imshow(open_image_idx(idx))
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = min([max_n_ims, len(group_idx)])
idx_list = group_idx[:t]
n_idx_list = len(idx_list)

fig = plt.figure()

for i, idx in enumerate(idx_list):
    ax=fig.add_subplot(1, n_idx_list, i+1)        
    ax.imshow(open_image_idx(idx))
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = min([max_n_ims, len(group_idx)])
idx_list = group_idx[:t]
n_idx_list = len(idx_list)

fig = plt.figure()

for i, idx in enumerate(idx_list):
    ax=fig.add_subplot(1, n_idx_list, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = min([max_n_ims, len(group_idx)])
idx_list = group_idx[:t]
n_idx_list = len(idx_list)

fig = plt.figure()

for i, idx in enumerate(idx_list):
    ax=fig.add_subplot(1, n_idx_list, i+1)        
    ax.imshow(open_image_idx(idx))
#     pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = min([max_n_ims, len(group_idx)])
idx_list = group_idx[:t]
n_idx_list = len(idx_list)

fig = plt.figure()

for i, idx in enumerate(idx_list):
    ax=fig.add_subplot(1, n_idx_list, i+1)        
    ax.imshow(open_image_idx(idx))

pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

max_n_ims = 10
t = min([max_n_ims, len(group_idx)])
idx_list = group_idx[:t]
n_idx_list = len(idx_list)

fig = plt.figure()

for i, idx in enumerate(idx_list):
    ax=fig.add_subplot(1, n_idx_list, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# wanna see the images?
fig=plt.figure()
for i, ima in enumerate(img):
    ax=fig.add_subplot(1,3,i+1)        
    ax.imshow(open_image(ima))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()    
4%3
5/2
np.ceil(5/3)
np.ceil(5/3.)
np.ceil(5/3)
np.ceil(5/3.)
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 8
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 12
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 10
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
# set up access to images
# imfacc = sda.get_accessor('slurp_images')
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
im_idx = 10
group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
print group_idx

# set up access to images
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
# see the images of these
im_idx = 0
group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
print group_idx

# set up access to images
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
t = df[df['n_similar_im']==max(df['n_similar_im']))]
t
t = df[df['n_similar_im']==max(df['n_similar_im'])]
t
t = df[df['n_similar_im']==max(df['n_similar_im'])]
print "number of those: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
t = df[df['n_similar_im']==max(df['n_similar_im'])]
print "number of those: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
im_idx
t = df[df['n_similar_im']==max(df['n_similar_im'])]
print "number of those: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
print "idx = %d" % im_idx
thresh = 50
dist_lidx = dist_mat < thresh
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
print "thresh = %0.02f" % thresh
print "num above thresh = %d" % sum(dist_lidx)
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += [{'im_idx':i, 'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}]
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index(drop=True)
print "number of rows: %d" % len(df)
df.head()
t = df[df['n_similar_im']==max(df['n_similar_im'])]
print "number of those: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
print "idx = %d" % im_idx
# see the images of these
# im_idx = 0

group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
print group_idx

# set up access to images
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
max_group_size = max(df['n_similar_im'])
print "max_group_size = %d" % max_group_size
t = df[df['n_similar_im']==max_group_size]
print "number of groups of that size: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
print "idx = %d" % im_idx
thresh = 40
dist_lidx = dist_mat < thresh
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
print "thresh = %0.02f" % thresh
print "num above thresh = %d" % sum(dist_lidx)
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += [{'im_idx':i, 'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}]
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index(drop=True)
print "number of rows: %d" % len(df)
df.head()
max_group_size = max(df['n_similar_im'])
print "max_group_size = %d" % max_group_size
t = df[df['n_similar_im']==max_group_size]
print "number of groups of that size: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
print "idx = %d" % im_idx
# see the images of these
# im_idx = 0

group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
print group_idx

# set up access to images
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
thresh = 45
dist_lidx = dist_mat < thresh
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
print "thresh = %0.02f" % thresh
print "num above thresh = %d" % sum(dist_lidx)
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += [{'im_idx':i, 'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}]
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index(drop=True)
print "number of rows: %d" % len(df)
df.head()
max_group_size = max(df['n_similar_im'])
print "max_group_size = %d" % max_group_size
t = df[df['n_similar_im']==max_group_size]
print "number of groups of that size: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
print "idx = %d" % im_idx
# see the images of these
# im_idx = 0

group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
print group_idx

# set up access to images
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
thresh = 42
dist_lidx = dist_mat < thresh
print "number of pairs: %d" % (len(dist_mat)*(len(dist_mat)-1)/2)
print "thresh = %0.02f" % thresh
print "num above thresh = %d" % sum(dist_lidx)
n = len(dist_lidx)
d = []
for i,r in enumerate(iter(dist_lidx)):
    d += [{'im_idx':i, 'similar_im_idx': [j for j in range(n) if r[j] and i!=j]}]
df = pd.DataFrame(d)
df['n_similar_im'] = df['similar_im_idx'].map(len)
df = df[df['n_similar_im'] > 0]
df = df.reset_index(drop=True)
print "number of rows: %d" % len(df)
df.head()
max_group_size = max(df['n_similar_im'])
print "max_group_size = %d" % max_group_size
t = df[df['n_similar_im']==max_group_size]
print "number of groups of that size: %d" % len(t)
im_idx = t['im_idx'].iloc[0]
print "idx = %d" % im_idx
# see the images of these
# im_idx = 0

group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])[0]
print group_idx

# set up access to images
im_filepaths = sda.facc.load('image_dist_mat_file_names.list')
def open_image_idx(idx):
    return PIL.Image.open(im_filepaths[idx])

# max_n_ims = 10
# t = min([max_n_ims, len(group_idx)])
# idx_list = group_idx[:t]
# n_idx_list = len(idx_list)

fig = plt.figure()

n_disp_cols = 6
n_disp_rows = np.ceil(len(group_idx) / float(n_disp_cols))

for i, idx in enumerate(group_idx):
    ax=fig.add_subplot(n_disp_rows, n_disp_cols, i+1)        
    ax.imshow(open_image_idx(idx))
    pylab.axis('off')
# plt.suptitle('The images')
plt.show()  
group_idx = list(df[df['im_idx']==im_idx]['similar_im_idx'])
for gi in group_idx:
    display_images_of_group_idx(gi)
