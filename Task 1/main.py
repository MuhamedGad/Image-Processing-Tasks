import numpy as np
import cv2 as cv

img = cv.imread('images.jpg',0)
equ = cv.equalizeHist(img)
res = np.hstack((img, equ))
cv.imwrite('NEW.jpg',res)

