
#pip install qrcode
import qrcode

img= qrcode.make("bienvenido de nuevo")
f = open("qr.png","wb")
img.save(f)
f.close()
