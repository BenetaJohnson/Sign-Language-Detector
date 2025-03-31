import cv2                        #To access Open-cv
import os                         #To access within OS
import time                       #To give timeouts or delays
import uuid                       #To name image files

Images_path = "Tensorflow/workspace/images/CollectImages"
labels = ["Hello", "Thank You", "Yes", "No", "I Love You"]
Number_Images = 15

os.makedirs(Images_path)
for label in labels:
    os.makedirs(os.path.join(Images_path, label))                  #Create a directory for each label
    capture = cv2.VideoCapture(0)                               #Access the camera - 0 denotes default webcam
    print(f"Collecting images for {label}")                     #Print the label being collected
    time.sleep(5)                                               #Give the camera 5 seconds to warm up
    for imageNum in range(Number_Images):
        ret, frame = capture.read()                             #Read the frame from the camera
        image_Name = os.path.join(Images_path, label, label + "." + f"{str(uuid.uuid1())}.jpg")  #Create a unique path and unique name for the image
        cv2.imwrite(image_Name, frame)                          #Write the image to the directory
        cv2.imshow("Frame", frame)
        time.sleep(2)                                           #Give a 2 second delay between images
        if cv2.waitKey(1) and 0xFF == ord('q'):
            break
    capture.release()                                            #Release the camera