import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np

im = Image.new("RGB", (30,30))
pic = np.array(im)
im=pic
for k in range(30):
  for j in range(30):
    if (k-15)*(k-15)+(j-15)*(j-15)<225:
      if (k-15)*(k-15)+(j-15)*(j-15)>190:
        im[k,j] = (255,255,255)


imageio.imsave("rond.png", im)

