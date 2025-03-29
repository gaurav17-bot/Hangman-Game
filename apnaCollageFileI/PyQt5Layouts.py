import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow,QLabel,QWidget,
                             QVBoxLayout,QHBoxLayout,QGridLayout)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(500,300,300,300)
        self.initUI()
    
    def initUI(self):
        central_widget=QWidget()
        self.setCentralWidget(central_widget)

        label1=QLabel("One",self)
        label2=QLabel("two",self)
        label3=QLabel("Three",self)
        label4=QLabel("Four",self)
        label5=QLabel("Five",self)

        label1.setStyleSheet("background-color: blue;")
        label2.setStyleSheet("background-color: red;")
        label3.setStyleSheet("background-color: pink;")
        label4.setStyleSheet("background-color: green;")
        label5.setStyleSheet("background-color: grey;")



        ##### to arrange vertically
        # vbox=QVBoxLayout()
        # vbox.addWidget(label1)
        # vbox.addWidget(label2)
        # vbox.addWidget(label3)
        # vbox.addWidget(label4)
        # vbox.addWidget(label5)

        ####### to arrange horizontally
        
        # hbox=QHBoxLayout()
        # hbox.addWidget(label1)
        # hbox.addWidget(label2)
        # hbox.addWidget(label3)
        # hbox.addWidget(label4)
        # hbox.addWidget(label5)


        ### to arrange in given index#####

        grid=QGridLayout()
        grid.addWidget(label1,0,0)
        grid.addWidget(label2,1,1)
        grid.addWidget(label3,2,2)
        grid.addWidget(label4,3,3)
        grid.addWidget(label5,4,4)



        central_widget.setLayout(grid)


     

def main():
    app=QApplication(sys.argv)
    window=MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__=="__main__":
    main()