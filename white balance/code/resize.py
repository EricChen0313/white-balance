import cv2 
import numpy as np

# 讀取圖片
img = cv2.imread('cat inside.jpg')

# 修改大小
img = cv2.resize(img, (1280, 720))  
# 長方形 1920*1080、1280*720

# 儲存圖片
cv2.imwrite('resized cat inside.jpg', img)