from PIL import Image
import pytesseract
import numpy as np
import cv2
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
import base64

pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\alkarar\\AppData\\Local\\Tesseract-OCR\\tesseract.exe\\tesseract.exe'


def textRecognizer(imgPath):

    imgorig = np.array(Image.open(imgPath))
    img = cv2.resize(imgorig, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    kernel = np.ones((1, 1), np.uint8)
    img = cv2.dilate(img, kernel, iterations=1)
    img = cv2.erode(img, kernel, iterations=1)
    cv2.threshold(cv2.medianBlur(img, 3), 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    return pytesseract.image_to_string(img)


def fetchImg():
    driver = webdriver.Chrome(executable_path="chromedriver")

    driver.get("https://www.google.com/search?q=computer%20science%20quotes&tbm=isch&hl=en-GB&tbs=rimg:CaJmDVQWudNmYR7JROjHTrBi8AEAsgIMCgIIABAAOgQIABAA&rlz=1C1CHBF_enCA947CA947&sa=X&ved=0CBsQuIIBahcKEwi4tOX3gq_5AhUAAAAAHQAAAAAQDg&biw=1519&bih=688")
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    imgElement =driver.find_element(by=By.XPATH, value='//*[@id="islrg"]/div[1]/div[1]/a[1]/div[1]/img')
    imgSrc = imgElement.get_attribute("src")


    byteData = base64.b64decode(" ".join(imgSrc.split(",")[1:]))

    open("img.jpg", "wb").write(byteData)
    driver.quit()


def isName(text):
    driver = webdriver.Chrome(executable_path="chromedriver")

    driver.get(f"https://www.google.com/search?q={text}&rlz=1C1CHBF_enCA947CA947&oq=sfsf&aqs=chrome..69i57j0i10i512j0i512l2j46i512j0i512j0i10i512j0i512l3.914j0j7&sourceid=chrome&ie=UTF-8")

    try:
        elememt = driver.find_element(by=By.CLASS_NAME, value='SPZz6b')
        return True
        
    except NoSuchElementException:
        return False
        
    finally:
        driver.quit()


def organizeInfo(text):
    textArr = text.split("\n")
    textArr = [x for x in textArr if x]

    infoDict = {}

    for i in range(len(textArr)):
        if isName(textArr[i]):
            infoDict["quote"] = " ".join(textArr[:i])
            infoDict["author"] = "".join([letter for letter in textArr[i] if letter.isalpha() or letter == " "])
            break
    
    return infoDict


