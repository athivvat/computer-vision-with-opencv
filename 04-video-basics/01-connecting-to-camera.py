import cv2

cap = cv2.VideoCapture(0)

width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# WINDOWS -- *'DIVX'
# MACOS or LINUX -- *'XVID'

writer = cv2.VideoWriter('mysupervideo.mp4', cv2.VideoWriter_fourcc(*'XVID'), 20, (width, height))

while True:
    ret, frame = cap.read()

    # Operations (Drawing)
    writer.write(frame)

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == 27:
        break

cap.release()
writer.release()
cv2.destroyAllWindows()