import numpy as np
import time, os, sys
from urllib.parse import urlparse
import matplotlib.pyplot as plt
import matplotlib as mpl
#%matplotlib inline
mpl.rcParams['figure.dpi'] = 300
from cellpose import  models,utils, io

# READ FILENAME
# REPLACE FILES WITH YOUR IMAGE PATHS
# WRITE EXTENSION NAME
files = []
count = 0
path = "/cellpose/cellpose_test"
for filename in os.listdir(path):
    if(filename.endswith(".tif") == True):
        files.append(filename)
        count = count + 1

# DEFINE CELLPOSE MODEL
# model_type='cyto' or model_type='nuclei'
model = models.Cellpose(gpu=False, model_type='nuclei')

# for the same channels 
channels = []
for i in range(1,count+1):
    channels.append([0,0])
print(channels)
    
# run in a loop
for chan, filename in zip(channels, files):
    img = io.imread(path +"/"+filename)
    masks, flows, styles, diams = model.eval(img, diameter=None, channels=chan)

    # save results so you can load in gui
    io.masks_flows_to_seg(img, masks, flows, diams, filename, chan)

    # save results as png
    io.save_to_png(img, masks, flows, filename)