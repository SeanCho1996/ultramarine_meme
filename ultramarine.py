# %%
import cv2
from PIL import Image, ImageDraw, ImageFont
import argparse
import numpy as np
from matplotlib import pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--image", type=str, default="./Abyssinian_20.jpg")

args = parser.parse_args(args=[])
img_path = args.image

img = Image.open(img_path)
img_arr = np.array(img)

# %%
um = np.zeros_like(img_arr)
um[:, :, 0] = 78
um[:, :, 1] = 114
um[:, :, 2] = 190

add = cv2.addWeighted(img_arr, 0.3, um, 0.7, 0)
# plt.imshow(add)

# %% test text
# img_text = Image.fromarray(add)
# draw = ImageDraw.Draw(img_text)

# textSize = 80
# fontStyle = ImageFont.truetype(
#   "./Heiti.ttc", textSize, encoding="utf-8")

# left = 10
# top = 10
# text = '群青'
# textColor = (255, 255, 255)
# draw.text((left, top), text, textColor, font=fontStyle)
# draw.rectangle(((left, top), (left + 2 * textSize, top + textSize)), fill=None, outline='red', width = 5)
# plt.imshow(img_text)
# %%
shorter_side = min(img.size)
img_gs = cv2.cvtColor(img_arr, cv2.COLOR_RGB2GRAY)
k_size = int(np.ceil(shorter_side / 400) * 6)
img_gs = cv2.blur(img_gs, (k_size, k_size))
grad_x = cv2.Sobel(img_gs, -1, 1, 0, ksize=3)  
grad_y = cv2.Sobel(img_gs, -1, 0, 1, ksize=3)  

border = cv2.addWeighted(grad_x, 0.5, grad_y, 0.5, 0)
# border = cv2.adaptiveThreshold(border, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 301, 0)
_, border = cv2.threshold(border, 0, 255, cv2.THRESH_OTSU)
# plt.imshow(border, cmap='gray')  
# %%
textSize = int(shorter_side / 400 * 60)
rec_length, rec_height = 2 * textSize, textSize + int(textSize / 6)

img_check = img.copy()
draw = ImageDraw.Draw(img_check)
potential_x = []
potential_y = []
for i in range(int(textSize / 2), img.size[0] - rec_length - int(textSize / 2), int(textSize / 2)):
  for j in range(int(textSize / 2), img.size[1] - rec_height - int(textSize / 2), int(textSize / 2)):
    space = border[j : j + rec_height, i :i + rec_length]
    # print(np.max(space))
    if np.max(space) == 0:
      # draw.rectangle(((i, j), (i + rec_length, j + rec_height)), fill=None, outline='red', width = 5)
      potential_y.append(j)
      potential_x.append(i)

# plt.imshow(img_check)
print(potential_x)
print(potential_y)
# %%
img_text = Image.fromarray(add)
draw = ImageDraw.Draw(img_text)

if len(potential_x) == 0:
  left = textSize / 2
  top = textSize / 2

left = potential_x[len(potential_x) // 2]
top = potential_y[len(potential_x) // 2]
fontStyle1 = ImageFont.truetype(
  "./Heiti.ttc", textSize, encoding="utf-8")
fontStyle2 = ImageFont.truetype(
  "./Heiti.ttc", int(textSize * 2 / 7), encoding="utf-8")

textColor = (255, 255, 255)
draw.text((left, top), '群青', textColor, font=fontStyle1)
draw.text((left + int(textSize / 7), top + textSize + int(textSize / 6)), 'YOASOBI', textColor, font=fontStyle2)
# draw.rectangle(((left, top), (left + 2 * textSize, top + textSize)), fill=None, outline='red', width = 5)
plt.imshow(img_text)
img_text.save("./ultramarine.png")



# %%