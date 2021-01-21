from PIL import Image
#pip install pillow

#xxd -p Reverseit | tr -d '\n' | rev | xxd -r -p > 1.jpg
#convert -flop 1.jpg 2.jpg

with open("0.png",'rb') as file: #按照二进制位读取文件
	tmp = file.read()[::-1]
jpg = b""
for i in tmp:
	jpg += bytes.fromhex(hex(i)[2:][::-1].ljust(2,"0"))
print(jpg)
with open("Reverse-it.jpg",'wb') as file:
	file.write(jpg)

im = Image.open("Reverse-it.jpg")
im.transpose(Image.FLIP_LEFT_RIGHT).save("Reverse-it-to.jpg")
im.close()