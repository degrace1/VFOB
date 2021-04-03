
import cv2
import picamera
from picamera.array import PiRGBArray
import time

class ObjectDet:
    def __init__(self):
        
        ################################################################
        self.path = 'haarcascades/haarcascade 13stg'  # PATH OF THE CASCADE
        #cameraNo = 0                       # CAMERA NUMBER
        self.objectName = 'Bolt'       # OBJECT NAME TO DISPLAY
        self.frameWidth= 640                     # DISPLAY WIDTH
        self.frameHeight = 480                  # DISPLAY HEIGHT
        self.color= (255,0,255)
        self.locations = []
        #################################################################
        
        '''
        cap = cv2.VideoCapture(cameraNo)
        cap.set(3, frameWidth)
        cap.set(4, frameHeight)
        '''

        self.camera = picamera.PiCamera()
        self.camera.resolution = (640,480)
        self.camera.framerate = 32
        self.rawCapture = PiRGBArray(camera, size=(640,480))
        time.sleep(0.1)

    def empty(self):
        pass

    def trackbar(self):
        # CREATE TRACKBAR
        cv2.namedWindow("Result")
        cv2.resizeWindow("Result",self.frameWidth,self.frameHeight+100)
        cv2.createTrackbar("Scale","Result",400,1000,self.empty())
        cv2.createTrackbar("Neig","Result",8,50,self.empty())
        cv2.createTrackbar("Min Area","Result",0,100000,self.empty())
        cv2.createTrackbar("Brightness","Result",180,255,self.empty())
    
    def cascade(self):
        cascade = cv2.CascadeClassifier(self.path)
        return cascade

    def object_bound(self):
        #while True:
        self.trackbar()
        self.locations = []
        for frame in self.camera.capture_continuous(self.rawCapture, format='bgr', use_video_port=True):
            # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
            cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
            #cap.set(10, cameraBrightness)
            
            # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
            #success, img = cap.read()
            img = frame.array
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            
            # DETECT THE OBJECT USING THE CASCADE
            scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
            neig=cv2.getTrackbarPos("Neig", "Result")
            cascade = self.cascade()
            objects = cascade.detectMultiScale(gray,scaleVal, neig)
            # DISPLAY THE DETECTED OBJECTS
            for (x,y,w,h) in objects:
                self.locations.append([x,y,w,h])
                area = w*h
                minArea = cv2.getTrackbarPos("Min Area", "Result")
                if area >minArea:
                    cv2.rectangle(img,(x,y),(x+w,y+h),color,3)
                    cv2.putText(img,objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,color,2)
                    roi_color = img[y:y+h, x:x+w]
        
            cv2.imshow("Result", img)
            
            rawCapture.truncate(0)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        

        cv2.destroyAllWindows()