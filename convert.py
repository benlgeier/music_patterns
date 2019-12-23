from PIL import Image, ImageDraw

if __name__ == '__main__':

	song = open("powerful.txt", "r").read().split()
	for word in range(len(song)):
		song[word] = song[word].lower().strip(",")
	
	box_size = 10
	song_len = len(song)
	img_size = song_len * box_size

	song_grid = [["" for i in range(song_len)] for j in range(song_len)]
	
	for y in range(song_len):
		for x in range(song_len):
			if song[y] == song[x]:
				song_grid[y][x] = song[x]

	print(song_grid)


	# image = Image.new(mode='RGB', size=(img_size, img_size), color=(0,0,0))

	# for y in range(0, img_size, box_size):
	# 	for x in range(0, img_size, box_size):
	# 		ImageDraw.Draw(image).rectangle(
	# 			[x,y,x+10,y+10],(x,y,x),(0,0,0),1)

	# image.show()

