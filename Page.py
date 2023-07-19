import rgb as rgb
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor, QPen, QBrush
from PyQt5.QtWidgets import QPushButton, QApplication


class ShadowButton(QPushButton):
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 원래 버튼의 배경을 그리기
        super().paintEvent(event)

        # 그림자 그리기
        shadow_color = QColor(0, 0, 0, 100)  # 그림자 색상 (검은색, 투명도 100)
        shadow_offset = 2  # 그림자의 수평 및 수직 오프셋

        path = QPainterPath()
        path.addRoundedRect(
            shadow_offset, shadow_offset,
            self.width() - 2 * shadow_offset, self.height() - 2 * shadow_offset,
            self.height() / 2, self.height() / 2
        )

        painter.setPen(Qt.NoPen)
        painter.setBrush(QBrush(shadow_color))
        painter.drawPath(path.translated(0, shadow_offset))


class PageBtn(object):
    def __init__(self, lay, txt):
        self.button = QPushButton()
        self.button.setMinimumSize(QSize(40, 40))
        self.button.setMaximumSize(QSize(40, 40))
        self.button.setText(txt)

        # 일단 버튼 스타일시트 부분은일단둬바
        # self.button.setStyleSheet('''
        #     QPushButton {
        #         color: black;
        #         background-color: #FFFFFF;
        #         border-radius: 5px;
        #         padding: 10px;
        #         border-bottom: 3px solid black;
        #         box-shadow: 2px 2px 5px rgba(45, 45, 45, 0.5);
        #     }
        #     QPushButton:hover {
        #         box-shadow: 4px 4px 8px rgba(0, 0, 0, 0.7);
        #     }
        # ''')

    # def arrow_btn(self):
    #     """화살표 버튼"""


    def btn_return(self):
        return self.button
