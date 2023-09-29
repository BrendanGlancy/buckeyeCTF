from PIL import Image
import numpy as np


im = np.asarray(Image.open('IMG.png'))
# Make a copy of the image
im2 = im.copy()

im2 = np.asarray(Image.open('IMG.png'))
img = np.fft.fftn(im)
img_hash_original = np.std(img)
print("img_hash_original: ", img_hash_original)

im2[0, 0] = 0
img_alt = np.fft.fftn(im2)
img_hash_alt = np.std(img_alt)
print("img_hash_alt: ", img_hash_alt)

print("img_hash_alt - img_hash_original: ", img_hash_alt - img_hash_original)
if img_hash_alt - img_hash_original < 1 and img_hash_alt - img_hash_original > -1:
    print("success")

# convert img2 from numpy array to image
img2 = Image.fromarray(im2)
img2.save('IMG2.png')


