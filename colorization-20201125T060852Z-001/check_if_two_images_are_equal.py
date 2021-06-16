import cv2
import numpy as np
import matplotlib.pyplot as plt


original = cv2.imread("13.png")
eccv16 = cv2.imread("eccv16_denoised13.png")
siggraph17 = cv2.imread("siggraph17_denoised13.png")

Y1 = np.square(np.subtract(original,eccv16)).mean() # tính MSE
print("MSE:", Y1)		
Y2 = np.square(np.subtract(original,siggraph17)).mean() # tính MSE
print("MSE:", Y2)

plt.figure(figsize=(12,8))
plt.subplot(2,2,1)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(2,2,2)
plt.imshow(cv2.cvtColor(eccv16, cv2.COLOR_BGR2RGB))
plt.title('MSE = ' + str(Y1) + ' ECCV16')
plt.axis('off')

plt.subplot(2,2,3)
plt.imshow(cv2.cvtColor(original, cv2.COLOR_BGR2RGB))
plt.title('Original')
plt.axis('off')

plt.subplot(2,2,4)
plt.imshow(cv2.cvtColor(siggraph17, cv2.COLOR_BGR2RGB))
plt.title('MSE = ' + str(Y2) + ' SIGGRAPH17')
plt.axis('off')

plt.show()