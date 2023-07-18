import sys

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QFontDatabase

from mainwidget import MainWidget

def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")



    window = MainWidget()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()