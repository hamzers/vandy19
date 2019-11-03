from PIL import ImageFilter, Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import scipy.misc

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

#im1.save("done.jpg")

#plt.imsave('output.png', im1)

