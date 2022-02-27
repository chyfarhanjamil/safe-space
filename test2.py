import sys
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
 
 
 
class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(450, 550)
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(10, 10, 431, 531))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 140, 360, 360))
      #  self.label.setStyleSheet(u"background-image: url(:/image/pngtree-user-login-or-authenticate-icon-on-gray-background-flat-icon-ve-png-image_1786166.jpg);")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(-10, 50, 451, 71))
        font = QFont()
        font.setFamily(u"Segoe UI")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(50, 250, 311, 41))
        font1 = QFont()
        font1.setPointSize(17)
        self.lineEdit.setFont(font1)
        self.lineEdit.setAutoFillBackground(False)
        self.lineEdit.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"")
        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(50, 340, 311, 41))
        self.lineEdit_2.setFont(font1)
        self.lineEdit_2.setAutoFillBackground(False)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(244, 244, 244);\n"
"border:none;\n"
"border-bottom:2px solid rgba(105,118,132,255);\n"
"color: rgb(0, 0, 0);\n"
"padding-bottom:7px;\n"
"\n"
"\n"
"")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(50, 450, 311, 51))
        font2 = QFont()
        font2.setPointSize(18)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"QPushButton#pushButton{\n"
"	border-radius:20px;\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-width:15px;\n"
"	\n"
"	\n"
"	background-color: rgb(150, 225, 225);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:hover{\n"
"	border-radius:20px;\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-width:15px;\n"
"	\n"
"	\n"
"	\n"
"	\n"
"	background-color: rgb(133, 199, 199);\n"
"\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed{\n"
"	border-radius:20px;\n"
"	\n"
"	border-color: rgb(255, 255, 255);\n"
"	border-width:15px;\n"
"	\n"
"	\n"
"	background-color: rgb(150, 225, 225);\n"
"\n"
"	padding-left:5px;\n"
"	padding-top:5px;\n"
"\n"
"}")
 
        self.retranslateUi(Form)
    
        QMetaObject.connectSlotsByName(Form)
    # setupUi
 
    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Log In", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Form", u"  Username", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u"  Password", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Log In", None))
    # retranslateUi
 
if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    Form=QtWidgets.QWidget()
    ui=Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())