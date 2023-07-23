from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class MsgBox(QWidget):
    def __init__(self, msg_txt, send_time, parent):
        super().__init__()
        self.resize(685, 131)

        # v 레이아웃 설정
        self.v_lay = QVBoxLayout(self)
        self.v_lay.setObjectName('v_lay')
        self.v_lay.setContentsMargins(5, 5, 5, 5)

        # h 레이아웃 설정
        self.h_lay = QHBoxLayout()
        self.h_lay.setObjectName('h_lay')
        self.h_lay.setContentsMargins(9, 9, 9, 9)
        self.h_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.h_lay.addItem(self.h_spacer)

        # 메세지 라벨 설정
        self.msg_lab = QLabel(self)
        self.msg_lab.setObjectName('msgbox')
        self.msg_lab.setMinimumSize(QSize(0, 35))
        self.msg_lab.setStyleSheet('''
            background-color: #C1D9FA;
            padding: 5px;    
            border-radius: 7px;
            ''')

        font = QFont()
        font.setFamily("나눔스퀘어 네오 Regular")
        font.setPointSize(10)
        self.msg_lab.setFont(font)

        self.h_lay.addWidget(self.msg_lab)
        self.v_lay.addLayout(self.h_lay)

        self.v_spacer = QSpacerItem(20, 0, QSizePolicy.Minimum, QSizePolicy.Preferred)
        self.v_lay.addItem(self.v_spacer)

        # 라벨에 메세지 넣기
        self.msg_lab.setText(msg_txt)

if __name__ == '__main__':
    # app = QApplication([])
    # window = MsgBox('테스트 중 이것은 메세지 메세지 메세지 메셎지', '11:50', parent=None)
    # window.show()
    # app.exec_()
    pass
