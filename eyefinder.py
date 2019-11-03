
import cv2  
  


  
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
  
# camera catch
img = cv2.imread('input.jpg') 

scale_factor = .2
width = int(img.shape[1] * scale_factor)
height = int(img.shape[0] * scale_factor)
dim = (width, height)
img = cv2.resize(img, dim)


ret = img 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
faces = face_cascade.detectMultiScale(gray, 1.3, 5) 

for (x,y,w,h) in faces: 
        
    #cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,255),2)  
    roi_gray = gray[y:y+h, x:x+w] 
    roi_color = img[y:y+h, x:x+w] 

    eyes = eye_cascade.detectMultiScale(roi_gray)  

    for (ex,ey,ew,eh) in eyes: 
        #cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(2,2,255),5) 
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 16, (255,0,0))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 13, (255,0,0))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 11, (255,0,0))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 9, (255,60,40))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 8, (255,140,140))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 7, (255,180,180))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 6, (255,200,200))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 5, (255,255,255))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 4, (255,255,255))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 3, (255,255,255))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 2, (255,255,255))
        cv2.circle(roi_color, ((int)(ex + ew/2),(int)(ey + eh/2)), 1, (255,255,255))



cv2.imwrite('tmp.jpg', img)

  

cv2.destroyAllWindows()  