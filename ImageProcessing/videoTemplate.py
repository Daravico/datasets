import cv2 

cap = cv2.VideoCapture(0)

w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = w // 2
y = h // 2

while True:
    ret, frame = cap.read()

    cv2.imshow("VideoCapture", frame)

    # No more frames captured. Exiting.
    if not ret:
        break

    k = cv2.waitKey(1)

    if k == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()