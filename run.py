#!/usr/bin/env python
import numpy as np
import cv2
import matplotlib.pyplot as pyplot
from matplotlib.colors import LogNorm
import argparse
import os
import sys

import matplotlib.image as mpimg

parser = argparse.ArgumentParser(description='Tool to calculate the NDVI index.')
parser.add_argument('inputImg', type=str, help='Path of the input image for calculation of NDVI index.')
parser.add_argument('cmap', type=str, help='Color map to apply to the output file. Compatible with matplotlib colormaps.')
parser.add_argument('output', type=str, help='Path for the image with the NDVI index.')

args = parser.parse_args()
pathInput = args.inputImg
colorMap = args.cmap
pathOutput = args.output


def calculateNDVI():

    existFile = os.path.exists(pathInput)

    if(existFile):

        image = cv2.imread(pathInput, cv2.IMREAD_COLOR)

        # Split the RGB image in their channels
        b, g, r = cv2.split(image)

        bottom = (r.astype(float) + b.astype(float))

        bottom[bottom == 0] = 0.01  # Make sure we don't divide by zero!

        ndvi = (r.astype(float) - b) / bottom

        pyplot.imsave(pathOutput, ndvi, vmin=-1., vmax=1., cmap=colorMap)
    else:
        # Error: File does not exist.
        sys.exit(20)


calculateNDVI()