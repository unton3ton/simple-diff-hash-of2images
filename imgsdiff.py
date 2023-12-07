from PIL import Image

img1 = Image.open('catodog85percent.jpg').convert("RGB")
img2 = Image.open('catodog.jpg').convert("RGB")
 
N = 0
new_image = Image.new("RGB", (img1.size[0], img1.size[1]))

for i in range(img1.size[0]):
    for j in range(img1.size[1]):
        if (img1.getpixel((i,j)) != img2.getpixel((i,j))):
            N += 1
            i1 = img1.getpixel((i,j))
            i2 = img2.getpixel((i,j))
            new_image.putpixel((i, j), tuple([i1[0]-i2[0],i1[1]-i2[1],i1[2]-i2[2]]))

print("diff pixls = ", N) # diff pixls =  179958


new_image.show()
new_image.save("diffimage.png")