from PIL import Image
im = Image.open("日出.jpg")
im.thumbnail((2.74, 3.65))
im.save("日出TN","JPEG")