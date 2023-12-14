# importing packages & modules
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os

# Implementation to generate certificate
df = pd.read_csv('list.csv')
name_font = ImageFont.truetype('GreatVibes-Regular.ttf', 100)
council_font = ImageFont.truetype('Poppins-Bold.ttf', 37)
for index, j in df.iterrows():
    img = Image.open('certificate.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(1000, 850),
              text='{}'.format(j['Name']),
              fill=(0, 0, 0),
              anchor="mm", 
              font=name_font)
    draw.text(xy=(1000, 1030),
              text='{}'.format(j['Council']),
              fill=(29, 66, 83),
              anchor="mm", 
              font=council_font)
    img.save('USS/{}.png'.format(j['Name']))