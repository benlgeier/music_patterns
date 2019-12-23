from PIL import Image

if __name__ == '__main__':
	height = 600
	width = 600 
	image = Image.new(mode='L', size=(height,width), color=255)

	image.show()