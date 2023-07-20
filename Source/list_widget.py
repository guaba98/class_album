from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from UI.UI_list import Ui_Form


class ListItem(QWidget, Ui_Form):
    def __init__(self, number, title: str, writer: str, write_date, parent):
        super().__init__()
        self.setupUi(self)

        self.number = number
        self.title = title
        self.writer = writer
        self.write_date = write_date
        self.parent = parent

        # 라벨에 자료 넣기
        self.num_lab.setText(number)
        self.writer_lab.setText(writer)
        self.title_lab.setText(title)
        self.date_lab.setText(write_date)

        # 프레임 클릭하면 창 옮기기

        self.List_frame.mousePressEvent = lambda event: self.parent.move_to_contents(
            number, title, writer, write_date)


    def set_title_bar(self):
        """타이틀 스타일을 변경합니다."""
        self.List_frame.setStyleSheet('background-color: #2F80ED')  # 타이틀 배경색 변경
        title_labels = self.List_frame.findChildren(QLabel)  # 타이틀 폰트색 변경
        for labs in title_labels:
            labs.setStyleSheet("color: {}".format(QColor(255, 255, 255).name()))

    def set_contents_bar(self):
        """내용 제목을 변경합니다. -> 하단에만 파란 선 추가"""
        self.List_frame.setStyleSheet(
            """
            border: 1px solid #2F80ED;
            border-right-color: transparent;
            border-left-color: transparent;
            border-top-color: transparent;
            """
        )

    # self.frame.mousePressEvent = self.move_page
