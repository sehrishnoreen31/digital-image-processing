from PIL import Image
import matplotlib.pyplot as plt
my_img = Image.open('Wallapers\sd (3).jpg')

# image format
print(my_img.format)

# image size
print(my_img.size)

# image mode
print(my_img.mode)

# show image
# my_img.show(title='Scene')
plt.imshow(my_img)
plt.axis('off')
plt.show()

