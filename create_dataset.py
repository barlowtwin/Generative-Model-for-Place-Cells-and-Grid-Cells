#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import random
import matplotlib.pyplot as plt
import matplotlib


# In[2]:


# green [0,128,0] 
# yellow [255,255,0] 



# 5 different patterns of size 2*2 are placed randomly in a 8*8 image
# 2 different types of pixel are used

# pattern 1 = [[0,0],[0,0]]
# pattern 2 = [[0,1],[0,0]]
# pattern 3 = [[1,0],[0,1]]
# pattern 4 = [[0,0],[0,1]]
# pattern 5 = [[1,1],[1,1]]

# 0 means green, 1 means yellow

n = 2000 # to generate 1000 images

for k in range(n):
    
    img_array = np.zeros((8,8,3))
    
    #generating a random number between 1 and 5
    
    
    for i in range(4): # rows/2 because we have a patch of size 2*2
        for j in range(4): # columns/2
            
            pattern = random.randint(1,5)
            
            
            
            if pattern == 1 :
            
                img_array[2*i][2*j][2] = 0
                img_array[2*i][2*j][1] = 128
                img_array[2*i][2*j][0] = 0
                
                img_array[2*i][2*j+1][2] = 0
                img_array[2*i][2*j+1][1] = 128
                img_array[2*i][2*j+1][0] = 0
                
                img_array[2*i+1][2*j][2] = 0
                img_array[2*i+1][2*j][1] = 128
                img_array[2*i+1][2*j][0] = 0
                
                img_array[2*i+1][2*j+1][2] = 0
                img_array[2*i+1][2*j+1][1] = 128
                img_array[2*i+1][2*j+1][0] = 0
                
            if pattern == 2 :
                
                img_array[2*i][2*j][2] = 0
                img_array[2*i][2*j][1] = 128
                img_array[2*i][2*j][0] = 0
                
                img_array[2*i][2*j+1][2] = 0
                img_array[2*i][2*j+1][1] = 255
                img_array[2*i][2*j+1][0] = 255
                
                img_array[2*i+1][2*j][2] = 0
                img_array[2*i+1][2*j][1] = 128
                img_array[2*i+1][2*j][0] = 0
                
                img_array[2*i+1][2*j+1][2] = 0
                img_array[2*i+1][2*j+1][1] = 128
                img_array[2*i+1][2*j+1][0] = 0
                
            if pattern == 3 :
                
                img_array[2*i][2*j][2] = 0
                img_array[2*i][2*j][1] = 255
                img_array[2*i][2*j][0] = 255
                
                img_array[2*i][2*j+1][2] = 0
                img_array[2*i][2*j+1][1] = 128
                img_array[2*i][2*j+1][0] = 0
                
                img_array[2*i+1][2*j][2] = 0
                img_array[2*i+1][2*j][1] = 128
                img_array[2*i+1][2*j][0] = 0
                
                img_array[2*i+1][2*j+1][2] = 0
                img_array[2*i+1][2*j+1][1] = 255
                img_array[2*i+1][2*j+1][0] = 255
                
            if pattern == 4:
                
                img_array[2*i][2*j][2] = 0
                img_array[2*i][2*j][1] = 128
                img_array[2*i][2*j][0] = 0
                
                img_array[2*i][2*j+1][2] = 0
                img_array[2*i][2*j+1][1] = 128
                img_array[2*i][2*j+1][0] = 0
                
                img_array[2*i+1][2*j][2] = 0
                img_array[2*i+1][2*j][1] = 128
                img_array[2*i+1][2*j][0] = 0
                
                img_array[2*i+1][2*j+1][2] = 0
                img_array[2*i+1][2*j+1][1] = 255
                img_array[2*i+1][2*j+1][0] = 255
                
            if pattern == 5 :
            
                img_array[2*i][2*j][2] = 0
                img_array[2*i][2*j][1] = 255
                img_array[2*i][2*j][0] = 255
                
                img_array[2*i][2*j+1][2] = 0
                img_array[2*i][2*j+1][1] = 255
                img_array[2*i][2*j+1][0] = 255
                
                img_array[2*i+1][2*j][2] = 0
                img_array[2*i+1][2*j][1] = 255
                img_array[2*i+1][2*j][0] = 255
                
                img_array[2*i+1][2*j+1][2] = 0
                img_array[2*i+1][2*j+1][1] = 255
                img_array[2*i+1][2*j+1][0] = 255
                
    img_array = img_array/255
    matplotlib.image.imsave(str(k)+'.png', img_array)

