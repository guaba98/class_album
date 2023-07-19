import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

from Source.mainwidget import MainWidget


def main():
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # 글꼴 설정
    fontDB = QFontDatabase()
    fontDB.addApplicationFont('./font/NanumSquareNeo-aLt.ttf')
    fontDB.addApplicationFont('./font/NanumSquareNeo-bRg.ttf')
    fontDB.addApplicationFont('./font/NanumSquareNeo-cBd.ttf')
    fontDB.addApplicationFont('./font/NanumSquareNeo-dEb.ttf')
    fontDB.addApplicationFont('./font/NanumSquareNeo-eHv.ttf')

    window = MainWidget()
    window.show()
    app.exec_()


if __name__ == "__main__":
    main()
