import numpy as nb
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # captura frame by frame
    ret, frame = cap.read()

    # Configuracao dos frame podem ser feito aqui
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display result
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
