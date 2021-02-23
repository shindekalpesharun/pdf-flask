from PIL import Image

image1 = Image.open(r'1.png')
im1 = image1.convert('RGB')
im1.save(r'1.pdf')
