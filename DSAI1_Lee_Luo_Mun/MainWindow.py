import sys
import pickle
import time

from PyQt5 import QtGui

import store_database
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from TodayStores import TodayStores
from ChooseDate import ChooseDate


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.resize(1000, 800)
        self.setWindowTitle("NTU Menu")
        self.setWindowIcon(QIcon('ntu_logo.png'))

        self.back_g = QLabel(self)
        self.pixmap = QPixmap('main_bg.jpg')
        self.back_g.setPixmap(self.pixmap)

        self.view_btn = QPushButton("View Today's Stores",self)
        self.view_btn.setFont(QFont('Century Gothic',11))
        self.view_btn.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                    "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                    "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
        self.view_btn.resize(250,45)
        self.view_btn.move(50,500)

        self.choose_btn = QPushButton("View Stores by Other Dates",self)
        self.choose_btn.setFont(QFont('Century Gothic', 11))
        self.choose_btn.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                      "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                      "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
        self.choose_btn.resize(250,45)
        self.choose_btn.move(50,550)

        self.exitBtn = QPushButton("Exit", self)
        self.exitBtn.setFont(QFont('Century Gothic', 11))
        self.exitBtn.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                   "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                   "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
        self.exitBtn.resize(250, 45)
        self.exitBtn.move(50, 600)

        global datetime
        datetime = QDateTime.currentDateTime()
        self.now_time = QLabel(datetime.toString('dddd, dd MMMM yyyy h:mm'),self)  #display current date and time
        self.now_time.setFont(QFont('Century Gothic',16))
        self.now_time.resize(400,40)
        self.now_time.move(50,350)

        self.view_btn.clicked.connect(self.openTodayStores)
        self.choose_btn.clicked.connect(self.openChooseDate)
        self.exitBtn.clicked.connect(self.exit_sys)

        self.window2_1 = TodayStores()
        self.window2_2 = ChooseDate()

    def openTodayStores(self):
        self.window2_1.show()
        self.hide()

    def openChooseDate(self):
        self.window2_2.show()

    def exit_sys(self):
        self.close()

    def back_to_main_window(self):
        TodayStores().back_to_main_window()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWin = MainWindow()
    MainWin.show()
    sys.exit(app.exec_())