import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import webbrowser
from PyQt5.QtCore import pyqtSlot
import PyQt5
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
import sys
import os
import subprocess
from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QIcon, QPixmap
from easygui import *
import PySimpleGUI as sg           
import os
import time              
import json
from PyQt5 import QtCore, QtWidgets

account1 = open("C:\\Users\\Public\\.account\\.username.bin", "r")
account_ = account1.read()
print(account_)
account1.close()
account2 = open("C:\\Users\\Public\\.account\\.password.bin", "r")
account_p = account2.read()
print(account_p)
account2.close()
account3 = open("C:\\Users\\Public\\.account\\1-2-1.bin", "r")
account_pin = account3.read()
account3.close()

class MainWindow(QMainWindow):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = "Sign in"
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 700
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon("Q:/Documents/Python/Projects/Sign-in Page/.media/icon.ico"))
        self.textbox1 = QLineEdit(self)
        self.textbox1.move(350, 300)
        self.textbox1.resize(300,40)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(350, 400)
        self.textbox2.resize(300,40)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(350, 510)
        self.textbox3.resize(70,40)
        info_0 = QLabel("Create New Account", self)
        info_0.move(385,200)
        info_0.resize(800,30)
        info_0.setStyleSheet("color: solid black;") 
        info_0.setFont(QFont("Arial Bold", 14))  
        info_1 = QLabel("Enter Name or Email!", self)
        info_1.resize(450,30)
        info_1.move(355,250)
        info_1.setStyleSheet("color: blue;")
        info_r = QLabel(" Remember This is your account Recover Pin,\n If your Forget this 'pin' No Ideas! Your Will Lost You Account...", self)
        info_r.resize(8000,30)
        info_r.move(340,460)
        info_r.setStyleSheet("color: red;")
        info_2 = QLabel("Enter Your Password!", self)
        info_2.resize(450,30)
        info_2.move(355,350)
        info_2.setStyleSheet("color: blue;")
        button = QPushButton("Create", self)
        button.setStyleSheet("background-color : blue; border-radius : 50; color: white;")
        button.move(550,515)
        button.clicked.connect(self.switch)
        self.show()

    # @pyqtSlot()
    def switch(self):
        textboxValue1 = self.textbox1.text().lower()
        textboxValue2 = self.textbox2.text().lower()
        textboxValue3 = self.textbox3.text().lower()
        save_info = open("C:\\Users\\Public\\.account\\.username.bin", "w")
        save_info.write(textboxValue1)
        save_info.close()
        save_info_p = open("C:\\Users\\Public\\.account\\.password.bin", "w")
        save_info_p.write(textboxValue2)
        save_info_p.close()
        save_info_v = open("C:\\Users\\Public\\.account\\1-2-1.bin", "w")
        save_info_v.write(textboxValue3)
        save_info_v.close()
        print("action done!")
        self.switch_window.emit()

class WindowTwo(QMainWindow, QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = "Sign in"
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 700
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon("Q:\\Documents\\Python Projects\\Sign-in Page\\.media\\d8d47af9059b6b3f12e47ea6014c966d.ico"))
        self.textbox = QLineEdit(self)
        self.textbox.move(350, 250)
        self.textbox.resize(300,40)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(350, 400)
        self.textbox2.resize(300,40)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(660, 400)
        self.textbox3.resize(70,40)
        self.button = QPushButton("Forgot Account?", self)
        self.button.setStyleSheet("border-radius : 50; color: blue;") 
        self.button.resize(200,30)
        self.button.move(282,335)
        self.button.clicked.connect(self.on_click)
        info_0 = QLabel("Login in", self)
        info_0.move(455,165)
        info_0.setStyleSheet("color: solid black;") 
        info_0.setFont(QFont("Arial Bold", 14)) 
        info_e = QLabel("Enter Name or Email!", self)
        info_e.resize(450,30)
        info_e.move(350,220)
        info_e.setStyleSheet("color: blue;") 
        info_1 = QLabel("Forget your name or password?. if it is right click forgot account", self)
        info_1.resize(450,30)
        info_1.move(335,300)
        info_1.setStyleSheet("color: grey;")
        info_p = QLabel("Enter Password or Pin", self)
        info_p.resize(450,30)
        info_p.move(350,365)
        info_p.setStyleSheet("color: blue;") 
        button = QPushButton("Next", self)
        button.setStyleSheet("background-color : blue; border-radius : 50; color: white;")
        button.move(550,470)
        button.clicked.connect(self.on_click_sign_in)
        self.show()

    @pyqtSlot()
    def on_click(self):
        webbrowser.open("http://3.bp.blogspot.com/-And5mt9-gnc/VDXwjWFWJaI/AAAAAAAACxo/VwrbjonLwgs/s1600/EnterPin.jpg")

    @pyqtSlot()
    def on_click_sign_in(self):
        while True:
            textboxValue = self.textbox.text().lower()
            if account_ in textboxValue:                        
                print("1-1")
                break  
            else:
                print("0-1")
                break
        while True:
            textboxValue2 = self.textbox2.text().lower()
            if account_p in textboxValue2:
                print("2-1")
                break
            else:
                print("2-0")
                break
        while True:
            textboxValue3 = self.textbox3.text().lower()
            if account_pin in textboxValue3:
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl("http://www.netanimations.net/april-fools-day-005.gif"))
                self.setCentralWidget(self.browser)
                print("hello world")
                break
            else:
                exit()

class Login(QMainWindow, QWidget):

    switch_window = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.title = "Sign in"
        self.left = 100
        self.top = 100
        self.width = 1000
        self.height = 700
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.setStyleSheet("background-color: white;")
        self.setWindowIcon(QIcon("Q:\\Documents\\Python Projects\\Sign-in Page\\.media\\d8d47af9059b6b3f12e47ea6014c966d.ico"))
        self.textbox = QLineEdit(self)
        self.textbox.move(350, 250)
        self.textbox.resize(300,40)
        self.textbox2 = QLineEdit(self)
        self.textbox2.move(350, 400)
        self.textbox2.resize(300,40)
        self.textbox3 = QLineEdit(self)
        self.textbox3.move(660, 400)
        self.textbox3.resize(70,40)
        self.button = QPushButton("Forgot Account?", self)
        self.button.setStyleSheet("border-radius : 50; color: blue;") 
        self.button.resize(200,30)
        self.button.move(282,335)
        self.button.clicked.connect(self.on_click)
        info_0 = QLabel("Sign in", self)
        info_0.move(455,165)
        info_0.setStyleSheet("color: solid black;") 
        info_0.setFont(QFont("Arial Bold", 14)) 
        info_e = QLabel("Enter Name or Email!", self)
        info_e.resize(450,30)
        info_e.move(350,220)
        info_e.setStyleSheet("color: blue;") 
        info_1 = QLabel("Forget your name or password?. if it is right click forgot account", self)
        info_1.resize(450,30)
        info_1.move(335,300)
        info_1.setStyleSheet("color: grey;")
        info_p = QLabel("Enter Password or Pin", self)
        info_p.resize(450,30)
        info_p.move(350,365)
        info_p.setStyleSheet("color: blue;") 
        self.button = QPushButton("Create account", self)
        self.button.setStyleSheet("border-radius : 50; color: blue;") 
        self.button.move(334,470)
        self.button.clicked.connect(self.on_click_anc)
        button = QPushButton("Next", self)
        button.setStyleSheet("background-color : blue; border-radius : 50; color: white;")
        button.move(550,470)
        button.clicked.connect(self.on_click_sign_in)
        self.show()

    @pyqtSlot()
    def on_click(self):
        webbrowser.open("http://3.bp.blogspot.com/-And5mt9-gnc/VDXwjWFWJaI/AAAAAAAACxo/VwrbjonLwgs/s1600/EnterPin.jpg")

    @pyqtSlot()
    def on_click_sign_in(self):
        while True:
            textboxValue = self.textbox.text().lower()
            if account_ in textboxValue:                        
                print("1-1")
                break  
            else:
                print("0-1")
                break
        while True:
            textboxValue2 = self.textbox2.text().lower()
            if account_p in textboxValue2:
                print("2-1")
                break
            else:
                print("2-0")
                break
        while True:
            textboxValue3 = self.textbox3.text().lower()
            if account_pin in textboxValue3:
                self.browser = QWebEngineView()
                self.browser.setUrl(QUrl("http://www.netanimations.net/april-fools-day-005.gif"))
                self.setCentralWidget(self.browser)
                print("hello world")
                break
            else:
                exit()

    @pyqtSlot()
    def on_click_anc(self):
        self.switch_window.emit()
            
class Controller:

    def __init__(self):
        pass

    def show_login(self):
        self.login = Login()
        self.login.switch_window.connect(self.show_main)
        self.login.show()

    def show_main(self):
        self.window = MainWindow()
        self.window.switch_window.connect(self.show_window_two)
        self.login.close()
        self.window.show()

    def show_window_two(self):
        self.window_two = WindowTwo()
        self.window.close()
        self.window_two.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = Controller()
    controller.show_login()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     ex = App()
#     sys.exit(app.exec_())
