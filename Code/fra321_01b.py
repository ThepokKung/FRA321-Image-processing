import numpy as np
import cv2 
from matplotlib import pyplot as plt

# img = cv2.imread('1306770.jpeg',0)
img = cv2.imread('1306770.jpeg',1)
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]),plt.yticks([]) #hide tick value on x and y axis
plt.show()