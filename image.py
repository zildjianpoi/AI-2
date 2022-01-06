import PIL, urllib.request, io, sys
from PIL import Image

URL = sys.argv[1]
print(URL)
f = io.BytesIO(urllib.request.urlopen(URL).read())
img = Image.open(f)
img.show()
print(img.size) #w,h
pix = img.load()
print(pix[2,5]) #(r,g,b) 0-sr255

for x in range(img.size[0]):
    for y in range(img.size[1]):
        newVal = []
        for val in pix[x,y]:
            if val < 255//3:
                newVal.append(0)
            elif val > (255*2)//3:
                newVal.append(255)
            else:
                newVal.append(127)
        pix[x,y] = tuple(newVal)
img.show()
