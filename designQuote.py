import cv2
import numpy as np
from PIL import ImageColor



def designQuotePost(data):

    img = np.ones((540, 540, 3), np.uint8)
    img.fill(255)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    pt1 = (0, 0)
    pt2 = (0, 540)
    pt3 = (540, 540)


    triangle1 = np.array([(0, 0), (0, 540), (540, 540)])
    triangle2 = np.array([(540, 0), (540, 540), (0, 0)])


    cv2.drawContours(img, [triangle1], 0, (195, 164, 7), -1)
    cv2.drawContours(img, [triangle2], 0, (9, 29, 68), -1)

    cv2.circle(img, (270, 270), 220,(255, 255, 255), -1)


    start = 0

    wordArr = data["quote"].split(" ")
    line = 0

    for i in range(len(wordArr)):


        if len(" ".join((wordArr[start:i+1]))) > 32 or i == len(wordArr)-1:

            cv2.putText(img, " ".join(wordArr[start:i+1]), (100, 250 + (30*line)), fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.6, color=(0, 0, 0))
            line+=1
            start=i+1


    cv2.putText(img, "-" + data["author"], (220, 250 + (30*line)), fontFace= cv2.FONT_HERSHEY_SIMPLEX,fontScale=0.4, color=(195, 164, 7))


    cv2.imwrite("quotePost.jpg", img)


