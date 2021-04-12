
import cv2
import imutils
from imutils.video import VideoStream

class objectdet:
    def __init__(self, vs = None):
        ################################################################
        self.path = 'haarcascades/cascade.xml'  # PATH OF THE CASCADE
        #self.cameraNo = 0                       # CAMERA NUMBER
        self.objectName = 'Bolt'       # OBJECT NAME TO DISPLAY
        self.frameWidth= 640                     # DISPLAY WIDTH
        self.frameHeight = 480                  # DISPLAY HEIGHT
        self.color= (255,0,255)
        #################################################################

        if vs == None:
            self.vs = VideoStream(src=0).start()
        else:
            self.vs = vs
        self.frame = None
        
    def empty(self,a):
        pass

    def trackbar(self):
        # CREATE TRACKBAR
        cv2.namedWindow("Result")
        cv2.resizeWindow("Result",self.frameWidth,self.frameHeight+100)
        cv2.createTrackbar("Scale","Result",80,1000,self.empty)
        cv2.createTrackbar("Neig","Result",16,50,self.empty)
        cv2.createTrackbar("Min Area","Result",0,100000,self.empty)
        cv2.createTrackbar("Brightness","Result",180,255,self.empty)
 
    def cascade(self):
        # LOAD THE CLASSIFIERS DOWNLOADED
        cascade = cv2.CascadeClassifier(self.path)
        return cascade
 
    def locate(self):
            #while True:
        self.trackbar()
        locations = []
        for _ in range(2):
            # SET CAMERA BRIGHTNESS FROM TRACKBAR VALUE
            #cameraBrightness = cv2.getTrackbarPos("Brightness", "Result")
            #cap.set(10, cameraBrightness)
            # GET CAMERA IMAGE AND CONVERT TO GRAYSCALE
            #success, img = cap.read()
            self.frame = self.vs.read()
            if self.frame is None:
                print("No frame taken")
                return locations
            img = self.frame
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # DETECT THE OBJECT USING THE CASCADE
            scaleVal =1 + (cv2.getTrackbarPos("Scale", "Result") /1000)
            neig=cv2.getTrackbarPos("Neig", "Result")
            cascade = self.cascade()
            objects = cascade.detectMultiScale(gray,scaleVal, neig)
            # DISPLAY THE DETECTED OBJECTS
            for (x,y,w,h) in objects:
                locations.append([x,y,w,h])
                area = w*h
                minArea = cv2.getTrackbarPos("Min Area", "Result")
                if area >minArea:
                    cv2.rectangle(img,(x,y),(x+w,y+h),self.color,3)
                    cv2.putText(img,self.objectName,(x,y-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,self.color,2)
                    roi_color = img[y:y+h, x:x+w]
            #cv2.imshow("Result", img)
                
            #self.rawCapture.truncate(0)
                
        return locations

    def profit(self):
        bolt_coords = self.locate()
        if bolt_coords != []:
            print("Number of bolts: ", len(bolt_coords))
            print("x:",bolt_coords[0][0],"  y:",bolt_coords[0][1])
            print("bolt width:",bolt_coords[0][2],"  bolt height:",bolt_coords[0][3])
            self.endAll()
            return bolt_coords[0]
        else:
            print("No bolt located")
            return "empty"
            
    #close the camera and all windows
    def endAll(self):
        self.vs.stop()
        cv2.destroyAllWindows() 
