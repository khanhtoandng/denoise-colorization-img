from PIL import Image

col = Image.open("test.jpg")
gray = col.convert('L')
bw = gray.point(lambda x: 0 if x<128 else 255, '1')
bw.save("man_bn.png")
