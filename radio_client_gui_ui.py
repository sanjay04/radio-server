# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'radio_client_gui_v2.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4 import phonon
 
import sys
import socket
import pyaudio
import threading

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

   
#autogenerated code
class Ui_MainWindow(QtGui.QMainWindow):
    def __init__(self):
        
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)

        #global variables
        self.CHUNK = (441 * 6 + 150)
        self.SECRET_KEY = "my secret key"
        ##self.SERVER_IP = "192.168.0.110"
        ##self.SERVER_PORT = 35000
        ##self.SERVER_ADDR = (self.SERVER_IP,self.SERVER_PORT)
        
        #predefined objects
        self.socketfd = None
        self.p = pyaudio.PyAudio()
        self.stream = self.p.open(format=8, #formate defined in pyaudio module for wav
                channels=2, #channel 2
                rate=44100, #framerate of audio clip
                output=True) #to play audio

        
        #global constants
        self.CONNECTION = 0
        self.RECEIVE = 0
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1020, 608)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_3 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setFrameShape(QtGui.QFrame.NoFrame)
        self.label.setLineWidth(0)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 5, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 7, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 4, 2, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 5, 5, 1, 1)
        self.lineEdit_ip = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_ip.setObjectName(_fromUtf8("lineEdit_ip"))
        self.gridLayout.addWidget(self.lineEdit_ip, 6, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 5, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem4, 6, 5, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem5, 6, 0, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem6, 6, 6, 1, 1)
        self.stopButton = QtGui.QPushButton(self.centralwidget)
        self.stopButton.setObjectName(_fromUtf8("stopButton"))
        self.gridLayout.addWidget(self.stopButton, 6, 4, 1, 1)
        self.startButton = QtGui.QPushButton(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.startButton.sizePolicy().hasHeightForWidth())
        self.startButton.setSizePolicy(sizePolicy)
        self.startButton.setObjectName(_fromUtf8("startButton"))
        self.gridLayout.addWidget(self.startButton, 5, 4, 1, 1)
        spacerItem7 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem7, 6, 1, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 5, 3, 1, 1)
        self.lineEdit_port = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit_port.setObjectName(_fromUtf8("lineEdit_port"))
        self.gridLayout.addWidget(self.lineEdit_port, 6, 3, 1, 1)
        spacerItem8 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem8, 3, 2, 1, 1)
        spacerItem9 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem9, 0, 2, 1, 1)
        spacerItem10 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem10, 2, 2, 1, 1)
        spacerItem11 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem11, 1, 2, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout, 0, 0, 1, 1)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem12 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem12, 1, 0, 1, 1)
        spacerItem13 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem13, 2, 3, 1, 1)
        spacerItem14 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem14, 1, 4, 1, 1)
        self.volumeSlider = phonon.Phonon.VolumeSlider(self.centralwidget)##
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))
        self.gridLayout_2.addWidget(self.volumeSlider, 3, 2, 1, 1)
        spacerItem15 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem15, 0, 3, 1, 1)
        spacerItem16 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem16, 4, 3, 1, 1)
        self.resumeButton = QtGui.QPushButton(self.centralwidget)
        self.resumeButton.setObjectName(_fromUtf8("resumeButton"))
        self.gridLayout_2.addWidget(self.resumeButton, 1, 2, 1, 1)
        self.pauseButton = QtGui.QPushButton(self.centralwidget)
        self.pauseButton.setObjectName(_fromUtf8("pauseButton"))
        self.gridLayout_2.addWidget(self.pauseButton, 2, 2, 1, 1)
        spacerItem17 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem17, 6, 3, 1, 1)
        spacerItem18 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem18, 5, 3, 1, 1)
        spacerItem19 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem19, 3, 3, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1020, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.label.setText(_translate("MainWindow", "Server IP", None))
        self.stopButton.setText(_translate("MainWindow", "Stop", None))
        self.startButton.setText(_translate("MainWindow", "Start", None))
        self.label_2.setText(_translate("MainWindow", "Server Port", None))
        self.resumeButton.setText(_translate("MainWindow", "Resume", None))
        self.pauseButton.setText(_translate("MainWindow", "Pause", None))

        self.stopButton.clicked.connect(self.stopButton_function)
        self.startButton.clicked.connect(self.startButton_function)
        self.resumeButton.clicked.connect(self.resumeButton_function)
        self.pauseButton.clicked.connect(self.pauseButton_function)

    #self coded
    def playSong(self):
        try:
            while True:
                while(self.RECEIVE):
                    data, addr = self.socketfd.recvfrom(self.CHUNK)
                    self.stream.write(data)
        except socket.error:
            pass
        
    def stopButton_function(self):
        if(self.CONNECTION):
            self.CONNECTION = 0
            self.socketfd.close()
            

    def startButton_function(self):
        if(self.CONNECTION):
            pass
        else:       
            server_addr = (self.lineEdit_ip.text(),int(self.lineEdit_port.text()))
            self.CONNECTION = 1
            self.RECEIVE = 1
            self.socketfd = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
            self.socketfd.sendto(self.SECRET_KEY,server_addr)
            playsong_thread = threading.Thread(target=self.playSong)
            playsong_thread.start()

    def resumeButton_function(self):
        if(self.RECEIVE):
            pass
        else :
            self.RECEIVE = 1

    def pauseButton_function(self):
        if(self.RECEIVE):
            self.RECEIVE = 0

    



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    ex = Ui_MainWindow()
    ex.show()
    sys.exit(app.exec_())
