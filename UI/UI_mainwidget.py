# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/UI_mainwidget.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(978, 600)
        MainWindow.setMinimumSize(QtCore.QSize(978, 600))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.login_page)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.login_main_widget = QtWidgets.QWidget(self.login_page)
        self.login_main_widget.setMinimumSize(QtCore.QSize(338, 0))
        self.login_main_widget.setObjectName("login_main_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.login_main_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.login_main_frame = QtWidgets.QFrame(self.login_main_widget)
        self.login_main_frame.setMinimumSize(QtCore.QSize(0, 273))
        self.login_main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.login_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.login_main_frame.setObjectName("login_main_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.login_main_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.login_title_lab = QtWidgets.QLabel(self.login_main_frame)
        self.login_title_lab.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.login_title_lab.setFont(font)
        self.login_title_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.login_title_lab.setObjectName("login_title_lab")
        self.verticalLayout_2.addWidget(self.login_title_lab)
        self.email_label = QtWidgets.QLabel(self.login_main_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.email_label.setFont(font)
        self.email_label.setObjectName("email_label")
        self.verticalLayout_2.addWidget(self.email_label)
        self.email_lineedit = QtWidgets.QLineEdit(self.login_main_frame)
        self.email_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.email_lineedit.setObjectName("email_lineedit")
        self.verticalLayout_2.addWidget(self.email_lineedit)
        self.password_label = QtWidgets.QLabel(self.login_main_frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.password_label.setFont(font)
        self.password_label.setObjectName("password_label")
        self.verticalLayout_2.addWidget(self.password_label)
        self.password_lineedit = QtWidgets.QLineEdit(self.login_main_frame)
        self.password_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.password_lineedit.setObjectName("password_lineedit")
        self.verticalLayout_2.addWidget(self.password_lineedit)
        self.register_btn = QtWidgets.QLabel(self.login_main_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_btn.setFont(font)
        self.register_btn.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.register_btn.setObjectName("register_btn")
        self.verticalLayout_2.addWidget(self.register_btn)
        self.verticalLayout_3.addWidget(self.login_main_frame)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.login_start_btn = QtWidgets.QPushButton(self.login_main_widget)
        self.login_start_btn.setMinimumSize(QtCore.QSize(124, 48))
        self.login_start_btn.setMaximumSize(QtCore.QSize(124, 48))
        self.login_start_btn.setObjectName("login_start_btn")
        self.horizontalLayout_3.addWidget(self.login_start_btn)
        self.verticalLayout_3.addLayout(self.horizontalLayout_3)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem2)
        self.horizontalLayout.addWidget(self.login_main_widget)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.horizontalLayout_2.addLayout(self.horizontalLayout)
        self.stackedWidget.addWidget(self.login_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.register_page)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.register_main_widget = QtWidgets.QWidget(self.register_page)
        self.register_main_widget.setMinimumSize(QtCore.QSize(338, 0))
        self.register_main_widget.setObjectName("register_main_widget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.register_main_widget)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem5)
        self.register_main_frame = QtWidgets.QFrame(self.register_main_widget)
        self.register_main_frame.setMinimumSize(QtCore.QSize(0, 292))
        self.register_main_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.register_main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.register_main_frame.setObjectName("register_main_frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.register_main_frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.register_title_lab = QtWidgets.QLabel(self.register_main_frame)
        self.register_title_lab.setMinimumSize(QtCore.QSize(0, 67))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.register_title_lab.setFont(font)
        self.register_title_lab.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.register_title_lab.setObjectName("register_title_lab")
        self.verticalLayout_5.addWidget(self.register_title_lab)
        self.register_name_lab = QtWidgets.QLabel(self.register_main_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_name_lab.setFont(font)
        self.register_name_lab.setObjectName("register_name_lab")
        self.verticalLayout_5.addWidget(self.register_name_lab)
        self.register_name_lineedit = QtWidgets.QLineEdit(self.register_main_frame)
        self.register_name_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.register_name_lineedit.setObjectName("register_name_lineedit")
        self.verticalLayout_5.addWidget(self.register_name_lineedit)
        self.register_email_lab = QtWidgets.QLabel(self.register_main_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_email_lab.setFont(font)
        self.register_email_lab.setObjectName("register_email_lab")
        self.verticalLayout_5.addWidget(self.register_email_lab)
        self.register_email_lineedit = QtWidgets.QLineEdit(self.register_main_frame)
        self.register_email_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.register_email_lineedit.setObjectName("register_email_lineedit")
        self.verticalLayout_5.addWidget(self.register_email_lineedit)
        self.register_cellphone_num_lab = QtWidgets.QLabel(self.register_main_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_cellphone_num_lab.setFont(font)
        self.register_cellphone_num_lab.setObjectName("register_cellphone_num_lab")
        self.verticalLayout_5.addWidget(self.register_cellphone_num_lab)
        self.register_cellphone_num_lineedit = QtWidgets.QLineEdit(self.register_main_frame)
        self.register_cellphone_num_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.register_cellphone_num_lineedit.setObjectName("register_cellphone_num_lineedit")
        self.verticalLayout_5.addWidget(self.register_cellphone_num_lineedit)
        self.register_password_lab = QtWidgets.QLabel(self.register_main_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_password_lab.setFont(font)
        self.register_password_lab.setObjectName("register_password_lab")
        self.verticalLayout_5.addWidget(self.register_password_lab)
        self.register_password_lineedit = QtWidgets.QLineEdit(self.register_main_frame)
        self.register_password_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.register_password_lineedit.setObjectName("register_password_lineedit")
        self.verticalLayout_5.addWidget(self.register_password_lineedit)
        self.register_password_recheck_lab = QtWidgets.QLabel(self.register_main_frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_password_recheck_lab.setFont(font)
        self.register_password_recheck_lab.setObjectName("register_password_recheck_lab")
        self.verticalLayout_5.addWidget(self.register_password_recheck_lab)
        self.register_password_recheck_lineedit = QtWidgets.QLineEdit(self.register_main_frame)
        self.register_password_recheck_lineedit.setMinimumSize(QtCore.QSize(0, 40))
        self.register_password_recheck_lineedit.setObjectName("register_password_recheck_lineedit")
        self.verticalLayout_5.addWidget(self.register_password_recheck_lineedit)
        self.verticalLayout_4.addWidget(self.register_main_frame)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.register_admit_btn = QtWidgets.QPushButton(self.register_main_widget)
        self.register_admit_btn.setMinimumSize(QtCore.QSize(124, 48))
        self.register_admit_btn.setMaximumSize(QtCore.QSize(124, 48))
        self.register_admit_btn.setObjectName("register_admit_btn")
        self.horizontalLayout_5.addWidget(self.register_admit_btn)
        self.verticalLayout_4.addLayout(self.horizontalLayout_5)
        self.register_login_lab = QtWidgets.QLabel(self.register_main_widget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.register_login_lab.setFont(font)
        self.register_login_lab.setAlignment(QtCore.Qt.AlignCenter)
        self.register_login_lab.setObjectName("register_login_lab")
        self.verticalLayout_4.addWidget(self.register_login_lab)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem6)
        self.horizontalLayout_4.addWidget(self.register_main_widget)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem7)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        self.stackedWidget.addWidget(self.register_page)
        self.main_page = QtWidgets.QWidget()
        self.main_page.setObjectName("main_page")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.main_page)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.category_widget = QtWidgets.QWidget(self.main_page)
        self.category_widget.setMinimumSize(QtCore.QSize(160, 0))
        self.category_widget.setMaximumSize(QtCore.QSize(160, 16777215))
        self.category_widget.setStyleSheet("background-color: rgb(47, 128, 237);")
        self.category_widget.setObjectName("category_widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.category_widget)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        spacerItem8 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_8.addItem(spacerItem8)
        self.main_category = QtWidgets.QVBoxLayout()
        self.main_category.setObjectName("main_category")
        self.verticalLayout_8.addLayout(self.main_category)
        spacerItem9 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_8.addItem(spacerItem9)
        self.horizontalLayout_6.addWidget(self.category_widget)
        self.sub_stackedwidget = QtWidgets.QStackedWidget(self.main_page)
        self.sub_stackedwidget.setObjectName("sub_stackedwidget")
        self.content_page = QtWidgets.QWidget()
        self.content_page.setObjectName("content_page")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.content_page)
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        self.widget_3 = QtWidgets.QWidget(self.content_page)
        self.widget_3.setStyleSheet("background-color: rgba(47, 128, 237, 30);")
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem10 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem10)
        self.widget_5 = QtWidgets.QWidget(self.widget_3)
        self.widget_5.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        spacerItem11 = QtWidgets.QSpacerItem(20, 96, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem11)
        self.frame_4 = QtWidgets.QFrame(self.widget_5)
        self.frame_4.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.contents_title = QtWidgets.QLabel(self.frame_4)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 네오 Bold")
        font.setPointSize(17)
        self.contents_title.setFont(font)
        self.contents_title.setObjectName("contents_title")
        self.horizontalLayout_10.addWidget(self.contents_title)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem12)
        self.search_lineedit = QtWidgets.QLineEdit(self.frame_4)
        self.search_lineedit.setMaximumSize(QtCore.QSize(150, 30))
        self.search_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.search_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.search_lineedit.setObjectName("search_lineedit")
        self.horizontalLayout_10.addWidget(self.search_lineedit)
        self.search_btn = QtWidgets.QPushButton(self.frame_4)
        self.search_btn.setMaximumSize(QtCore.QSize(43, 30))
        self.search_btn.setStyleSheet("background-color: rgb(149, 190, 246);")
        self.search_btn.setObjectName("search_btn")
        self.horizontalLayout_10.addWidget(self.search_btn)
        self.verticalLayout_10.addWidget(self.frame_4)
        self.widget_7 = QtWidgets.QWidget(self.widget_5)
        self.widget_7.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_7.setObjectName("widget_7")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.widget_7)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.main_page_contents = QtWidgets.QVBoxLayout()
        self.main_page_contents.setObjectName("main_page_contents")
        self.verticalLayout_9.addLayout(self.main_page_contents)
        spacerItem13 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_9.addItem(spacerItem13)
        self.verticalLayout_10.addWidget(self.widget_7)
        self.frame_3 = QtWidgets.QFrame(self.widget_5)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 44))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem14 = QtWidgets.QSpacerItem(601, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem14)
        self.reply_lineedit = QtWidgets.QLineEdit(self.frame_3)
        self.reply_lineedit.setMinimumSize(QtCore.QSize(620, 30))
        self.reply_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.reply_lineedit.setObjectName("reply_lineedit")
        self.horizontalLayout_11.addWidget(self.reply_lineedit)
        self.reply_btn = QtWidgets.QPushButton(self.frame_3)
        self.reply_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.reply_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.reply_btn.setStyleSheet("background-color: rgb(47, 128, 237);")
        self.reply_btn.setObjectName("reply_btn")
        self.horizontalLayout_11.addWidget(self.reply_btn)
        self.write_contents_btn = QtWidgets.QPushButton(self.frame_3)
        self.write_contents_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.write_contents_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.write_contents_btn.setStyleSheet("background-color: rgb(47, 128, 237);")
        self.write_contents_btn.setObjectName("write_contents_btn")
        self.horizontalLayout_11.addWidget(self.write_contents_btn)
        self.verticalLayout_10.addWidget(self.frame_3)
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 45))
        self.widget_6.setMaximumSize(QtCore.QSize(16777215, 45))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        spacerItem15 = QtWidgets.QSpacerItem(332, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem15)
        self.main_paging = QtWidgets.QHBoxLayout()
        self.main_paging.setSpacing(10)
        self.main_paging.setObjectName("main_paging")
        self.horizontalLayout_13.addLayout(self.main_paging)
        spacerItem16 = QtWidgets.QSpacerItem(332, 19, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem16)
        self.verticalLayout_10.addWidget(self.widget_6)
        spacerItem17 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_10.addItem(spacerItem17)
        self.horizontalLayout_8.addWidget(self.widget_5)
        spacerItem18 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem18)
        self.horizontalLayout_9.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_12.addWidget(self.widget_3)
        self.sub_stackedwidget.addWidget(self.content_page)
        self.chat_page = QtWidgets.QWidget()
        self.chat_page.setObjectName("chat_page")
        self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.chat_page)
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_19.setObjectName("horizontalLayout_19")
        self.widget_4 = QtWidgets.QWidget(self.chat_page)
        self.widget_4.setStyleSheet("background-color: rgba(47, 128, 237, 30);")
        self.widget_4.setObjectName("widget_4")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.widget_4)
        self.horizontalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        spacerItem19 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem19)
        self.widget_8 = QtWidgets.QWidget(self.widget_4)
        self.widget_8.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        self.widget_8.setObjectName("widget_8")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.widget_8)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        spacerItem20 = QtWidgets.QSpacerItem(20, 103, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_11.addItem(spacerItem20)
        self.frame_5 = QtWidgets.QFrame(self.widget_8)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 40))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.frame_5)
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.chat_title = QtWidgets.QLabel(self.frame_5)
        font = QtGui.QFont()
        font.setPointSize(17)
        self.chat_title.setFont(font)
        self.chat_title.setObjectName("chat_title")
        self.horizontalLayout_16.addWidget(self.chat_title)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem21)
        self.chat_search_lineedit = QtWidgets.QLineEdit(self.frame_5)
        self.chat_search_lineedit.setMaximumSize(QtCore.QSize(150, 30))
        self.chat_search_lineedit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.chat_search_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chat_search_lineedit.setObjectName("chat_search_lineedit")
        self.horizontalLayout_16.addWidget(self.chat_search_lineedit)
        self.chat_search_btn = QtWidgets.QPushButton(self.frame_5)
        self.chat_search_btn.setMaximumSize(QtCore.QSize(43, 30))
        self.chat_search_btn.setStyleSheet("background-color: rgb(149, 190, 246);")
        self.chat_search_btn.setObjectName("chat_search_btn")
        self.horizontalLayout_16.addWidget(self.chat_search_btn)
        self.verticalLayout_11.addWidget(self.frame_5)
        self.widget_9 = QtWidgets.QWidget(self.widget_8)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 333))
        self.widget_9.setMaximumSize(QtCore.QSize(16777215, 333))
        self.widget_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.widget_9.setObjectName("widget_9")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.widget_9)
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.scrollArea = QtWidgets.QScrollArea(self.widget_9)
        self.scrollArea.setStyleSheet("QScrollBar:vertical {\n"
"background: transparent;\n"
"width: 15px;\n"
"margin: 0px;\n"
"}   \n"
"QScrollBar::handle:vertical {\n"
"background: #FFFFFF;  /* 하얀색 테두리 */\n"
"border: 2px solid #2F80ED;  /* 파란색 테두리 */\n"
"min-height: 20px;\n"
"border-radius: 5px;  /* 테두리 깍기 */\n"
"min-height: 20px;\n"
"}\n"
"QScrollBar::handle:vertical:hover{    \n"
"background-color: #2F80ED;\n"
"}\n"
"QScrollBar::handle:vertical:pressed {    \n"
"background-color: #2F80ED;\n"
"}\n"
"            \n"
"QScrollBar::add-line:vertical,\n"
"QScrollBar::sub-line:vertical,\n"
"QScrollBar::add-line:horizontal,\n"
"QScrollBar::sub-line:horizontal {\n"
"height: 0px;\n"
"width: 0px;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 42, 310))
        self.scrollAreaWidgetContents.setStyleSheet("            QScrollBar:vertical {\n"
"                background: transparent;\n"
"                width: 15px;\n"
"                margin: 0px;\n"
"            }   \n"
"            QScrollBar::handle:vertical {\n"
"                background: #FFFFFF;  /* 하얀색 테두리 */\n"
"                border: 2px solid #2F80ED;  /* 파란색 테두리 */\n"
"                min-height: 20px;\n"
"                border-radius: 5px;  /* 테두리 깍기 */\n"
"                min-height: 20px;\n"
"            }\n"
"            QScrollBar::handle:vertical:hover{    \n"
"            background-color: #2F80ED;\n"
"            }\n"
"            QScrollBar::handle:vertical:pressed {    \n"
"            background-color: #2F80ED;\n"
"            }\n"
"            \n"
"            QScrollBar::add-line:vertical,\n"
"            QScrollBar::sub-line:vertical,\n"
"            QScrollBar::add-line:horizontal,\n"
"            QScrollBar::sub-line:horizontal {\n"
"                height: 0px;\n"
"                width: 0px;\n"
"            }")
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.chat_main_contents = QtWidgets.QVBoxLayout()
        self.chat_main_contents.setObjectName("chat_main_contents")
        self.verticalLayout_7.addLayout(self.chat_main_contents)
        spacerItem22 = QtWidgets.QSpacerItem(20, 302, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem22)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout_12.addWidget(self.scrollArea)
        self.verticalLayout_11.addWidget(self.widget_9)
        self.frame_6 = QtWidgets.QFrame(self.widget_8)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.chat_lineedit = QtWidgets.QLineEdit(self.frame_6)
        self.chat_lineedit.setMinimumSize(QtCore.QSize(618, 30))
        self.chat_lineedit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.chat_lineedit.setObjectName("chat_lineedit")
        self.horizontalLayout_17.addWidget(self.chat_lineedit)
        spacerItem23 = QtWidgets.QSpacerItem(601, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_17.addItem(spacerItem23)
        self.chat_send_btn = QtWidgets.QPushButton(self.frame_6)
        self.chat_send_btn.setMinimumSize(QtCore.QSize(90, 30))
        self.chat_send_btn.setMaximumSize(QtCore.QSize(90, 16777215))
        self.chat_send_btn.setStyleSheet("background-color: rgb(47, 128, 237);")
        self.chat_send_btn.setObjectName("chat_send_btn")
        self.horizontalLayout_17.addWidget(self.chat_send_btn)
        self.verticalLayout_11.addWidget(self.frame_6)
        spacerItem24 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem24)
        self.horizontalLayout_15.addWidget(self.widget_8)
        spacerItem25 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_15.addItem(spacerItem25)
        self.horizontalLayout_14.addLayout(self.horizontalLayout_15)
        self.horizontalLayout_19.addWidget(self.widget_4)
        self.sub_stackedwidget.addWidget(self.chat_page)
        self.horizontalLayout_6.addWidget(self.sub_stackedwidget)
        self.horizontalLayout_7.addLayout(self.horizontalLayout_6)
        self.stackedWidget.addWidget(self.main_page)
        self.verticalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(2)
        self.sub_stackedwidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.login_title_lab.setText(_translate("MainWindow", "Login"))
        self.email_label.setText(_translate("MainWindow", "이메일"))
        self.email_lineedit.setText(_translate("MainWindow", "admin"))
        self.password_label.setText(_translate("MainWindow", "비밀번호"))
        self.password_lineedit.setText(_translate("MainWindow", "1234"))
        self.register_btn.setText(_translate("MainWindow", "새로오셨나요? 회원으로 함께하세요."))
        self.login_start_btn.setText(_translate("MainWindow", "시작하기"))
        self.register_title_lab.setText(_translate("MainWindow", "Register"))
        self.register_name_lab.setText(_translate("MainWindow", "이름"))
        self.register_name_lineedit.setPlaceholderText(_translate("MainWindow", "이름을 입력하세요."))
        self.register_email_lab.setText(_translate("MainWindow", "이메일"))
        self.register_email_lineedit.setPlaceholderText(_translate("MainWindow", "@을 포함하여 입력해 주세요."))
        self.register_cellphone_num_lab.setText(_translate("MainWindow", "핸드폰 번호"))
        self.register_cellphone_num_lineedit.setPlaceholderText(_translate("MainWindow", "핸드폰 번호를 입력하세요."))
        self.register_password_lab.setText(_translate("MainWindow", "비밀번호"))
        self.register_password_lineedit.setPlaceholderText(_translate("MainWindow", "영어와 숫자로 이루어져야 합니다."))
        self.register_password_recheck_lab.setText(_translate("MainWindow", "비밀번호 확인"))
        self.register_password_recheck_lineedit.setPlaceholderText(_translate("MainWindow", "비밀번호를 한번 더 입력하세요."))
        self.register_admit_btn.setText(_translate("MainWindow", "시작하기"))
        self.register_login_lab.setText(_translate("MainWindow", "이미 회원이시라면 로그인 하세요!"))
        self.contents_title.setText(_translate("MainWindow", "게시판 제목"))
        self.search_btn.setText(_translate("MainWindow", "검색"))
        self.reply_btn.setText(_translate("MainWindow", "댓글 달기"))
        self.write_contents_btn.setText(_translate("MainWindow", "글 작성하기"))
        self.chat_title.setText(_translate("MainWindow", "단체 채팅방"))
        self.chat_search_btn.setText(_translate("MainWindow", "검색"))
        self.chat_send_btn.setText(_translate("MainWindow", "댓글달기"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
