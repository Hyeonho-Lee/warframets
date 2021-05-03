import os
import re
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from pytesseract import *

def make_image():
    
    pytesseract.tesseract_cmd = r'/usr/bin/tesseract'
    config = '--tessdata-dir "/usr/share/tesseract-ocr/4.00/tessdata" -l kor+eng --psm 1 -c preserve_interword_spaces=1 --oem 3'
    
    img = cv2.imread('./test4.jpg', cv2.IMREAD_COLOR)
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img3 = cv2.medianBlur(img2, 1)
    result = cv2.threshold(img3, 209, 255, cv2.THRESH_BINARY)[1]

    height, width = result.shape
    roi_0 = result[0+100:int(height/4), 0:width]
    roi_1 = result[1*int(height/4)+100:(1+1)*int(height/4), 0:width]
    roi_2 = result[2*int(height/4)+100:(2+1)*int(height/4), 0:width]
    roi_3 = result[3*int(height/4)+100:(3+1)*int(height/4), 0:width]
    result = np.vstack((roi_0, roi_1, roi_2, roi_3))

    kernel = np.ones((2,2), np.uint8)
    result = cv2.dilate(result, kernel, iterations=1)

    result_1 = result.copy()
    result_1 = 255 - result_1

    cv2.imwrite('./test_result.jpg', result_1)
    
    text = pytesseract.image_to_string(result_1, config=config)
    with open('./result_text.txt', 'w') as file:
        file.write(str(text))

make_image()