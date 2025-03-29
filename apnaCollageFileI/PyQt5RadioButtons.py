import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QRadioButton,QButtonGroup,QLabel
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.label=QLabel("Payment method: ",self)
        self.label1=QLabel("Payment mode: ",self)
        self.radio1=QRadioButton("Visa",self)
        self.radio2=QRadioButton("Credit Card",self)
        self.radio3=QRadioButton("Gift Card",self)   
        self.radio4=QRadioButton("In-store",self)
        self.radio5=QRadioButton("Online",self)
        self.button_group1=QButtonGroup(self)
        self.button_group2=QButtonGroup(self)
        self.setGeometry(100,100,500,500)
        self.initUI()
    
    def initUI(self):
        self.label.setGeometry(0,0,300,50)
        self.label1.setGeometry(0,200,300,50)
        
        self.radio1.setGeometry(0,50,300,50)
        self.radio2.setGeometry(0,100,300,50)
        self.radio3.setGeometry(0,150,300,50)
        
        self.radio4.setGeometry(0,250,300,50)
        self.radio5.setGeometry(0,300,300,50)

        self.label.setStyleSheet("font-size:30px;")
        self.label1.setStyleSheet("font-size:30px;")
        
        self.setStyleSheet("QRadioButton{""font-size:30px;"  #stylling whole buttons at atime
                           "color: red;"
                           "padding:10px;""}")
        
        self.button_group1.addButton(self.radio1)
        self.button_group1.addButton(self.radio2)
        self.button_group1.addButton(self.radio3)
        self.button_group2.addButton(self.radio4)
        self.button_group2.addButton(self.radio5)

        self.radio1.toggled.connect(self.radioButton_checked)
        self.radio2.toggled.connect(self.radioButton_checked)
        self.radio3.toggled.connect(self.radioButton_checked)
        self.radio4.toggled.connect(self.radioButton_checked)
        self.radio5.toggled.connect(self.radioButton_checked)

    
    def radioButton_checked(self):
        radio_button=self.sender()
        if radio_button.isChecked():
            print(f"{radio_button.text()} is selected")

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()