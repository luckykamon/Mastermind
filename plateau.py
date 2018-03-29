import imageio
import matplotlib.pyplot as plt
import Image
import numpy as np

im = Image.new("RGB", (295,650))
pic = np.array(im)
im=pic
c=[70,625] #coordonne du cendre du grand rond en bas a gauche
for l in range(13):
  for k in range(650):
    for j in range(295):
      if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0])*(j-c[0])<225:
        if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0])*(j-c[0])>190:
          im[k,j] = (255,255,255)
      if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-50)*(j-c[0]-50)<225:
        if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-50)*(j-c[0]-50)>190:
          im[k,j] = (255,255,255)
      if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-100)*(j-c[0]-100)<225:
        if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-100)*(j-c[0]-100)>190:
          im[k,j] = (255,255,255)
      if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-150)*(j-c[0]-150)<225:
        if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-150)*(j-c[0]-150)>190:
          im[k,j] = (255,255,255)

c=[15,635] #coordonne du cendre du petit rond en bas a gauche
for l in range(12):
  for k in range(650):
    for j in range(295):
      if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0])*(j-c[0])<25:
        if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0])*(j-c[0])>10:
          im[k,j] = (255,255,255)
      if (k-c[1]+50*l+15)*(k-c[1]+50*l+15)+(j-c[0])*(j-c[0])<25:
        if (k-c[1]+50*l+15)*(k-c[1]+50*l+15)+(j-c[0])*(j-c[0])>10:
          im[k,j] = (255,255,255)
      if (k-c[1]+50*l+15)*(k-c[1]+50*l+15)+(j-c[0]-15)*(j-c[0]-15)<25:
        if (k-c[1]+50*l+15)*(k-c[1]+50*l+15)+(j-c[0]-15)*(j-c[0]-15)>10:
          im[k,j] = (255,255,255)
      if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-15)*(j-c[0]-15)<25:
        if (k-c[1]+50*l)*(k-c[1]+50*l)+(j-c[0]-15)*(j-c[0]-15)>10:
          im[k,j] = (255,255,255)


imageio.imsave("plateau.png", im)

