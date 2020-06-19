# -*- Mode: Python; tab-width: 8; python-indent-offset: 4 -*-
# vim:set et sts=4 ts=4 tw=80:
# This Source Code Form is subject to the terms of the MIT License.
# If a copy of the ML was not distributed with this
# file, You can obtain one at https://opensource.org/licenses/MIT

# author: JackRed <jackred@tuta.io>

from sklearn.cluster import KMeans
from skimage import io, transform
#from matplotlib import pyplot as plt
import sys
# import numpy as np

# The number of color to extract from the image
NB_COLORS = 5

# check an argument is given
if len(sys.argv) != 2:
    exit("need 1 argument: main.py path/to/image.jpg")

# read the argument
image_path = sys.argv[1]
# load the images
im = io.imread(image_path)

# im = io.imread("./example/wall2.png")
img = transform.resize(im, (im.shape[0] // 4, im.shape[1] // 4, im.shape[2]))

# 2d > 1d array
shape = img.shape
ar = img.reshape((-1, shape[2]))

# kmeans clustering
kmeans1 = KMeans(n_clusters=NB_COLORS).fit(ar)

print("\n".join(([" ".join([str(j) for j in i])
                  for i in kmeans1.cluster_centers_*256])))

# displaying image for debug
#color1 = kmeans1.cluster_centers_.reshape((1, NB_COLORS, im.shape[2]))

# fig, ax = plt.subplots(nrows=2)

# ax[0].imshow(img)
# ax[1].imshow(color1)

# plt.show()
