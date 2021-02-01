import sys
import time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from TodayStores import TodayStores

class ChooseDate(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.resize(500,300)
        self.setWindowTitle("Choose date and time")

        self.dateinput = QLabel(self)
        self.dateinput.setText("Please Enter Date (DD/MM/YYYY): ")
        self.timeinput = QLabel(self)
        self.timeinput.setText("Please Enter Time (HH:MM): ")
        self.datebox = QLineEdit(self)
        self.timebox = QLineEdit(self)
        self.timebox.setPlaceholderText('24 hour format')
        self.dateinput.move(20, 20)
        self.dateinput.resize(250, 20)
        self.datebox.move(270, 20)
        self.datebox.resize(150, 20)
        self.timeinput.move(20, 60)
        self.timeinput.resize(250, 60)
        self.timebox.move(270, 80)
        self.timebox.resize(150, 20)

        self.enter = QPushButton("Enter", self)
        self.enter.move(270, 150)
        self.enter.resize(150, 25)
        self.enter.clicked.connect(self.on_click)

    def show_stall_list(self):
        from TodayStores import TodayStores
        self.w = TodayStores()
        self.w.show()
        self.close()

    def on_click(self):  # function to validate format of input date and time and to ensure users do not enter date/time
        try:  # which is in the past. It allows user to re-enter until a correct input is achieved
            global datetime  # this variable will also be used in function StallList() class
            datetime = QDateTime.fromString(self.datebox.text() + ' ' + self.timebox.text(), "dd/MM/yyyy hh:mm")
            date_check = time.mktime(time.strptime(self.datebox.text(), '%d/%m/%Y'))  # }
            time_check_hr = int(self.timebox.text()[:2])  # }
            time_check_min = int(self.timebox.text()[3:])  # } computation of input date and time
            time_check = (time_check_hr * 3600) + (time_check_min * 60)  # } in seconds
            check = date_check + time_check  # }
            if (check < time.time()):  # compare input date and time with current system date and time in seconds
                msg = QMessageBox()  # message box to alert user that date/time entered is in the past
                msg.setText("Please enter a future date and time")
                msg.setWindowTitle("Date error message")
                msg.setIcon(QMessageBox.Warning)
                msg.setStandardButtons(QMessageBox.Ok)
                msg.exec()
            else:
                self.show_stall_list()
        except ValueError:
            msg = QMessageBox()  # message box to alert user that date/time entered is incorrect
            msg.setText("Error: Date/Time format invalid")
            msg.setWindowTitle("Date error message")
            msg.setIcon(QMessageBox.Critical)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()



