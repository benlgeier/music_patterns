from PIL import Image, ImageDraw

if __name__ == '__main__':
	# height = 600
	# width = 600 
	# image = Image.new(mode='RGB', size=(height,width), color=(0,0,0))

	# size = 10

	# for y in range(0, height, size):
	# 	for x in range(0, width, size):
	# 		ImageDraw.Draw(image).rectangle(
	# 			[x,y,x+10,y+10],(x,y,x),(0,0,0),1)

	# image.show()

	song = open("powerful.txt", "r").read().split()
	for word in range(len(song)):
		song[word] = song[word].lower().strip(",")
	print(song)
