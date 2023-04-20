from PyQt5.QtWidgets import *  
from booking.booking import Booking


class Window(QWidget):
    def __init__(self):
        super().__init__()

        #username
        self.usernameLabel = QLabel(self)
        self.usernameLabel.setText('Please enter your PC Marc PlayByPoint username:')
        self.usernameLabel.move(50, 50)

        self.usernameText = QLineEdit(self)
        self.usernameText.move(50, 75)
        self.usernameText.resize(200, 25)

        #password
        self.passwordLabel = QLabel(self)
        self.passwordLabel.setText('Please enter your PC Marc PlayByPoint password:')
        self.passwordLabel.move(50, 125)

        self.passwordText = QLineEdit(self)
        self.passwordText.move(50, 150)
        self.passwordText.resize(200, 25)

        #weekday
        self.dayLabel = QLabel(self)
        self.dayLabel.setText('Please elect day of the week:')
        self.dayLabel.move(50, 200)

        self.dayComboBox = QComboBox(self)
        self.dayComboBox.addItems(['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'])
        self.dayComboBox.move(50, 225)
        self.dayComboBox.resize(200, 25)

        #sport
        self.sportLabel = QLabel(self)
        self.sportLabel.setText('Please select sport:')
        self.sportLabel.move(50, 275)

        self.sportComboBox = QComboBox(self)
        self.sportComboBox.addItems(['pickleball', 'tennis'])
        self.sportComboBox.move(50, 300)
        self.sportComboBox.resize(200, 25)

        #timeslot
        self.timeLabel = QLabel(self)
        self.timeLabel.setText('Please enter a 30min timeslot:')
        self.timeLabel.move(50, 350)

        self.timeComboBox = QComboBox(self)
        self.timeComboBox.addItems([
            '6-6:30am', '6:30-7am', '7-7:30am', '7:30-8am',
            '8-8:30am', '8:30-9am', '9-9:30am', '9:30-10am',
            '10-10:30am', '10:30-11am', '11-11:30am', '11:30-12pm',
            '12-12:30pm', '12:30-1pm', '1-1:30pm', '1:30-2pm',
            '2-2:30pm', '2:30-3pm', '3-3:30pm', '3:30-4pm',
            '4-4:30pm', '4:30-5pm', '5-5:30pm', '5:30-6pm',
            '6-6:30pm', '6:30-7pm', '7-7:30pm', '7:30-8pm',
            '8-8:30pm', '8:30-9pm', '9-9:30pm', '9:30-10pm'
            ])
        self.timeComboBox.move(50, 375)
        self.timeComboBox.resize(200, 25)

        #court
        self.courtLabel = QLabel(self)
        self.courtLabel.setText('Please select a court:')
        self.courtLabel.move(50, 425)

        self.courtComboBox = QComboBox(self)
        self.courtComboBox.addItems(['Pickleball 7A', 'Pickleball 7B', 'Pickleball 8A', 'Pickleball 8B', 'Pickleball 9A', 'Pickleball 9B'])
        self.courtComboBox.move(50, 450)
        self.courtComboBox.resize(200, 25)

        self.submitButton = QPushButton(self)
        self.submitButton.move(50, 500)
        self.submitButton.setText('Submit')
        self.submitButton.clicked.connect(self.submit)

        self.setGeometry(100, 100, 600, 600)
        self.show()


    def submit(self):
        username = self.usernameText.text()
        password = self.passwordText.text()
        weekday = self.dayComboBox.currentText()
        sport = self.sportComboBox.currentText()
        time = self.timeComboBox.currentText()
        court = self.courtComboBox.currentText()

        alert = QMessageBox()

        if not username or not password:
            print('missing username or password')
            return 0
        
        #runs booking bot code
        with Booking() as bot:
            bot.land_first_page()
            bot.login(username, password)
            bot.nav_to_booking_page()
            day = bot.weekday(weekday)
            status = bot.make_res(sport, day, time, court)

            alert.setText(status)
            alert.exec_()

if __name__ == '__main__':
    app = QApplication([])
    window = Window()
    app.exec_()





