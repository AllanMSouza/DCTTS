# -*- coding: utf-8 -*-
#/usr/bin/python2
'''
By kyubyong park. kbpark.linguist@gmail.com.
https://www.github.com/kyubyong/dc_tts
'''

from __future__ import print_function

from utils import load_spectrograms
import os
from data_load import load_data
import numpy as np
import tqdm
from optparse import OptionParser

# Load data
parser = OptionParser()
parser.add_option('-d', '--dataset',  dest='dataset_path',  metavar='STRING')

(opt, args) = parser.parse_args()

fpaths, _, _ = load_data(opt.dataset_path) # list

for fpath in tqdm.tqdm(fpaths):
    fname, mel, mag = load_spectrograms(fpath)
    if not os.path.exists(f"{opt.dataset_path}/mels"): os.mkdir("mels")
    if not os.path.exists(f"{opt.dataset_path}/mags"): os.mkdir("mags")

    np.save("{}/mels/{}".format(opt.dataset_path, fname.replace("wav", "npy")), mel)
    np.save("{}/mags/{}".format(opt.dataset_path, fname.replace("wav", "npy")), mag)