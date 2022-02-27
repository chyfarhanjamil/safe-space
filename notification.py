import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QStackedWidget, QWidget
 
class middlwWindow(QDialog):
 
    def __init__(self):
        super(middlwWindow,self).__init__()
        loadUi("email.ui",self)
        #self.enterEmail.clicked.connect(self.gotoEmail)
 
        self.confirm.clicked.connect(self.savingFunction)
        self.back.clicked.connect(self.returnFunction)
 
    def savingFunction(self):
 
        email=self.emailField.text()
        if len(email)==0:
            self.error.setText("You must input valid address")
    
 
 
        else:
 
            self.emailField.setText("")
            print(email)
            file=open("email.txt","a+")
            file.write(email+"\n")
            file.close()
            print("you subscribed to notification service successfully!")
    
    def returnFunction(self):
        self.close()
        widget.close()
 
 
 
app=QApplication(sys.argv)
middle=middlwWindow()
widget=QStackedWidget()
widget.addWidget(middle)
widget.setFixedHeight(602)
widget.setFixedWidth(902)
widget.show()
try:
 
    sys.exit(app.exec_())
except:
    print("Exiting")
