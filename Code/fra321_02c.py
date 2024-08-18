import cv2

img1 = cv2.imread('1306770.jpeg')
dsize = (int(img1.shape[1]/2)),int(img1.shape[0]/2)
img1 = cv2.resize(img1,dsize)
e1 = cv2.getTickCount()
#your code here
for i in range(5,11,2):
    img1 = cv2.medianBlur(img1,i)
    cv2.imshow('result'+str(i),img1)
e2 = cv2.getTickCount()
t = (e2-e1)/cv2.getTickFrequency()
print(t)

cv2.waitKey(0)
cv2.destroyWindow()