import cv2
import numpy as np
import os
from IPython.display import clear_output
from time import sleep
import matplotlib.pyplot as plt


def clear():
    _ = os.system('cls')

folder = "\ground_truth"

for i, img in enumerate(folder):
    if(i==10):
        break
    img = cv2.imread('ground_truth/' + '00' + str(i) + '.png')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours, _ = cv2.findContours(gray, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    cnt_img = cv2.drawContours(img, contours, -1, (255,0,0),3)
    for j in range(len(contours)):
        contour = contours[j]
        area = cv2.contourArea(contour)
        length = cv2.arcLength(contour, True)
        print( "{0}.\tkép".format(i+1),"{0}. eszköz területe:\t".format(j+1), round(area,1),"pixel" , "\tátmérője: " , round(np.sqrt(4*area /np.pi),1),"pixel" , "\tkerülete: " , round(length,1),"pixel")
    cv2.imshow("",img)
    cv2.waitKey()
