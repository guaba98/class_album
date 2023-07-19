# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/UI_server.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_server_form(object):
    def setupUi(self, server_form):
        server_form.setObjectName("server_form")
        server_form.resize(978, 600)
        self.horizontalLayout = QtWidgets.QHBoxLayout(server_form)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.server_title_lab = QtWidgets.QLabel(server_form)
        self.server_title_lab.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.server_title_lab.setFont(font)
        self.server_title_lab.setObjectName("server_title_lab")
        self.gridLayout_3.addWidget(self.server_title_lab, 0, 0, 1, 1)
        self.host_ip_lab = QtWidgets.QLabel(server_form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.host_ip_lab.setFont(font)
        self.host_ip_lab.setObjectName("host_ip_lab")
        self.gridLayout_3.addWidget(self.host_ip_lab, 1, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(server_form)
        self.label_6.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 4, 1, 1, 1)
        self.connected_info_lab = QtWidgets.QLabel(server_form)
        self.connected_info_lab.setMinimumSize(QtCore.QSize(0, 60))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.connected_info_lab.setFont(font)
        self.connected_info_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.connected_info_lab.setObjectName("connected_info_lab")
        self.gridLayout_3.addWidget(self.connected_info_lab, 3, 0, 1, 1)
        self.send_btn = QtWidgets.QPushButton(server_form)
        self.send_btn.setMinimumSize(QtCore.QSize(0, 28))
        self.send_btn.setObjectName("send_btn")
        self.gridLayout_3.addWidget(self.send_btn, 6, 3, 1, 1)
        self.label_7 = QtWidgets.QLabel(server_form)
        self.label_7.setMaximumSize(QtCore.QSize(16777215, 15))
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 5, 2, 1, 1)
        self.host_port_lineedit = QtWidgets.QLineEdit(server_form)
        self.host_port_lineedit.setMinimumSize(QtCore.QSize(309, 40))
        self.host_port_lineedit.setObjectName("host_port_lineedit")
        self.gridLayout_3.addWidget(self.host_port_lineedit, 2, 2, 1, 1)
        self.tableWidget_members = QtWidgets.QTableWidget(server_form)
        self.tableWidget_members.setObjectName("tableWidget_members")
        self.tableWidget_members.setColumnCount(2)
        self.tableWidget_members.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_members.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget_members.setHorizontalHeaderItem(1, item)
        self.gridLayout_3.addWidget(self.tableWidget_members, 4, 0, 3, 1)
        self.host_port_lab = QtWidgets.QLabel(server_form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.host_port_lab.setFont(font)
        self.host_port_lab.setObjectName("host_port_lab")
        self.gridLayout_3.addWidget(self.host_port_lab, 1, 2, 1, 1)
        self.host_ip_lineedit = QtWidgets.QLineEdit(server_form)
        self.host_ip_lineedit.setMinimumSize(QtCore.QSize(309, 40))
        self.host_ip_lineedit.setObjectName("host_ip_lineedit")
        self.gridLayout_3.addWidget(self.host_ip_lineedit, 2, 0, 1, 1)
        self.server_start_btn = QtWidgets.QPushButton(server_form)
        self.server_start_btn.setMinimumSize(QtCore.QSize(124, 40))
        self.server_start_btn.setCheckable(True)
        self.server_start_btn.setObjectName("server_start_btn")
        self.gridLayout_3.addWidget(self.server_start_btn, 2, 3, 1, 1)
        self.chat_lineedit = QtWidgets.QLineEdit(server_form)
        self.chat_lineedit.setMinimumSize(QtCore.QSize(0, 28))
        self.chat_lineedit.setObjectName("chat_lineedit")
        self.gridLayout_3.addWidget(self.chat_lineedit, 6, 2, 1, 1)
        self.notice_comments_lab = QtWidgets.QLabel(server_form)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.notice_comments_lab.setFont(font)
        self.notice_comments_lab.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.notice_comments_lab.setObjectName("notice_comments_lab")
        self.gridLayout_3.addWidget(self.notice_comments_lab, 3, 2, 1, 1)
        self.chat_listwidget = QtWidgets.QListWidget(server_form)
        self.chat_listwidget.setMinimumSize(QtCore.QSize(0, 220))
        self.chat_listwidget.setObjectName("chat_listwidget")
        self.gridLayout_3.addWidget(self.chat_listwidget, 4, 2, 1, 2)
        self.gridLayout_3.setColumnStretch(0, 10)
        self.gridLayout_3.setColumnStretch(1, 10)
        self.gridLayout_3.setColumnStretch(2, 10)
        self.verticalLayout.addLayout(self.gridLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 45, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem3 = QtWidgets.QSpacerItem(95, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(server_form)
        QtCore.QMetaObject.connectSlotsByName(server_form)

    def retranslateUi(self, server_form):
        _translate = QtCore.QCoreApplication.translate
        server_form.setWindowTitle(_translate("server_form", "Form"))
        self.server_title_lab.setText(_translate("server_form", "Server setting"))
        self.host_ip_lab.setText(_translate("server_form", "HOST_IP"))
        self.connected_info_lab.setText(_translate("server_form", "접속자 정보"))
        self.send_btn.setText(_translate("server_form", "전송"))
        item = self.tableWidget_members.horizontalHeaderItem(0)
        item.setText(_translate("server_form", "IP"))
        item = self.tableWidget_members.horizontalHeaderItem(1)
        item.setText(_translate("server_form", "PORT"))
        self.host_port_lab.setText(_translate("server_form", "HOST_PORT"))
        self.server_start_btn.setText(_translate("server_form", "서버 실행"))
        self.notice_comments_lab.setText(_translate("server_form", "채팅 공지 알림"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    server_form = QtWidgets.QWidget()
    ui = Ui_server_form()
    ui.setupUi(server_form)
    server_form.show()
    sys.exit(app.exec_())