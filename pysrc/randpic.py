import PIL.Image
import random

# generate random image of x*y pixels
def randpic(x, y):
    img = PIL.Image.new('RGB', (x, y))
    for i in range(x):
        for j in range(y):
            img.putpixel((i, j), (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    return img

def randdims():
    return (random.randint(200, 300), random.randint(200, 300))

# Function taking jpeg path and returning the bmp transformation
def jpg2bmp(jpgpath):
    jpg = PIL.Image.open(jpgpath)
    bmp = PIL.Image.new('RGB', jpg.size)
    for i in range(jpg.size[0]):
        for j in range(jpg.size[1]):
            bmp.putpixel((i, j), jpg.getpixel((i, j)))
    return bmp