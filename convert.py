#from heic2png import HEIC2PNG
import os

path = "."
for root, d_names, f_names in os.walk(path):
   print(root, d_names, f_names)

#png = HEIC2PNG("IMG_2160.HEIC")
#png.save()
#print(png)