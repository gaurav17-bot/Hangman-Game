import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QLabel

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(500,300,300,300)
        self.button=QPushButton("Click Me!",self)
        self.label=QLabel("Hello",self)
        self.initUI()

    def initUI(self):
        self.button.setGeometry(100,100,150,100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.on_click)
        self.label.setGeometry(160,160,500,100)
        self.label.setStyleSheet("font-size:30px;")
    
    def on_click(self):
        print("Button Clicked")
        self.button.setText("Clicked")
        
        self.label.setText("Good byee")
        

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()