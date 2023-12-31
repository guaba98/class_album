# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './UI/UI_category.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(160, 35)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.img_lab = QtWidgets.QLabel(self.frame)
        self.img_lab.setMinimumSize(QtCore.QSize(25, 25))
        self.img_lab.setMaximumSize(QtCore.QSize(25, 25))
        self.img_lab.setText("")
        self.img_lab.setPixmap(QtGui.QPixmap("./UI\\../img/ui_img/home.png"))
        self.img_lab.setScaledContents(True)
        self.img_lab.setObjectName("img_lab")
        self.horizontalLayout.addWidget(self.img_lab)
        spacerItem1 = QtWidgets.QSpacerItem(10, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.name_lab = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("나눔스퀘어 네오 Bold")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.name_lab.setFont(font)
        self.name_lab.setStyleSheet("color: rgb(255, 255, 255);")
        self.name_lab.setObjectName("name_lab")
        self.horizontalLayout.addWidget(self.name_lab)
        self.horizontalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.name_lab.setText(_translate("Form", "카테고리이름"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
