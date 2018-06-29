import os
import numpy as np
from PIL import Image
import scipy.misc

nchannels=3

for root, dirs, files in os.walk('.'):
	for d in dirs[:]:
		for i in os.listdir(d):

        		pathabs=os.path.abspath(d+"/"+i) 
			img = np.asarray(Image.open(pathabs))
                        x=img.shape
                        xlen=len(x)
                        if (xlen==3):
				height, width, channels = img.shape
			if (xlen==2):
				height, width = img.shape
			if channels==1: 

				new_img = np.stack((img,)*nchannels, -1)
				scipy.misc.imsave(pathabs, new_img)
