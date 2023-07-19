# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
# from PyQt5.QtGui import QGraphicsDropShadowEffect
# from PyQt5.QtCore import Qt
#
#
# def add_shadow_effect(widget):
#     shadow = QGraphicsDropShadowEffect()
#     shadow.setBlurRadius(8)
#     shadow.setColor(Qt.black)
#     shadow.setOffset(0, 0)
#     widget.setGraphicsEffect(shadow)
#
# app = QApplication([])
# window = QMainWindow()
#
# button = QPushButton("Shadowed Button")
# add_shadow_effect(button)
#
# window.setCentralWidget(button)
# window.show()
#
# app.exec_()

from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QGraphicsDropShadowEffect
from PyQt5.QtGui import QColor

app = QApplication([])

start_button = QPushButton()
start_button.setText("")
label = QLabel(start_button)
label.setText("<b>Button</b>")
effect = QGraphicsDropShadowEffect()
effect.setBlurRadius(5)
effect.setColor(QColor(0, 0, 0, 255))  # Set the shadow color (black with full opacity)
effect.setOffset(0, 0)  # Set the shadow offset
label.setGraphicsEffect(effect)

start_button.show()
app.exec()
