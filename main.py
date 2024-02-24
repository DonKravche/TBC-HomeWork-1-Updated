import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtWidgets import QMainWindow

from UI_MainWindow import Ui_MainWindow


def Email_Input_MessageBox_Error():
    eMail_messageBox = QMessageBox()
    eMail_messageBox.setText("Invalid E-Mail Address")
    eMail_messageBox.setWindowTitle("E-mail Error")
    eMail_messageBox.setIcon(QMessageBox.Warning)
    eMail_messageBox.exec()


def Password_Input_MessageBox_Error():
    password_messageBox = QMessageBox()
    password_messageBox.setText("Invalid Password")
    password_messageBox.setWindowTitle("Password Error")
    password_messageBox.setIcon(QMessageBox.Warning)
    password_messageBox.exec()


def Password_Dont_Much_MessageBox_Error():
    password_messageBox = QMessageBox()
    password_messageBox.setText("Invalid Passwords")
    password_messageBox.setWindowTitle("Password Dont much Error")
    password_messageBox.setIcon(QMessageBox.Warning)
    password_messageBox.exec()


def Registration_Complete_MessageBox():
    password_messageBox = QMessageBox()
    password_messageBox.setText("You Successfully Registered")
    password_messageBox.setWindowTitle("Registration Complete")
    password_messageBox.setIcon(QMessageBox.Information)
    password_messageBox.exec()


def Log_In_Fail_MessageBox():
    logIn_messageBox = QMessageBox()
    logIn_messageBox.setText("Invalid eMail or Password")
    logIn_messageBox.setWindowTitle("Log In Error")
    logIn_messageBox.setIcon(QMessageBox.Information)
    logIn_messageBox.exec()


class MyWindow:
    def __init__(self):
        self.window = QMainWindow()
        self.initUI = Ui_MainWindow()
        self.initUI.setupUi(self.window)

        # Log In Page
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Log_In_Page)

        # Move To The Register Page
        self.initUI.Create_Account.clicked.connect(self.Log_In_Create_Account_Button_Clicker)

        # Move Back To The Register Page
        self.initUI.Return_Log_In_Button.clicked.connect(self.Return_Log_in_Clicker)

        # Connect Register button to registration function
        self.initUI.Register_Button.clicked.connect(self.Register_Account_Function)

        # Connect Log In button to log in function
        self.initUI.Log_In_Button.clicked.connect(self.Log_In_Button_Clicker_User_Page)

        # Connect us From User Page to Log In
        self.initUI.Log_Out_Button.clicked.connect(self.Log_Out_And_Go_Log_In_page)

        # Variables to store authorization information
        self.email = ""
        self.password = ""

    def show(self):  # This Function Display us Window
        self.window.show()

    def Log_In_Create_Account_Button_Clicker(self):  # This Function Help us to move to the Create Account Page
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Create_Account_Page)

    def Return_Log_in_Clicker(self):  # This Function Help us to move back to the Log_In page
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Log_In_Page)

    def Log_In_Button_Clicker_User_Page(self):  # This Function Help us to move User Page
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.User_Page)

    def Log_Out_And_Go_Log_In_page(self):
        self.initUI.stackedWidget.setCurrentWidget(self.initUI.Log_In_Page)

    def Register_Account_Function(self):  # Registration Account
        Email_Input = self.initUI.Email_Register.text()
        Password_Input = self.initUI.Password_Register.text()
        Re_Enter_Password_Input = self.initUI.Re_Enter_Password_Register.text()

        if len(Email_Input) <= 3 or '@' not in Email_Input:
            Email_Input_MessageBox_Error()
        elif len(Password_Input) <= 3:
            Password_Input_MessageBox_Error()
        elif Password_Input != Re_Enter_Password_Input:
            Password_Dont_Much_MessageBox_Error()
        else:
            Registration_Complete_MessageBox()

            # Store authorization information
            self.email = Email_Input
            self.password = Password_Input
            Registration_Complete_MessageBox()

    def Log_In_Function(self):  # Log In
        Entered_Email = self.initUI.Log_in_Email.text()
        Entered_Password = self.initUI.Log_in_Password.text()

        # Check if the entered email and password match the stored ones

        if Entered_Email == self.email and Entered_Password == self.password:
            self.initUI.Log_In_Button.clicked.connect(self.Log_In_Button_Clicker_User_Page)
        else:
            Log_In_Fail_MessageBox()


if __name__ == '__main__':
    application = QApplication(sys.argv)
    window = MyWindow()

    window.show()
    sys.exit(application.exec_())
