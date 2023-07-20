from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtCore import Qt
import sys
from UI.UI_warning import Ui_Dialog

class DialogWarning(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.connect_event()
        self.set_dialog_type(t_type='used_id', bt_cnt=None)

    # 아니오, 닫기 눌렀을 때
    # def reject(self) -> None:
    #     print('아니오')
    #     self.setResult(0)
    #     self.close()

    # 예, 확인 눌렀을 때
    # def accept(self) -> None:
    #     print('예')
    #     self.setResult(1)
    #     self.close()
    #
    def accept_btn(self):
        print('예')
        self.close()
    def reject_btn(self):
        print('아니오')
        self.close()

    # 이벤트 연결
    def connect_event(self):
        # 예, 확인 : accept (1)
        # 아니오, 닫기 : reject (0)
        self.yes_btn.clicked.connect(self.accept_btn)
        self.no_btn.clicked.connect(self.reject_btn)

    # 다이얼로그 타입 설정
    # bt_cnt : 버튼 수량
    # t_type : 다이얼로그 타입
    def set_dialog_type(self, bt_cnt: int, t_type="", text=""):
        # if bt_cnt == 1:
        #     self.layout_double.setVisible(False)
        #     self.btn_single.setVisible(True)
        #
        # elif bt_cnt == 2:
        #     self.layout_double.setVisible(True)
        #     self.btn_single.setVisible(False)
        if text:
            self.lbl_text.setText(text)
        elif t_type == 'used_id':
            self.warning_lab.setText('사용 중인 아이디입니다.')
        elif t_type == 'user_can_use_id':
            self.warning_lab.setText('사용할 수 있는 아이디입니다.')

if __name__ == '__main__':
    # app = QApplication(sys.argv)
    # d = DialogWarning()
    # d.show()
    # app.exec_()
    pass