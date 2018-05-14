from PIL import Image
im = Image.open("日出.jpg")
r, g, b = im.split()
om = Image.merge("RGB", (b, g, r))
om.save("日出BGR.jpg")