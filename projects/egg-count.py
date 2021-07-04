import time
import cv2
import numpy as np

def contours_img(frame):
    contours, hieracy = cv2.findContours(frame, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)
    return contours, hieracy

cap = cv2.VideoCapture('../data/eggs.mp4')

if not cap.isOpened():
    print("ERROR FILE NOT FOUND! OR WONG CODEC USED!")

while True:
    ret, frame = cap.read()

    # Blurring
    blurring_img = cv2.GaussianBlur(frame, (7, 7), 0)

    # Sobel
    canny = cv2.Canny(blurring_img, threshold1=127, threshold2=127)

    # Threshold
    # gray_img = cv2.cvtColor(canny, cv2.COLOR_BGR2GRAY)
    # ret, threshold = cv2.threshold(canny, 175, 255, cv2.THRESH_BINARY_INV)

    # Erod
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (7, 7))
    # erod_img = cv2.erode(frame, kernel, iterations=10)

    # Dilate
    dilate_img = cv2.dilate(canny, kernel, iterations=1)

    # Contours
    contours, hieracy = contours_img(dilate_img)
    frame_contours = np.zeros(frame.shape)
    for i in range(len(contours)):
        cv2.drawContours(frame_contours, contours, i, 255, -1)

    time.sleep(1 / 10)
    cv2.imshow("EGG COUNT", dilate_img)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
if cap.isOpened():
    cap.release()