import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget
from PyQt5.uic import loadUi
from plyer import notification

title="Warning"
message="Username or Password is wrong"

class Login(QDialog):
    def __init__(self):
        super(Login,self).__init__()
        loadUi("login.ui",self)
        self.loginbutton.clicked.connect(self.loginfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.createaccbutton.clicked.connect(self.gotocreate)
        
        

    def loginfunction(self):
        email=self.email.text()
        password=self.password.text()
       # print("Successfully logged in with email: ", email, "and password:", password)
        if(email=="admin" and password=="admin"):
            widget.close()
        else:
            notification.notify(
            title=title,
            message=message,
            app_icon=None,
            timeout=10,
            toast=False
        )
       # import main
        

    def gotocreate(self):
        createacc=CreateAcc()
        widget.addWidget(createacc)
        widget.setCurrentIndex(widget.currentIndex()+1)
        self.close()

class CreateAcc(QDialog):
    def __init__(self):
        super(CreateAcc,self).__init__()
        loadUi("createacc.ui",self)
        self.signupbutton.clicked.connect(self.createaccfunction)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirmpass.setEchoMode(QtWidgets.QLineEdit.Password)

    def createaccfunction(self):
        email = self.email.text()
        if self.password.text()==self.confirmpass.text():
            password=self.password.text()
            print("Successfully created acc with email: ", email, "and password: ", password)
            login=Login()
            widget.addWidget(login)
            widget.setCurrentIndex(widget.currentIndex()+1)


app=QApplication(sys.argv)
mainwindow=Login()
widget=QtWidgets.QStackedWidget()
widget.addWidget(mainwindow)
widget.setFixedWidth(480)
widget.setFixedHeight(620)
widget.show()
app.exec_()