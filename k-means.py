import PIL, urllib.request, io, sys, random, statistics as stat, time
from PIL import Image
print('running')

k = int(sys.argv[1])
for arg in sys.argv:
    if arg[0:4] == "http":
        URL = arg
        print(URL)
        f = io.BytesIO(urllib.request.urlopen(URL).read())
    elif arg[-3: -1] == 'jp':
        f = arg

img = Image.open(f)
#img.show()
SIZE = img.size[0]*img.size[1]
print('size: ', img.size[0], 'x', img.size[1]) #w,h
print('pixels: ', SIZE)
pix = img.load()
#img.show()

means = [pix[img.size[0]//2, img.size[1]//2]]
colors = dict()
coordColor = dict()
#print(pix[2,5], means) #(r,g,b) 0-sr255
for i in range(1, k):
    means.append(pix[random.random()*img.size[0], random.random()*img.size[1]])

pixset = set()
for x in range(img.size[0]):
    for y in range(img.size[1]):
        pixset.add((x, y))
        colors[pix[(x, y)]] = colors.get(pix[x, y], []) + [(x, y)]

print('Distinct Pixel Count: ', len(colors))
mcp = max(colors.keys(), key=lambda a: len(colors[a]))
print("Most Common Pixel: ", mcp, '=>', len(colors[mcp]))


t = time.time()
nochange = False
while not nochange:
    #print('again', img.size)
    nochange = True
    points = [list() for i in range(k)]
    for r,g,b in colors:
        #for y in range(img.size[1]):
        group = int(min(range(k), key=lambda gg: (means[gg][0]-r)**2 + (means[gg][1]-g)**2 + (means[gg][2]-b)**2))
        points[group].append((r,g,b))       # points = list of rgb tuples of each colorgroup
        #print([len(points[g]) for g in range(len(points))])
        if (r,g,b) in coordColor: oldG = coordColor[(r,g,b)]
        else: oldG = -1
        #print(oldG, group, nochange)
        if oldG != group:
            nochange = False
        coordColor[(r,g,b)] = group
        #print(x,y,group, means[group])
    for mi in range(len(means)):
        #print([len(points[i]) for i in range(len(points))])
        if points[mi]:
            totP = sum([len(colors[i]) for i in points[mi]])  # total points in this group
            means[mi] = (sum([(i[0]*len(colors[i])/totP) for i in points[mi]]), sum([(i[1]*len(colors[i])/totP) for i in points[mi]]), sum([(i[2]*len(colors[i])/totP) for i in points[mi]]))


    #print('means: ', means)
    #print('iii', nochange)
    #sys.exit()

for rgb in colors:
    group = coordColor[rgb]
    for p in colors[rgb]:
        #print(means[group])
        pix[p] = (int(means[group][0]), int(means[group][1]), int(means[group][2]))
avgToGroup = {(int(a[0]), int(a[1]), int(a[2])):i for i,a in enumerate(means)}
#print([len(points[i]) for i in range(k)])

print('Final means: ')
for i in range(k):
    print(i+1, ': ', means[i], ' => ', sum([len(colors[c]) for c in points[i]]))

#print FLOATS


def areafill(pix, k, pixset, avgG):
    #sys.setrecursionlimit(50225)
    # start = (0,0)
    regions = [0]*k
    while pixset:
        start = pixset.pop()
        Ogcolor = pix[start]
        lll = len(pixset)
        pixset.add(start)
        startcolor = pix[start]
        #print(start, startcolor, len(pixset))
        #print(coordColor)
        alist = [start]
        while alist:
            aa = alist.pop()
            #if pix[aa] == startcolor:
            if aa not in pixset: continue
            pixset.remove(aa)
            if (aa[0] + 1, aa[1]) in pixset and pix[aa[0] + 1, aa[1]] == startcolor: alist.append((aa[0] + 1, aa[1]))
            if (aa[0], aa[1] + 1) in pixset and pix[aa[0], aa[1] + 1] == startcolor: alist.append((aa[0], aa[1] + 1))
            if (aa[0] - 1, aa[1]) in pixset and pix[aa[0] - 1, aa[1]] == startcolor: alist.append((aa[0] - 1, aa[1]))
            if (aa[0], aa[1] - 1) in pixset and pix[aa[0], aa[1] - 1] == startcolor: alist.append((aa[0], aa[1] - 1))

            if (aa[0] + 1, aa[1] + 1) in pixset and pix[aa[0] + 1, aa[1] + 1] == startcolor: alist.append((aa[0] + 1, aa[1] + 1))
            if (aa[0] - 1, aa[1] + 1) in pixset and pix[aa[0] - 1, aa[1] + 1] == startcolor: alist.append((aa[0] - 1, aa[1] + 1))
            if (aa[0] - 1, aa[1] - 1) in pixset and pix[aa[0] - 1, aa[1] - 1] == startcolor: alist.append((aa[0] - 1, aa[1] - 1))
            if (aa[0] + 1, aa[1] - 1) in pixset and pix[aa[0] + 1, aa[1] - 1] == startcolor: alist.append((aa[0] + 1, aa[1] - 1))
        regions[avgG[Ogcolor]] += 1
    return regions



print('Region Counts: ', areafill(pix, k, pixset, avgToGroup))
print('time: ', time.time()-t)
img.show()
#img.save("kmeans/{}.png".format("2020zyang"), "PNG")
