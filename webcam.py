import cv2

def takePhoto(filename):
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    cv2.imwrite(filename+".jpeg", frame)
    cap.release()
    cv2.destroyAllWindows()
