'''
验证码的识别
利用了 tesserocr
直接扫描一遍图片就可以得出图片上的文本
'''
import tesserocr
from PIL import Image

# image = Image.open('code.jpg')
# result = tesserocr.image_to_text(image)
# print(result)
#
image = Image.open('code2.jpg')
# result = tesserocr.image_to_text(image)
# print(result)
image.show()
print(tesserocr.image_to_text(image))

image = image.convert("L")
image.show()
print(tesserocr.image_to_text(image))

image = image.convert("1")
image.show()
print(tesserocr.image_to_text(image))
