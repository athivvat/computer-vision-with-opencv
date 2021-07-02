import cv2
import time

cap = cv2.VideoCapture('../data/hand_move.mp4')

if cap.isOpened() == False:
    print("ERROR FILE NOT FOUND! OR WONG CODEC USED!")

while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        # WRITER 20 FPS
        time.sleep(1/20)
        cv2.imshow("frame", frame)

        if cv2.waitKey(10) == 27:
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
