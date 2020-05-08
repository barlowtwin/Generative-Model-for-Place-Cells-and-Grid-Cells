#!/usr/bin/env python
# coding: utf-8

# In[5]:


import random
import cv2
import numpy as np
import scipy.misc
import matplotlib.pyplot as plt
import matplotlib


# In[6]:


# RGB color - R,G,B

# yellow - 255,255,0
# green  - 0,128,0
# blue   - 0,0,255
# red    - 255,0,0  

yellow = [255,255,0] # 0
green = [0,128,0]    # 1
blue = [0,0,255]     # 2
red = [255,0,0]      # 3



# In[7]:


for n in range(1000) : # 10000 number of images to generated
    
    arr = np.zeros((32,32,3)) # space for an image 
    
    for i in range(32):
        for j in range(32):
            
            random_pixel = random.randint(0,3)
            
            if random_pixel == 0 : # yellow
                
                arr[i][j][2] = 255
                arr[i][j][1] = 255
                arr[i][j][0] = 0
                
            if random_pixel == 1 : # green
                
                arr[i][j][2] = 0
                arr[i][j][1] = 128
                arr[i][j][0] = 0 
                
            if random_pixel == 2 : # blue
                
                arr[i][j][2] = 0
                arr[i][j][1] = 0
                arr[i][j][0] = 255
                
            if random_pixel == 3 : #red
                
                arr[i][j][2] = 255
                arr[i][j][1] = 0
                arr[i][j][0] = 0
                
    arr = arr/255 # neceassary for usinig saving using matplotlib 
            
    matplotlib.image.imsave(str(n)+'.png', arr)
            
                
                


# In[ ]:




