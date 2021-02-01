from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import pickle
import store_database
d = store_database.d

class TodayStores(QWidget):
    def __init__(self):
        super().__init__()
        self.set_ui()

    def set_ui(self):
        self.setWindowTitle("Today's Stores")
        self.resize(350,400)

        self.back_g = QLabel(self)
        self.pixmap = QPixmap('TSbg.jpg')
        self.back_g.setPixmap(self.pixmap)

        font = QFont('Century Gothic',12)
        font.setBold(True)

        self.titleLbl = QLabel("Please select a store:", self)
        self.titleLbl.setFont(font)
        self.titleLbl.resize(250, 50)
        self.titleLbl.move(90,60)

        global datetime
        datetime = QDateTime.currentDateTime()

        self.timeLbl = QLabel((datetime.toString("dddd,dd MMMM yyyy hh:mm")), self)  # display current  system date/time
        self.timeLbl.setFont(font)
        self.timeLbl.resize(300, 50)  # or user's defined date/time
        self.timeLbl.move(40,100)

        day_now = datetime.toString("dddd")  # string operation to obtain day(eg. Monday) of current date or input date
        time_now = int(datetime.toString("hmm"))  # string operation to obtain time(eg. 1030) of current or inputted time
        # convert string to integer for comparison purpose

        lst_of_stall = []
        count_op_stall = 0
        for key, value in d.items():
            op_start_time = value[0]
            op_end_time = value[1]
            op_stall = key[0]
            if (key[1] == day_now) and (op_start_time <= time_now <= op_end_time):  # compare the day and time with
                count_op_stall += 1  # the stalls' operating days and times in the 'stalls operating hour "
                lst_of_stall.append(op_stall)  # dictionary and append name of opening stalls in a list
        if count_op_stall == 0:
            self.stallLbl = QLabel(("Sorry,all the stores are closed!"), self)
            self.stallLbl.setFont(font)

        else:
            for stall in lst_of_stall:  # a loop to create buttons for all the opening stalls
                self.stallBtn = QPushButton(stall, self)
                self.stallBtn.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                           "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                           "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
                self.stallBtn.setFont(QFont("Century Gothic",11))
                self.stallBtn.move(75,(count_op_stall+1)*30)
                self.stallBtn.resize(200,28)
                count_op_stall +=1
                global stallName  # this variable is used to get the text on each QPushButtons and then used in
                stallName = self.stallBtn.text()  # StallMenu() class to display the stall menu
                self.stallBtn.clicked.connect(self.show_stall_menu)

        self.backBtn = QPushButton("Back to main menu", self)
        self.backBtn.setFont(font)
        self.backBtn.resize(350,35)
        self.backBtn.move(0,365)
        self.backBtn.clicked.connect(self.back_to_main_window)

    def back_to_main_window(self):
        from MainWindow import MainWindow
        self.mainWin = MainWindow()
        self.mainWin.show()
        self.hide()

    def show_stall_menu(self):
        global stallName
        stallName =self.sender().text()
        self.window3 = StallMenu()
        self.window3.show()
        self.hide()


class StallMenu(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.set_up_ui()
        self.retrieve_menu()


    def set_up_ui(self):
        self.setWindowTitle("NTU Canteen: Stall Menu")
        self.resize(1000, 740)
        self.back_g1 = QLabel(self)
        self.pixmap = QPixmap('bg3.jpg')
        self.back_g1.setPixmap(self.pixmap)

        self.menuLb = QLabel(self)
        self.priceLb = QLabel(self)
        self.stlname = QLabel(self)


        self.op_hr = QPushButton("Operating Hours", self)
        self.op_hr.setFont(QFont("Century Gothic",12))
        self.op_hr.move(700,200)
        self.op_hr.resize(170,30)
        self.op_hr.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                 "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                 "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
        self.op_hr.clicked.connect(self.show_op_hour)

        self.calWt = QPushButton("Calculate Wait Time",self)
        self.calWt.setFont(QFont("Century Gothic",12))
        self.calWt.move(500,200)
        self.calWt.resize(170,30)
        self.calWt.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                 "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                 "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
        self.calWt.clicked.connect(self.cal_wait_time)

        self.backb = QPushButton("Back to the Main Screen", self)
        self.backb.setFont(QFont("Century Gothic",15))
        self.backb.resize(1000,40)
        self.backb.move(0,700)
        self.backb.clicked.connect(self.back_to_mainwin)

        self.backm = QPushButton("Back to the Previous Screen", self)
        self.backm.setFont(QFont("Century Gothic", 15))
        self.backm.resize(1000, 40)
        self.backm.move(0,660)
        self.backm.clicked.connect(self.back_to_win2)

        if stallName == 'Indian Cuisine':
            self.indian = QLabel(self)
            indian_picture = QPixmap('indianicon.jpg')
            self.indian.setPixmap(indian_picture)
            self.indian.move(100,200)
        elif stallName == 'VinFood Western':
            self.western = QLabel(self)
            western_picture = QPixmap('westernicon.jpg')
            self.western.setPixmap(western_picture)
            self.western.move(100, 200)
        elif stallName == 'Mini Wok':
            self.wok = QLabel(self)
            wok_picture = QPixmap('wokicon.jpg')
            self.wok.setPixmap(wok_picture)
            self.wok.move(100, 200)
        elif stallName == 'Malay BBQ':
            self.bbq = QLabel(self)
            bbq_picture = QPixmap('bbq.jpg')
            self.bbq.setPixmap(bbq_picture)
            self.bbq.move(100, 200)
        else:
            self.huat = QLabel(self)
            huat_picture = QPixmap('huat.jpg')
            self.huat.setPixmap(huat_picture)
            self.huat.move(150, 250)

    def retrieve_menu(self):  # open pickler file which store all the menus for different stalls in their respective dictionaries
        aFile = open('backup.out', 'rb')
        self.dict_ic = pickle.load(aFile)
        self.dict_vw = pickle.load(aFile)
        self.dict_mw = pickle.load(aFile)
        self.dict_mbbq = pickle.load(aFile)
        self.dict_huat = pickle.load(aFile)
        aFile.close()

        day_now = datetime.toString("dddd")  # string operation to obtain day(eg. Monday) of current date or input date
        time_now = int(
            datetime.toString("hmm"))  # string operation to obtain time(eg. 1030) of current or inputted time
        # convert string to integer for comparison purpose

        lst_stall = ["Indian Cuisine", "VinFood Western", "Mini Wok", "Malay BBQ", "Huat Beverage"]
        lst_dict = [self.dict_ic, self.dict_vw, self.dict_mw, self.dict_mbbq, self.dict_huat]

        for i in lst_stall:
            if stallName == i:  # stallName obtained from StallList() class
                self.stlname.setText(i)
                self.stlname.move(300,50)
                self.stlname.setFont(QFont("Cream Peach",50))
                stallindex = lst_stall.index(i)
                dict_name = lst_dict[stallindex]
                for key, value in dict_name.items():
                    starttime = value[0]
                    endtime = value[1]
                    if day_now == key[1] and (starttime <= time_now <= endtime):  # based on the day and time, display the stall
                        self.menuLb.setText(key[2])  # menu according to its operating time
                        self.menuLb.move(400,250)
                        self.priceLb.setText(key[3])
                        self.priceLb.move(730,250)
                        self.menuLb.setFont(QFont("Ink Free",20))
                        self.priceLb.setFont(QFont("Ink Free",20))
                        self.update()

    def back_to_mainwin(self):
        from MainWindow import MainWindow
        self.mainWin = MainWindow()
        self.mainWin.show()
        self.hide()

    def back_to_win2(self):
        self.win2 = TodayStores()
        self.win2.show()
        self.hide()

    def show_op_hour(self):  # Dialog box to display operating hour for the stall
        opHourDlg = QDialog()
        opHourDlg.setMinimumWidth(480)
        opHourDlg.setWindowTitle("Operating Hour for " + stallName)
        opHourDlg.setWindowModality(Qt.ApplicationModal)

        vbox = QVBoxLayout()
        vbox.setAlignment(Qt.AlignCenter)

        op_days = []
        for store_day, op_time in d.items():  # go through the "stall operating hour" dictionary and store the opening
            op_start = op_time[0]  # days and times of the stall in a list then display them in the dialog window
            op_end = op_time[1]
            day = store_day[1]
            if (store_day[0] == stallName):
                op_days.append((day, op_start, op_end))
        for day in op_days:
            dayLbl = QLabel(day[0])
            if day[1] == 0:
                timeLbl=QLabel("Closed")
            else:
                self.day1_text = str(day[1])
                self.day2_text = str(day[2])
                timeday1 = QDateTime.fromString(self.day1_text,"hmm")  # convert time from 24-hour clock format to am/pm format
                timeday2 = QDateTime.fromString(self.day2_text, "hhmm")
                timeLbl = QLabel(timeday1.toString("h:mm ap") + " - " + timeday2.toString("h:mm ap"))
            hbox = QHBoxLayout()
            hbox.addWidget(dayLbl)
            hbox.addWidget(timeLbl)
            vbox.addLayout(hbox)
        okBtn = QPushButton("Ok", self)
        vbox.addWidget(okBtn)
        opHourDlg.setLayout(vbox)
        okBtn.clicked.connect(opHourDlg.close)
        opHourDlg.exec()

    def cal_wait_time(self):
        self.win3 = QueueTime()
        self.win3.show()


class QueueTime(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setWindowTitle("Calculate Wait Time")
        self.resize(300,150)

        self.queueLbl = QLabel("Enter number of people in queue", self)  # allow user to input no. of people queuing
        self.queueLbl.setFont(QFont("Century Gothic",12))
        self.queueLbl.move(20,20)
        self.numPaxLe = QLineEdit(self)
        self.numPaxLe.resize(200,25)
        self.numPaxLe.move(50,50)
        self.calBtn = QPushButton("Calculate waiting time",self)
        self.calBtn.setStyleSheet("QPushButton{border-image: url(ui/button.png)}"
                                 "QPushButton:hover{border-image: url(ui/button_hover.png)}"
                                 "QPushButton:pressed{border-image: url(ui/button_clicked.png)}")
        self.calBtn.setFont(QFont("Century Gothic", 12))
        self.calBtn.resize(200,25)
        self.calBtn.move(50,80)
        self.calBtn.clicked.connect(self.calculate_wait_time)



    def calculate_wait_time(self):
        if self.numPaxLe.text().isdigit():  # validatation to ensure that user input a digit, allow user
            numpax = int(self.numPaxLe.text())  # to re-enter until a correct input is achieved
            stall_info = d[(stallName, "Monday")]  # to obtain the waiting time per person from the "stall
            wait_time = int(stall_info[2]) * numpax  # operating hour" dictionary
            msg = QMessageBox()  # message box to display est. waiting time for the stall
            msg.setText("Estimated waiting time is: " + str(wait_time) + " minutes")
            msg.setWindowTitle("Waiting time info")
            msg.setIcon(QMessageBox.Information)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
        else:
            msg = QMessageBox()  # message box to alert user that input is invalid
            msg.setText("Please enter a valid number")
            msg.setWindowTitle("Error")
            msg.setIcon(QMessageBox.Warning)
            msg.setStandardButtons(QMessageBox.Ok)
            msg.exec()
