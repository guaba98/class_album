import socket
from PIL import Image
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from io import BytesIO

app = QApplication(sys.argv)
widget = QWidget()
label = QLabel(widget)

HOST = "10.10.20.103" # socket.gethostbyname(socket.gethostname())
PORT = 1121

s = socket.socket()
s.connect((HOST, PORT))
#
# while True:
#     image_binaries = s.recv(100000000)
#     if not image_binaries:
#         break
#     img = Image.open(BytesIO(image_binaries))
#     # img = Image.open(bytes(image_binaries))
image_binaries = b""
while True:
    chunk = s.recv(100000000)
    if not chunk:
        break
    image_binaries += chunk
s.close()


pixmap = QPixmap()
pixmap.loadFromData(image_binaries)
label.setPixmap(pixmap)
widget.resize(pixmap.width(), pixmap.height())

widget.show()
sys.exit(app.exec_())

