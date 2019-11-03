import cv2  
from PIL import ImageFilter, Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.misc


def eyefinder(filename):
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
    eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')  
    
    # camera catch
    img = cv2.imread(filename)

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
    #return img

def boost():
    img = Image.open('tmp.jpg')
    im1 = img.filter(ImageFilter.BLUR)
    for x in range(0, 10):
       im1 = im1.filter(ImageFilter.BLUR)
        
    width, height = im1.size
    for x in range(width):
        for y in range(height):
            r,g,b = im1.getpixel((x,y))
            if r > 150:
                value = (255, g, b)
                im1.putpixel((x,y), value)
            else:
                value = (r + 105, g, b)
                im1.putpixel((x,y), value)



    plt.imshow(im1)
    im1 = np.asarray(im1)
    print(im1.shape)

    scipy.misc.imsave('outfile.jpg', im1)
