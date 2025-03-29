import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLineEdit,QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(100,100,400,300)
        self.line_edit=QLineEdit(self)
        self.entry_button=QPushButton("Submit",self)
        
        self.initUI()

    def initUI(self):
        self.line_edit.setPlaceholderText("Enter your name")
        self.line_edit.setGeometry(10,10,200,40)
        self.line_edit.setStyleSheet("font-size:20px;"
                                     "font-family:Arial;")
        self.entry_button.setGeometry(210,10,100,40)
        self.entry_button.setStyleSheet("font-size:15px;"
                                        "font-family:Arial;")
        
        self.entry_button.clicked.connect(self.submit)
        

    def submit(self):
        text=self.line_edit.text()
        print(f"Hello {text}")

       
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()