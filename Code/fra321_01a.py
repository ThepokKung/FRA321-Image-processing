import numpy as np
import cv2

img = cv2.imread('1306770.jpeg',cv2.IMREAD_GRAYSCALE)
# img = cv2.imread('1306770.jpeg',cv2.IMREAD_COLOR)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27: #Wait for 'ESC' button to exit
    cv2.destroyAllWindows()
elif k == ord('s'): #Wait for 's' button to save and exit
    cv2.imwrite('Mahiru.png',img)
    cv2.destroyAllWindows()
