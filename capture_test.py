import numpy as np
import cv2

cap = cv2.VideoCapture(0)
i = 0
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    cv2.imwrite(f"{i}.png", frame)
    ret, frame_bytes = cv2.imencode(".png", frame)
    print(type(frame_bytes))
    i += 1
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
    break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
