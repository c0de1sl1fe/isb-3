import sys
import os
from functools import partial

from PyQt5.QtWidgets import (QSizePolicy, QFrame, QStatusBar, QShortcut, QAction, QWidget, QLabel, QLineEdit, QPushButton,
                             QTextEdit, QGridLayout, QApplication, QHBoxLayout,
                             QRadioButton, QFileDialog, qApp, QDesktopWidget, QMessageBox,
                             QTabWidget, QVBoxLayout, QMainWindow)
from PyQt5.QtGui import QIcon, QPixmap, QFont, QKeySequence


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

        self.pathOfEnctyptedSymmKey = "Empty"
        self.pathOfPublicKey = "Empty"
        self.pathOfPrivateKey = "Empty"


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
        line2 = QLabel('''At GenKeys you can generate and save keys\n - 1.1: Generate key for symm alg\n - 1.2: Generate key for assym alg\n - 1.3: serializate assymm key\n - 1.4: Encrypt public key via private key and save
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
        buttom11 = QPushButton("Path for encrypted key")
        # buttom11.setFixedSize(40,40)
        line11 = QLabel(self.pathOfEnctyptedSymmKey)
        line11.setStyleSheet("border: 3px solid red;")
        line1.addWidget(buttom11)
        
        line1.addWidget(line11)

        # to pass args to function use partial 
        buttom11.clicked.connect(partial(self.__inputPath, self.pathOfEnctyptedSymmKey, line11))   
        line2 = QHBoxLayout()

        buttom22 = QPushButton("Path for public key")
        # buttom22.setFixedSize(40,40)
        line22 = QLabel(self.pathOfPublicKey)
        line22.setStyleSheet("border: 3px solid red;")
        line2.addWidget(buttom22)
        line2.addWidget(line22)
        buttom22.clicked.connect(partial(self.__inputPath, self.pathOfPublicKey, line22))


        line3 = QHBoxLayout()
        buttom33 = QPushButton("Path for private key")
        # buttom33.setFixedSize(40,40)
        line33 = QLabel(self.pathOfPrivateKey)
        line33.setStyleSheet("border: 3px solid red;")
        line3.addWidget(buttom33)
        line3.addWidget(line33)
        buttom33.clicked.connect(partial(self.__inputPath, self.pathOfPrivateKey, line33))    

        first.addLayout(line1)
        first.addLayout(line2)
        first.addLayout(line3)
 
        buttom1 = QPushButton("gen symm key")
        buttom2 = QPushButton("gen assymm key")
        buttom3 = QPushButton("save assymm keys")
        buttom4 = QPushButton("encrypt and save symm key")

        second.addWidget(buttom1)
        second.addWidget(buttom2)
        second.addWidget(buttom3)
        second.addWidget(buttom4)

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
        buttom11 = QPushButton("Path of data")
        # buttom11.setFixedSize(40,40)
        line11 = QLabel("wait")
        line1.addWidget(buttom11)
        line1.addWidget(line11)

        line2 = QHBoxLayout()

        buttom22 = QPushButton("Path of private key")
        # buttom22.setFixedSize(40,40)
        line22 = QLabel("wait")
        line2.addWidget(buttom22)
        line2.addWidget(line22)
        line3 = QHBoxLayout()
        buttom33 = QPushButton("Path of encrypted key")
        # buttom33.setFixedSize(40,40)
        line33 = QLabel("wait")
        line3.addWidget(buttom33)
        line3.addWidget(line33)

        buttom44 = QPushButton("Path for encrypted data")
        # buttom33.setFixedSize(40,40)
        line44 = QLabel("wait")
        line4 = QHBoxLayout()
        line4.addWidget(buttom44)
        line4.addWidget(line44)

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
        buttom1 = QPushButton("decrypt key")
        buttom2 = QPushButton("encrypt data and save")

        second.addWidget(buttom1)
        second.addWidget(buttom2)

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
        buttom11 = QPushButton("Path of encrypted data")
        # buttom11.setFixedSize(40,40)
        line11 = QLabel("wait")
        line1.addWidget(buttom11)
        line1.addWidget(line11)

        line2 = QHBoxLayout()

        buttom22 = QPushButton("Path of private key")
        # buttom22.setFixedSize(40,40)
        line22 = QLabel("wait")
        line2.addWidget(buttom22)
        line2.addWidget(line22)
        line3 = QHBoxLayout()
        buttom33 = QPushButton("Path of encrypted key")
        # buttom33.setFixedSize(40,40)
        line33 = QLabel("wait")
        line3.addWidget(buttom33)
        line3.addWidget(line33)

        buttom44 = QPushButton("Path for decrypted data")
        # buttom33.setFixedSize(40,40)
        line44 = QLabel("wait")
        line4 = QHBoxLayout()
        line4.addWidget(buttom44)
        line4.addWidget(line44)

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
        buttom1 = QPushButton("decrypt key")
        buttom2 = QPushButton("decrypt data and save")

        second.addWidget(buttom1)
        second.addWidget(buttom2)


        # layout.addLayout(text)
        layout.addLayout(first)
        layout.addWidget(separador)
        layout.addLayout(second)
        # layout.addWidget(self.__mainBtn)

        generalTab.setLayout(layout)
        return generalTab

    def __onClicked(self) -> None:
        '''change class name'''
        print("test")
    def __inputPath(self, string: str, lable: QLabel) -> None:
        # self.pathOfSymmKey = QFileDialog.getExistingDirectory(self, 'Select Folder')
        '''service function'''
        print("input path")
        string = QFileDialog.getExistingDirectory(self, 'Select Folder')
        
        if not string:
            print("error")
            QMessageBox.critical(
                self, "Error", "please select dir", QMessageBox.Ok)
        else:
            lable.setText(string)
            lable.setStyleSheet("border: 3px solid green;")
            print("ok")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
