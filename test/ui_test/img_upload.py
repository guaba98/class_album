from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QFileDialog
from PyQt5.Qt import *
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Image Upload Example")

        self.label = QLabel(self)
        self.label.setGeometry(10, 10, 300, 300)

        self.button = QPushButton("Upload Image", self)
        self.button.setGeometry(10, 320, 100, 30)
        self.button.clicked.connect(self.upload_image)

    def upload_image(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Images (*.png *.jpg)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            self.label.setPixmap(pixmap.scaled(self.label.size(), aspectRatioMode=Qt.KeepAspectRatio))

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
