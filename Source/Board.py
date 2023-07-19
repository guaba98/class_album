from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from UI.UI_board_read import Ui_board_read_widget
from UI.UI_board_write import Ui_board_write_widget

class BoardWrite(QWidget, Ui_board_write_widget):
    """글 작성하는 클래스"""
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 이미지 업로드 버튼 클릭시 사진 업로드 창 띄우기
        self.img_upload_btn.clicked.connect(self.upload_image)

        # 등록 버튼 클릭시 db에 저장
        self.admit_btn.clicked.connect(self.save_contents)

    def save_contents(self):
        """글 내용과 이미지를 db에 저장합니다."""
        pass

    def upload_image(self):
        """이미지 업로드 창 띄우기"""
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Images (*.png *.jpg)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            pixmap = QPixmap(file_path)
            self.img_lab.setPixmap(pixmap.scaled(QSize(200,200), aspectRatioMode=Qt.KeepAspectRatio))



class BoardRead(QWidget, Ui_board_read_widget):
    """글 읽는 부분"""
    def __init__(self, writer, title, write_time, img_path, contents): # 제목, 이미지 경로, 글내용
        super().__init__()
        self.setupUi(self)

        self.writer_lab.setText(writer)
        self.write_time_lab.setText(write_time)
        # self.img_lab.setPixmap(QPixmap(img_path)) # 이미지
        self.contents_lab.setText(contents)
        # self.tableWidget # 댓글 내용

