from PIL import ImageFilter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = Image.open(r"C:\Users\ryanb\OneDrive\IdeaProjects\Image Editing\Hack.jpg")
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



imgplot = plt.imshow(im1)
