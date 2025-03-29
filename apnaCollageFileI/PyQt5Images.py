import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QLabel
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(700,300,500,500)

        lable=QLabel(self)
        lable.setGeometry(0,0,250,250)

        pixmap=QPixmap("my_icon.jpg")
        lable.setPixmap(pixmap)
        lable.setScaledContents(True)
        lable.setGeometry(self.width()-lable.width() ,
                          (self.height()-lable.height()),
                          lable.width(),
                          lable.height())
        
    
def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

