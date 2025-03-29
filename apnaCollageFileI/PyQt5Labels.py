import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.setGeometry(100,200,500,500)
        label=QLabel("Hello world",self)
        label.setFont(QFont("Arial",30))
        label.setGeometry(0,0,500,500)
        label.setStyleSheet("color: blue;"
                            "background-color: purple;"
                            "font-weight: bold;"
                            "text-decoration: underline;")
        

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()