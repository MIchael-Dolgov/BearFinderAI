import cv2
import numpy as np
from matplotlib import pyplot as plt

#примеры 2х картинок на которых всё работает хорошо
#img = cv2.imread("TEST IMAGES/withBears/_2016-04-25 13-50-46_1257_R.JPG")
#img = cv2.imread("TEST IMAGES/withBears/2016-05-13 11-33-21_0855_2R.JPG")

def anotatePhoto(image: str, filename: str):
    img = cv2.imread(image)

    #-----Converting image to LAB Color model-----------------------------------
    lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

    #-----Splitting the LAB image to different channels-------------------------
    l, a, b = cv2.split(lab)

    #-----Applying CLAHE to L-channel-------------------------------------------
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    cl = clahe.apply(l)

    #-----Merge the CLAHE enhanced L-channel with the a and b channel-----------
    limg = cv2.merge((cl,a,b))

    #-----Converting image from LAB Color model to RGB model--------------------
    final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)

    #---------------Converting to RGB--------------------
    img_RGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    img_hsv = cv2.cvtColor(img_RGB, cv2.COLOR_RGB2HSV)

    light_orange = (44, 10, 20)
    dark_orange = (60, 20, 80)

    mask = cv2.inRange(img_hsv, light_orange, dark_orange)

    position = np.unravel_index(np.argmax(mask), mask.shape)

    #выризаеим картинку чтобы посмотреть
    y=position[0]-100
    x=position[1]-100
    h=200
    w=200
    # выделяем медведя на общей картинке
    cv2.rectangle(img_RGB, (x,y), (x+w,y+h), (0, 255, 255), 20)
    cv2.imwrite(filename, img_RGB)