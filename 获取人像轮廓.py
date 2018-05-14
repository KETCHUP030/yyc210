from PIL import Image
from PIL import ImageFilter
im = Image.open("R.jpg")
om = im.filter(ImageFilter.CONTOUR)
om.save("RContour.jpg")