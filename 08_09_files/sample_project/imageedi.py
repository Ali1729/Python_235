# import PIL
from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
# from PIL import *
image_path = "plain.jpg"
image = Image.open(image_path)

fnt = ImageFont.truetype("FreeMono.ttf", 100)
I1 = ImageDraw.Draw(image)
I1.text((66,150), "nice Car", fill=(255, 0, 0),font=fnt)
image.save('plain1.jpg')

