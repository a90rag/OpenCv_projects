# if pip not install then type first (curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py) 
# that download script file in system, 
# then get pip.py script
# pip install opencv python if open cv not installed
# python.exe -m pip install --upgrade pip (to upgrade pip).
# to install opencv (pip install opencv-python)

import cv2  # cv2 is module name and opencv is library
from matplotlib import pyplot as plt
import numpy as np
#generate 100 data points along 3 dimansions

x,y,scale = np.random.randn(3,100)
fig,ax=plt.subplots()

#Map each onto a scatterplot we'll create with Matplotlib

ax.scatter(x=x,y=y,c=scale,s=np.abs(scale)*500)
ax.set(title="Some random data, created with with techlab!")
plt.show()