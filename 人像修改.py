from PIL import Image
from PIL import ImageEnhance
im = Image.open("R.jpg")
om = ImageEnhance.Contrast(im)
om.enhance(15).save("REN.jpg")