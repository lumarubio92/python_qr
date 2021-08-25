#
#pip install wifi-qrcode-generator
import wifi_qrcode_generator as qr
import qrcode 

SSID= 'nombre de la red'
PASSWORD= 'contraseña de red'
# formato de cadena para conexion de red  WIFI:S:<SSID>;T:<WPA|WEP|>;P:<password>;;
# wb es el modo para abrir el archivo 'w' escritura , 'b' binario
qr= qrcode.make(f"WIFI:S:{SSID};T:WPA;P:{PASSWORD};;")
f = open("wifi_Qr.png","wb")
qr.save(f)
f.close()
