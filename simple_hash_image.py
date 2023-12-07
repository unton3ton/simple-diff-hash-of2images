# https://stackoverflow.com/questions/10075065/compute-hash-of-only-the-core-image-data-excluding-metadata-for-an-image

from PIL import Image

import hashlib

img1 = Image.open('catodog85percent.jpg').convert("RGB")
img2 = Image.open('catodog.jpg').convert("RGB")

hashimg1 = hashlib.sha512(img1.tobytes()).hexdigest()
print(hashimg1)

hashimg2 = hashlib.sha512(img2.tobytes()).hexdigest()
print(hashimg2)