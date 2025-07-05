from PIL import Image
import urllib.request
# reading image from disk
my_image = Image.open('Wallpapers\sd (8).jpg')
# my_image.show()

# reading image from a url
url = 'https://hips.hearstapps.com/hmg-prod/images/spring-flowers-65de4a13478ee.jpg?crop=1.00xw:0.752xh;0,0.154xh&resize=1200:*'
# download image
urllib.request.urlretrieve(url, 'Wallpapers/Flowers.png')
# show image
downloaded_image = Image.open('Wallpapers/Flowers.png')
# downloaded_image.show()

# save an image
downloaded_image.save('Wallpapers/Flowers2.jpg')

# create new image
new_image = Image.new('RGB', (500,500), color='blue')
# new_image.show()
new_image = Image.new('RGB', (500,500), color='#c30010')
new_image.show()