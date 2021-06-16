import cv2
import os
import glob

cv_img = []
i = 0
for img in glob.glob("Gray_Change/*.jpg"):
    n = cv2.imread(img)
    namefile = img[12:]
    namefileout = str(i) + '.png'
    grayImage = cv2.cvtColor(n, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("Image_After/"+namefileout, grayImage) # xuất file
    i = i + 1
    print(i)
    cv_img.append(n)



# namefile = cv_img[0]
# namefileout = namefile.split('.')[0] + '.jpg'

# originalImage = cv2.imread(namefile)
# grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
  
# (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)
 

# cv2.imshow('Gray image', grayImage)
# cv2.imwrite("gray_image_"+namefileout, grayImage)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
