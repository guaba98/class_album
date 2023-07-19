import rgb as rgb
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QPushButton, QApplication, QGraphicsDropShadowEffect


class PageBtn(object):
    def __init__(self, lay, txt):

        self.button = QPushButton()
        self.button.setMinimumSize(QSize(40, 40))
        self.button.setMaximumSize(QSize(40, 40))
        self.button.setText(txt)

        # 버튼 그림자 생성
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QColor(0, 0, 0, 100))
        effect.setOffset(1, 3) # 객체와 그림자 사이의 거리 또는 변위
        self.button.setGraphicsEffect(effect)

    @property
    def btn_return(self):
        return self.button
