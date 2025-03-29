import sys
from PyQt5.QtWidgets import QApplication, QMainWindow,QPushButton,QHBoxLayout,QWidget


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My first cool GUI")
        self.button1=QPushButton("One")
        self.button2=QPushButton("Two")
        self.button3=QPushButton("Three")

        self.initUI()
       
    def initUI(self):
        centeral_widget=QWidget()
        self.setCentralWidget(centeral_widget)

        hbox=QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        centeral_widget.setLayout(hbox)
        self.button1.setObjectName("a")
        self.button2.setObjectName("b")
        self.button3.setObjectName("c")

        self.setStyleSheet("""
                QPushButton{
                           font-size:20px;
                           color:white;
                           margin:25px;}
                QPushButton#a{
                           background-color:blue;
                           }
                    QPushButton#b
                           {
                           background-color:red;}
              QPushButton#c
                           {
                           color:red;
                           background-color:purple;}
                             
        """)

        

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()