from PIL import Image, ImageOps

my_image = Image.open('Wallpapers\sd (11).jpg')
# my_image.show()

# convert to gray scale
gray_scale_image = ImageOps.grayscale(my_image)
# gray_scale_image.show()


equalized_image = ImageOps.equalize(my_image)
equalized_image.show()


