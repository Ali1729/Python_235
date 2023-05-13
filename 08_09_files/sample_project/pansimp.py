import pandas as pd
# from PIL import Image
# from PIL import ImageDraw
# from PIL import ImageFont
from PIL import *
from PIL import Image


image_path = "recpt.jpg"

# fnt = ImageFont.truetype("FreeMono.ttf", 40)



df = pd.read_excel('ADMNREGISTER_dummy.xlsx',skiprows=5)
for index,row in df.iterrows():
    # image = Image.open(image_path)
    # I1 = ImageDraw.Draw(image)
    # I1.text((228,322),str(row["ADMN"]), fill=(255, 0, 0),font=fnt)
    # new_file= str(row["ADMN"])+".jpg"
    # image.save(new_file)
    print(type(row))