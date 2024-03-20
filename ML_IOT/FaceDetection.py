import cv2

face_cap = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
video_cap = cv2.VideoCapture(0)
while True:
    ret, video_data = video_cap.read()
    col = cv2.cvtColor(video_data,cv2.COLOR_BGR2GRAY)
    faces = face_cap.detectMultiScale(
        col,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30,30),
       # flags=cv2.CASCAD_SCALE_IMAGE
    )
    
    for (x,y,w,h) in faces:
        cv2.imshow("video_live",video_data)
        
        if cv2.waitKey(10) == ord('a'):
            break
video_cap.release()


#Finally, the processed image with rectangles drawn around the detected faces is displayed. The cv2.waitKey(0) function waits for a key event (0 means indefinitely), and cv2.
# destroyAllWindows() closes all OpenCV windows when a key is pressed.