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
