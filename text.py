import cv2 
import numpy as np
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img = cv2.imread("image.png")
img = cv2.resize(img,None, fx = 0.9, fy = 0.8)
gray = cv2.cvtColor(img,cv2.COLOR_BGRA2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255,
	cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 21, 10)
text = pytesseract.image_to_string(thresh)
print(text)
cv2.imshow("threshold",thresh)
cv2.waitKey(0)

