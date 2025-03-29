import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QCheckBox
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(100,200,500,500)
        self.checkBox=QCheckBox("Do you love me?",self)
        self.initUI()


    def initUI(self):
        self.checkBox.setGeometry(20,10,300,100)
        self.checkBox.setStyleSheet("font-size: 30px;""color: red;""background-color: pink;")
        self.checkBox.setChecked(False)
        self.checkBox.stateChanged.connect(self.checkbox_changed)

    def checkbox_changed(self,state):
        if state==2:
            print("You love me")
        else:
            print("You don't love me!")

        

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()