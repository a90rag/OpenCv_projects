import cv2
#import pdb #python debugger pdb.set_trace
video_cap = cv2.VideoCapture(0)
while True :
    
    ret, video_data = video_cap.read()
    # when read mathod called mathos on 'videocapture object, it attempts to read the next frame from video source.
    #the mathos returns 2 value
    # 1: 'ret' - this is boolean variable that indicates frame was read successfully.
    # 2: frame - the variable contain actual frame data if 'ret' is 'true'. It could be a NumPy array representing the image.
    cv2.imshow("video_live",video_data) #make a frame using the code, cv2.imshow
    if cv2.waitKey(10) == ord("a"): #to stop video press 'a' , waitKey use to pause image for particule time.
        break
video_cap.release()#after succesfully run we will receive vedio live.
    
    