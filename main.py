import sys
import os
from functools import partial

from PyQt5.QtWidgets import (QSizePolicy, QFrame, QStatusBar, QShortcut, QAction, QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout,
                             QRadioButton, QFileDialog, qApp, QDesktopWidget, QMessageBox,
                             QTabWidget, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QKeySequence
from utils import generateAssymKeys, generateSymmKey, saveAssymKeys, saveSymmKey, loadAndDecryptSymmKey, encryptData, decryptData


class Example(QWidget):
    def __init__(self) -> None:
        '''Constructor'''
        super().__init__()

        self.initUI()

    # def __iter__(self) -> Self:
    #     '''something'''
    #     return self

    def initUI(self) -> None:
        '''support constructor function'''

        self.shortcut_exit = QShortcut(QKeySequence('esc'), self)
        self.shortcut_exit.activated.connect(qApp.quit)

        self.settings = {
            "pathOfEncryptedSymmKeyToSave": "Empty",
            "pathOfPublicKeyToSave": "Empty",
            "pathOfPrivateKeyToSave": "Empty",

            "pathOfDataToGet": "Empty",
            "pathOfPrivateKeyToGet1": "Empty",
            "pathOfEnctyptedSymmKeyToGet1": "Empty",
            "pathOfEncryptedDataToSave": "Empty",

            "pathOfEncryptedDataToGet": "Empty",
            "pathOfPrivateKeyToGet2": "Empty",
            "pathOfEnctyptedSymmKeyToGet2": "Empty",
            "pathOfDataToSave": "Empty"
        }

        self.pathOfEncryptedSymmKeyToSave = "Empty"
        self.pathOfPublicKeyToSave = "Empty"
        self.pathOfPrivateKeyToSave = "Empty"

        self.pathOfDataToGet = "Empty"
        self.pathOfPrivateKeyToGet1 = "Empty"
        self.pathOfEnctyptedSymmKeyToGet1 = "Empty"
        self.pathOfEncryptedDataToSave = "Empty"

        self.pathOfEncryptedDataToGet = "Empty"
        self.pathOfPrivateKeyToGet2 = "Empty"
        self.pathOfEnctyptedSymmKeyToGet2 = "Empty"
        self.pathOfDataToSave = "Empty"

        self.symmKey = 0
        self.publicKey = 0
        self.privateKey = 0

        self.setWindowTitle('Lab3')
        self.setWindowIcon(QIcon('6112_Logo_git_prefinal.jpg'))
        layout = QVBoxLayout()
        self.setLayout(layout)
        tabs = QTabWidget()

        tabs.addTab(self.__generalTab(), "general")
        tabs.addTab(self.__generateKeys(), "GenKeys")
        tabs.addTab(self.__encryptionTab(), "EncryptionTab")
        tabs.addTab(self.__decryptionTab(), "DecryptionTab")
        layout.addWidget(tabs)

        self.setGeometry(400, 400, 450, 400)
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)

        self.show()

    # Main window with hello-words and descripition what's going on
    def __generalTab(self) -> QWidget:
        '''main window with hello-words and descripition what's going on'''
        custom_font = QFont()
        custom_font.setPixelSize(40)
        generalTab = QWidget()
        layout = QVBoxLayout()
        text = QVBoxLayout()
        line1 = QLabel("Hello there!")
        line1.setFont(custom_font)

        custom_font.setPixelSize(20)
        line2 = QLabel('''At GenKeys you can generate and save keys:\n - 1.1: Generate key for symm alg\n - 1.2: Generate key for assym alg\n - 1.3: serializate assymm key\n - 1.4: Encrypt public key via private key and save
                        \nAt EncryptionTab you can:\n - 2.1: Decrypt symmetric key\n - 2.2: Encrypt you text and save it
                        \nAt DecryptionTab data of hybrid system:\n - 3.1: Decrypt symmetric key\n - 3.2: Decrypt you text and save it''')
        line2.setFont(custom_font)
        text.addWidget(line1)
        text.addWidget(line2)
        layout.addLayout(text)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab

    def __generateKeys(self) -> QWidget:

        generalTab = QWidget()
        layout = QVBoxLayout()
        first = QVBoxLayout()
        first.setContentsMargins(10, 10, 10, 200)
        second = QHBoxLayout()
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setLineWidth(2)
        # separador.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

        line1 = QHBoxLayout()
        button11 = QPushButton("Path for encrypted key")
        # buttom11.setFixedSize(40,40)
        line11 = QLabel(self.pathOfEncryptedSymmKeyToSave)
        line11.setStyleSheet("border: 3px solid red;")
        line1.addWidget(button11)
        line1.addWidget(line11)
        # to pass args to function use partial
        button11.clicked.connect(
            partial(self.__inputPath, self.settings, "pathOfEncryptedSymmKeyToSave", line11))

        line2 = QHBoxLayout()
        button22 = QPushButton("Path for public key")

        line22 = QLabel(self.pathOfPublicKeyToSave)
        line22.setStyleSheet("border: 3px solid red;")
        line2.addWidget(button22)
        line2.addWidget(line22)
        button22.clicked.connect(
            partial(self.__inputPath, self.settings, "pathOfPublicKeyToSave", line22))

        line3 = QHBoxLayout()
        button33 = QPushButton("Path for private key")

        line33 = QLabel(self.pathOfPrivateKeyToSave)
        line33.setStyleSheet("border: 3px solid red;")
        line3.addWidget(button33)
        line3.addWidget(line33)
        button33.clicked.connect(
            partial(self.__inputPath, self.settings, "pathOfPrivateKeyToSave", line33))

        first.addLayout(line1)
        first.addLayout(line2)
        first.addLayout(line3)

        button1 = QPushButton("gen symm key")
        button1.setStyleSheet("background-color: red")
        button1.clicked.connect(partial(self.__generateSymmKey, button1))

        button2 = QPushButton("gen assymm key")
        button2.setStyleSheet("background-color: red")
        button2.clicked.connect(partial(self.__generateAssymKeys, button2))

        button3 = QPushButton("save assymm keys")  # make it green
        button3.clicked.connect(partial(self.__saveAssymKeys, self.settings["pathOfPublicKeyToSave"],
                                self.settings["pathOfPrivateKeyToSave"], self.publicKey, self.privateKey, button3))

        button4 = QPushButton("encrypt and save symm key")  # make it green
        button4.clicked.connect(partial(self.__onClicked, button4))
        # button4.clicked.connect(partial(
        #     self.__saveSymmKey, self.pathOfEncryptedDataToSave, self.publicKey, self.symmKey, button4))

        button4.clicked.connect(partial(self.__onClicked, button4))
        second.addWidget(button1)
        second.addWidget(button2)
        second.addWidget(button3)
        second.addWidget(button4)

        # layout.addLayout(text)
        layout.addLayout(first)
        layout.addWidget(separador)
        layout.addLayout(second)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab

    def __encryptionTab(self) -> QWidget:

        generalTab = QWidget()
        layout = QVBoxLayout()

        first = QVBoxLayout()
        first.setContentsMargins(10, 10, 10, 200)
        second = QHBoxLayout()
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setLineWidth(2)
        # separador.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

        line1 = QHBoxLayout()
        button11 = QPushButton("Path of data")
        # buttom11.setFixedSize(40,40)
        line11 = QLabel(self.pathOfDataToGet)
        line11.setStyleSheet("border: 3px solid red;")
        line1.addWidget(button11)
        line1.addWidget(line11)
        button11.clicked.connect(
            partial(self.__inputFile, self.pathOfDataToGet, line11, '.txt'))

        line2 = QHBoxLayout()
        button22 = QPushButton("Path of private key")
        # buttom22.setFixedSize(40,40)

        line22 = QLabel(self.pathOfPrivateKeyToGet1)
        line22.setStyleSheet("border: 3px solid red")
        line2.addWidget(button22)
        line2.addWidget(line22)
        button22.clicked.connect(
            partial(self.__inputFile, self.pathOfPrivateKeyToGet1, line22, '.pem'))

        line3 = QHBoxLayout()
        button33 = QPushButton("Path of encrypted key")
        # buttom33.setFixedSize(40,40)
        line33 = QLabel(self.pathOfEnctyptedSymmKeyToGet1)
        line33.setStyleSheet("border: 3px solid red;")
        line3.addWidget(button33)
        line3.addWidget(line33)
        button33.clicked.connect(
            partial(self.__inputFile, self.pathOfEnctyptedSymmKeyToGet1, line33, '.bin'))

        line4 = QHBoxLayout()
        button44 = QPushButton("Path for encrypted data")
        # buttom33.setFixedSize(40,40)
        line44 = QLabel(self.pathOfEncryptedDataToSave)
        line44.setStyleSheet("border: 3px solid red;")
        line4.addWidget(button44)
        line4.addWidget(line44)
        button44.clicked.connect(
            partial(self.__inputPath, self.pathOfEncryptedDataToSave, line44))

        first.addLayout(line1)
        first.addLayout(line2)
        first.addLayout(line3)
        first.addLayout(line4)
        # text = QHBoxLayout()
        # line1 = QLabel("Hello there!")
        # buttom = QPushButton("test")
        # buttom.clicked.connect(self.__onClicked)
        # buttom.adjustSize()
        # text.addWidget(buttom)
        # text.addWidget(line1)
        button1 = QPushButton("decrypt key")
        button1.setStyleSheet("background-color: red")
        button2 = QPushButton("encrypt data and save")  # make it green

        second.addWidget(button1)
        second.addWidget(button2)

        # layout.addLayout(text)
        layout.addLayout(first)
        layout.addWidget(separador)
        layout.addLayout(second)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab
    # image tab where user choose directory and see the img via _next_

    def __decryptionTab(self) -> QWidget:

        generalTab = QWidget()
        layout = QVBoxLayout()

        first = QVBoxLayout()
        first.setContentsMargins(10, 10, 10, 200)
        second = QHBoxLayout()
        separador = QFrame()
        separador.setFrameShape(QFrame.HLine)
        separador.setLineWidth(2)
        # separador.setSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)

        line1 = QHBoxLayout()
        button11 = QPushButton("Path of encrypted data")
        # buttom11.setFixedSize(40,40)
        line11 = QLabel(self.pathOfEncryptedDataToGet)
        line11.setStyleSheet("border: 3px solid red")
        line1.addWidget(button11)
        line1.addWidget(line11)
        button11.clicked.connect(
            partial(self.__inputFile, self.pathOfEncryptedDataToGet, line11, '.bin'))

        line2 = QHBoxLayout()
        button22 = QPushButton("Path of private key")
        # buttom22.setFixedSize(40,40)
        line22 = QLabel(self.pathOfPrivateKeyToGet2)
        line22.setStyleSheet("border: 3px solid red;")
        line2.addWidget(button22)
        line2.addWidget(line22)
        button22.clicked.connect(
            partial(self.__inputFile, self.pathOfPrivateKeyToGet2, line22, '.pem'))

        line3 = QHBoxLayout()
        button33 = QPushButton("Path of encrypted key")
        # buttom33.setFixedSize(40,40)
        line33 = QLabel(self.pathOfEnctyptedSymmKeyToGet2)
        line33.setStyleSheet("border: 3px solid red;")
        line3.addWidget(button33)
        line3.addWidget(line33)
        button33.clicked.connect(
            partial(self.__inputFile, self.pathOfEnctyptedSymmKeyToGet2, line33, '.bin'))

        line4 = QHBoxLayout()
        button44 = QPushButton("Path for decrypted data")
        # buttom33.setFixedSize(40,40)
        line44 = QLabel(self.pathOfDataToSave)
        line44.setStyleSheet("border: 3px solid red")
        line4.addWidget(button44)
        line4.addWidget(line44)
        button44.clicked.connect(
            partial(self.__inputPath, self.pathOfDataToSave, line44))

        first.addLayout(line1)
        first.addLayout(line2)
        first.addLayout(line3)
        first.addLayout(line4)
        # text = QHBoxLayout()
        # line1 = QLabel("Hello there!")
        # buttom = QPushButton("test")
        # buttom.clicked.connect(self.__onClicked)
        # buttom.adjustSize()
        # text.addWidget(buttom)
        # text.addWidget(line1)
        button1 = QPushButton("decrypt key")
        button1.setStyleSheet("background-color: red")
        button2 = QPushButton("decrypt data and save")  # make it green

        second.addWidget(button1)
        second.addWidget(button2)

        # layout.addLayout(text)
        layout.addLayout(first)
        layout.addWidget(separador)
        layout.addLayout(second)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab

    def __onClicked(self, button: QPushButton) -> None:
        '''change class name'''
        # button.setStyleSheet("background-color: green")
        print(self.settings["pathOfPublicKeyToSave"],
              self.settings["pathOfPrivateKeyToSave"], self.publicKey, self.privateKey)
        # print(self.symmKey)
        # print(self.privateKey)
        # print(self.publicKey)
        # print(self.settings['pathOfEncryptedSymmKeyToSave'])
        # print("test")

    def __inputPath(self, settings: tuple, key: str, lable: QLabel) -> None:
        '''service function'''
        print("input path")
        settings[key] = QFileDialog.getExistingDirectory(self, 'Select Folder')
        print(settings[key])
        if not settings[key]:
            print("error")
            QMessageBox.critical(
                self, "Error", "please select dir", QMessageBox.Ok)

        else:
            lable.setText(settings[key])
            lable.setStyleSheet("border: 3px solid green;")
            print("ok")

    def __inputFile(self, settings: tuple, key: str,  lable: QLabel, typeCheck: str) -> None:
        # self.pathOfSymmKey = QFileDialog.getExistingDirectory(self, 'Select Folder')
        '''service function'''
        print("input path")
        settings[key] = QFileDialog.getOpenFileName(self, 'Select Folder')[0]
        print(settings[key])
        if not typeCheck in settings[key]:
            print("error")
            QMessageBox.critical(
                self, "Error", f"select correct file type - {typeCheck}", QMessageBox.Ok)
        else:
            lable.setText(settings[key])
            lable.setStyleSheet("border: 3px solid green;")
            print("ok")

    def __generateSymmKey(self, button: QPushButton):

        self.symmKey = generateSymmKey()
        button.setStyleSheet("background-color: green")

        print(self.symmKey)

    def __generateAssymKeys(self, button: QPushButton):

        self.privateKey = generateAssymKeys()
        self.publicKey = self.privateKey.public_key()
        button.setStyleSheet("background-color: green")

        print(self.publicKey)
        print(self.privateKey)

    def __saveAssymKeys(self, pathOfPublic: str, pathOfPrivate: str, publicKey, privateKey, button: QPushButton):
        print(self.settings)
        print(pathOfPrivate)
        print(pathOfPublic)
        print(publicKey)
        print(privateKey)
        if pathOfPrivate == 'Empty' or pathOfPublic == 'Empty' or not publicKey or not privateKey:

            print(pathOfPrivate)
            print(pathOfPublic)
            print(publicKey)
            print(privateKey)

            msg = QMessageBox()
            msg.setText('error')
            msg.setWindowTitle('enter every path and gen every key')
            msg.exec_()
            button.setStyleSheet("background-color: red")
            return
        try:
            saveAssymKeys(pathOfPublic, pathOfPrivate, publicKey, privateKey)
            button.setStyleSheet("background-color: green")
        except:
            msg = QMessageBox()
            msg.setText('error')
            msg.setWindowTitle('error')
            msg.exec_()
            button.setStyleSheet("background-color: red")

    def __saveSymmKey(self, pathOfKey: str, publicKey, symmKey: str, button: QPushButton):
        if pathOfKey == 'Empty' or not publicKey or not symmKey:
            msg = QMessageBox()
            msg.setWindowTitle('error')
            msg.setText('enter every path and gen every key')
            msg.exec_()
            button.setStyleSheet("background-color: red")
            return
        try:
            saveSymmKey(pathOfKey, publicKey, symmKey)
            button.setStyleSheet("background-color: green")
        except:
            msg = QMessageBox()
            msg.setText('error')
            msg.setWindowTitle('error')
            msg.exec_()
            button.setStyleSheet("background-color: red")

    def __loadAndDecryptSymmKey(self, pathOfKey: str, pathOfPrivateKey: str, button: QPushButton):
        if pathOfKey == 'Empty' or pathOfPrivateKey == 'Empty':
            msg = QMessageBox()
            msg.setWindowTitle('error')
            msg.setText('enter every path and gen every key')
            msg.exec_()
            button.setStyleSheet("background-color: red")
            return
        try:
            self.symmKey = loadAndDecryptSymmKey(pathOfKey, pathOfPrivateKey)
            button.setStyleSheet("background-color: green")
        except:
            msg = QMessageBox()
            msg.setText('error')
            msg.setWindowTitle('error')
            msg.exec_()
            button.setStyleSheet("background-color: red")

    def __encryptData(self, pathToSave: str, pathOfData: str, key, button: QPushButton):
        if pathToSave == 'Empty' or pathOfData == 'Empty' or not key:
            msg = QMessageBox()
            msg.setWindowTitle('error')
            msg.setText('enter every path and gen every key')
            msg.exec_()
            button.setStyleSheet("background-color: red")
            return
        try:
            encryptData(pathToSave, pathOfData, key)
            button.setStyleSheet("background-color: green")
        except:
            msg = QMessageBox()
            msg.setText('error')
            msg.setWindowTitle('error')
            msg.exec_()
            button.setStyleSheet("background-color: red")

    def decryptData(self, pathToSave: str, pathOfData: str, key, button: QPushButton):
        if pathToSave == 'Empty' or pathOfData == 'Empty' or not key:
            msg = QMessageBox()
            msg.setWindowTitle('error')
            msg.setText('enter every path and gen every key')
            msg.exec_()
            button.setStyleSheet("background-color: red")
            return
        try:
            decryptData(pathToSave, pathOfData, key)
            button.setStyleSheet("background-color: green")
        except:
            msg = QMessageBox()
            msg.setText('error')
            msg.setWindowTitle('error')
            msg.exec_()
            button.setStyleSheet("background-color: red")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
