#使用gray-world方法實現白平衡
#Gray-World核心概念為:任意一圖像，當它有足夠的色彩變化，則它的RGB分量的均值會趨於相等。
#引入套件
from PIL import Image
import numpy as np
import cv2

#指示欲處理圖片的相對路徑 
image_path=r'./cat inside.jpg'  
original_image=Image.open(image_path)

#將欲處理圖片的資訊儲存成array形式 
image=np.array(original_image)

#分離RGB通道
#依其在三維空間中的數據，依序取出相對應維度的所有數據
R=image[:,:,0] #第一維
G=image[:,:,1] #第二維
B=image[:,:,2] #第三維

#計算三通道的平均值
R_Average=np.mean(R)
G_Average=np.mean(G)
B_Average=np.mean(B)
#計算灰世界偏移因子
K=(R_Average+G_Average+B_Average)/3

#計算三個通道的增益係數 
Gain_R=K/R_Average
Gain_G=K/G_Average
Gain_B=K/B_Average

#根據Von Kries對角模型對於圖像中的每個像素的值，計算其調整後的RGB值 
R_wb=R*Gain_R
G_wb=G*Gain_G
B_wb=B*Gain_B

# 合併調整後的通道
wb_image=np.stack([R_wb,G_wb,B_wb],axis=2)
#將wb_image變數以最大值255~最小值0執行clip
#這麼做的原因為確保計算中有溢值的情況發生
#並存成Unsigned Integer的格式
wb_image=np.clip(wb_image,0,255).astype(np.uint8)

# 將調整後的圖片轉換為PIL Image
wb_image=Image.fromarray(wb_image)
 
#儲存結果圖並顯示 
wb_image.save(r'./cat inside result with Gray-World.jpg')