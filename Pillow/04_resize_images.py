from PIL import Image, ImageOps

my_image = Image.open('Wallpapers/Flowers.png')

# new size of image
new_size = (300,300)
# resize
resized_image = my_image.resize(new_size)
# cover area
resized_image = ImageOps.cover(resized_image, (300,300))
# fit area
resized_image = ImageOps.fit(resized_image, (300,300))
# show image
# resized_image.show()

# resize image by maintaining same aspect ratio
new_width = 300
resized_image2 = my_image.resize((new_width, int(my_image.height * (new_width/my_image.width))))
# resized_image2.show()

# scaling image
scaling_factor = 0.1
scaled_image = my_image.resize((int(my_image.width * scaling_factor), int(my_image.height * scaling_factor)))
scaled_image.show()