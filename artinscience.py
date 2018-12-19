from avy_gis.lib.topo_db import topo_db
from colour import Color
import numpy as np
import scipy.misc as smp

db = topo_db()

r = Color('red')
p = Color('purple')
gradient = list(r.range_to(p, 91))

def getColorIndex(rad):
	minA = -1
	maxA = 6.28319
	if(rad < minA):
		rad = minA
	if(rad > maxA):
		rad = maxA
	return int(round(((rad)/(maxA)) * 90))

def color_to_rgb(c):
	return map(lambda x:int(round(x * 255)), [c.get_red(),c.get_green(),c.get_blue(), 1])

bbox = {'sw': {'lat': 46.797337,'lon': -121.847628},'ne': {'lat': 46.913387,'lon': -121.676930}}
topo_data = db.get_bbox(bbox, ['aspect'])
aspects = topo_data['aspect']

img_data = []
for row in aspects:
	img_data.insert(0,[])
	for col in row:
		gradient_index = getColorIndex(col)
		c = gradient[gradient_index]
		img_data[0].append(color_to_rgb(c))
img = smp.toimage(img_data)
img.save('artinscience.png')