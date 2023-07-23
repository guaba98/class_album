# import rgb as rgb
from PyQt5.QtCore import *
# from PyQt5.QtGui import *
# from PyQt5.QtWidgets import *

# from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect


class PageBtn(object):
    def __init__(self, txt=None, parent=None):
        self.parent = parent

        # 버튼 생성
        self.button = QPushButton()
        self.button.setMinimumSize(QSize(40, 40))
        self.button.setMaximumSize(QSize(40, 40))
        self.button.setText(txt)
        self.set_background_color(self.button)

        # 버튼 클릭 이벤트
        self.button.clicked.connect(lambda x, y=txt: self.parent.move_paging(y))
        self.button.clicked.connect(self.change_color_btn)

    def set_background_color(self, btn):
        effect = QGraphicsDropShadowEffect()
        effect.setBlurRadius(5)
        effect.setColor(QColor(0, 0, 0, 100))
        effect.setOffset(1, 3)  # 객체와 그림자 사이의 거리 또는 변위
        btn.setGraphicsEffect(effect)

    def change_color_btn(self):
        print('여길 탑니다')
        for btn in self.parent.paging_widget.findChildren(QPushButton):
            btn.setStyleSheet('background-color: white;')
        self.button.setStyleSheet('background-color: rgb(47, 128, 237);')
        print(self.button.text())

    @property
    def btn_return(self):
        return self.button
