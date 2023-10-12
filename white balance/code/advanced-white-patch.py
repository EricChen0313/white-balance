#程式碼主要通過計算每個通道的直方圖，找到合適的亮度閾值，
#並根據閾值進行亮度調整，實現了一個簡單的白平衡過程。

#引入函示庫
from PIL import Image
import numpy as np
import cv2

#指定輸入圖片的路徑
input_image_path = r'./cat inside.jpg'
image = cv2.imread('cat inside.jpg')

#計算白平衡的閥值，這個閥值設定為圖片總像素的1%
top = image.shape[0]*image.shape[1]*0.01

#分離RGB通道 
B,G,R = cv2.split(image)

#初始化每個通道的最大像素值列表
RGB_Max = [0,0,0]

#計算每個通道的最大像素值
#對每個通道，計算其直方圖，然後選擇一個亮度閾值，使得在這個閾值之上的像素數量占總像素數量的1%。
#這樣可以得到每個通道的最大亮度值，將其存儲在 rgbmax 列表中。
for i in range(image.shape[-1]):
    sum = 0 #初始化一個變數用於累計直方圖的像素值總和
    l = 256 #初始化一個變數，表示直方圖的亮度級別。從最亮的開始
    #計算該通道的直方圖
    hist,_ = np.histogram(cv2.split(image)[i].flatten(),256,[0,256]) 
    while sum<top:
        l = l-1 #逐步降低亮度級別
        sum = sum+hist[l] #累加直方圖在當前亮度級別的像素值
    RGB_Max[i] = l #將計算得到的最大亮度級別存到列表中

#正規化每個通道的像素值，並將像素值縮放到0-255的範圍內。
B = (B/RGB_Max[0]*255).clip(0,255)
G = (G/RGB_Max[1]*255).clip(0,255)
R = (R/RGB_Max[2]*255).clip(0,255)

#合併通道，轉換為8-bit unsigned integer，並形成新的彩色圖像。 
image = cv2.merge([B,G,R]).astype(np.uint8)

#顯示圖片並儲存結果圖
cv2.imshow('Original Image', cv2.imread(input_image_path))
cv2.imshow('advanced_white_patch',image)
cv2.imwrite('cat inside result with advanced-White-Patch.jpg',image)
cv2.waitKey(0)