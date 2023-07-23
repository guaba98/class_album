from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.Qt import *
from UI.UI_board_read import Ui_board_read_widget
from UI.UI_board_write import Ui_board_write_widget


# img = 'C:\\Users\\KDT103\\Desktop\\coding\\0. 프로젝트\\개인프로젝트\\class_album\\Data\\receive_img\\img_1.png'
class BoardWrite(QWidget, Ui_board_write_widget):
    """글 작성하는 클래스"""

    def __init__(self, parent):
        super().__init__()
        self.setupUi(self)

        # 변수선언
        self.parent = parent
        self.img_path = None

        # 이미지 업로드 버튼 클릭시 사진 업로드 창 띄우기
        self.img_upload_btn.clicked.connect(self.upload_image)

        # 등록 버튼 클릭시 db에 저장
        self.admit_btn.clicked.connect(self.save_contents)




    def save_contents(self):
        """글 내용과 이미지를 db에 저장합니다."""
        print('여기에 글과 이미지를 저장합니다.')

        title = self.title_lineedit.text()  # 제목
        contents = self.contents_textedit.toPlainText()  # 내용
        img_path = self.img_path
        print("사진 저장 중: ", title, contents, img_path)

        self.parent.send_save_post(title, contents, img_path)

    def upload_image(self):
        """이미지 업로드 창 띄우기"""
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.AnyFile)
        file_dialog.setNameFilter("Images (*.png *.jpg)")

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            print('사진 경로: ', file_path)
            self.img_path = file_path
            pixmap = QPixmap(file_path)
            self.img_lab.setPixmap(pixmap.scaled(QSize(200, 200), aspectRatioMode=Qt.KeepAspectRatio))


class BoardRead(QWidget, Ui_board_read_widget):
    """글 읽는 부분"""

    def __init__(self, writer, title, write_time, img_path, contents, parent):  # 제목, 이미지 경로, 글내용
        super().__init__()
        self.setupUi(self)

        # 변수선언
        self.parent = parent
        self.is_admin = False

        # 값 넣어주기
        self.writer_lab.setText(writer)
        self.write_time_lab.setText(write_time)
        self.img_lab.setPixmap(QPixmap(img_path).scaled(QSize(500, 500), aspectRatioMode=Qt.KeepAspectRatio))  # 이미지
        self.contents_lab.setText(str(contents))

        # 관리자 확인
        self.check_admin()

        # 댓글 테이블위젯
        self.set_reply_tablewidget()


    def check_admin(self):
        """관리자인지 확인합니다."""
        if self.parent.user_name == 'admin':
            self.is_admin = True

    def check_user_name(self):
        """글 읽기 설정 """
        print('[board.py] 유저이름, 작성자이름', self.is_admin, self.writer_lab)

        if self.is_admin or self.parent.user_name == self.writer_lab:
            self.del_btn.setVisible(True)
            self.edit_btn.setVisible(True)
        else:
            self.del_btn.setVisible(False)
            self.edit_btn.setVisible(False)

    def set_reply_tablewidget(self):
        """댓글에 들어가는 테이블 위젯 설정"""
        self.tableWidget.setRowCount(3)  # 행 -> 댓글 갯수 만큼 수정해야 함.
        self.tableWidget.setColumnCount(4)  # 열

        # 헤더 숨기기
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)

        # 샘플 넣기
        for row in range(3):
            # 이름 라벨
            name_label = QLabel(f'Name {row}')
            # 댓글 라벨
            comment_label = QLabel(f'Comment {row}')
            # 수정 버튼
            edit_button = QPushButton('Edit')
            self.set_btn_style(edit_button)
            # 삭제 버튼
            delete_button = QPushButton('Delete')
            self.set_btn_style(delete_button)
            delete_button.clicked.connect(lambda _, row=row: self.delete_row(row))

            layout = QHBoxLayout()  # 가로로 배치하기 위해 QHBoxLayout 사용
            layout.addWidget(name_label)
            layout.addWidget(comment_label)
            layout.addWidget(edit_button)
            layout.addWidget(delete_button)

            container = QWidget()
            container.setLayout(layout)

            # 각 행에 순서대로 넣어주기 - 조건에 따라
            if self.is_admin:
                # 만약 관리자라면 모든 버튼을 행에 넣어주기
                self.tableWidget.setCellWidget(row, 0, name_label)
                self.tableWidget.setCellWidget(row, 1, comment_label)
                self.tableWidget.setCellWidget(row, 2, edit_button)
                self.tableWidget.setCellWidget(row, 3, delete_button)
            else:
                # 관리자가 아니면 수정과 삭제 버튼은 숨기기
                self.tableWidget.setCellWidget(row, 0, name_label)
                self.tableWidget.setCellWidget(row, 1, comment_label)

            # self.tableWidget.setCellWidget(row, 0, name_label)
            # self.tableWidget.setCellWidget(row, 1, comment_label)
            # self.tableWidget.setCellWidget(row, 2, edit_button)
            # self.tableWidget.setCellWidget(row, 3, delete_button)

        # 열 크기 조정
        self.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)  # 첫 번째 열을 stretch로 조절
        self.tableWidget.horizontalHeader().setSectionResizeMode(1, QHeaderView.ResizeToContents)  # 두 번째 열은 콘텐츠에 맞게 조절
        self.tableWidget.horizontalHeader().setSectionResizeMode(2, QHeaderView.ResizeToContents)  # 세 번째 열은 콘텐츠에 맞게 조절

        # # 열 크기로 헤더 조정하기
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)

    def delete_row(self, row):
        # 테이블 위젯에서 특정 행 삭제
        self.tableWidget.removeRow(row)

    def set_btn_style(self, btn):
        btn_style = '''
        QPushButton {
                    background-color: #2F80ED;
                    color: white;
                    border: 2px solid #2F80ED;
                    border-radius: 5px;
                    font-size: 14px;
                }

                QPushButton:hover {
                    background-color: #3C8DF5;  /* 밝은 색 */
                    border-color: #3C8DF5;
                }

                QPushButton:pressed {
                    background-color: #1B67B2;  /* 진한 색 */
                    border-color: #1B67B2;
                }
        '''
        btn.setStyleSheet(btn_style)