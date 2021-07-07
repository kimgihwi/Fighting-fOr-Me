import sys
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import random


class App(QtWidgets.QMainWindow):
    """
    UI of Application
    """

    def __init__(self):
        super().__init__()
        # Application Window
        self.setWindowTitle("Fighting fOr Me (FOM)")
        # self.setWindowIcon((QtGui.QIcon(abs_path + '/etc/icon.png')))
        self.setFixedSize(600, 200)
        self.center()
        # self.statusBar().showMessage('Ready')

        self.name = ""

        ### 입력칸 설정 ###
        # self.name_block = QtWidgets.QLineEdit(self)
        self.quote_block = QtWidgets.QLineEdit(self)
        # self.quote_block = QtWidgets.QTextEdit(self)

        # self.name_block.setAlignment(QtCore.Qt.AlignCenter)
        # self.quote_block.setAlignment(QtCore.Qt.AlignCenter)

        # self.name_block.setFont(QtGui.QFont("나눔바른고딕", 10))
        self.quote_block.setFont(QtGui.QFont("나눔바른고딕", 10))

        # self.name_block.move(670, 50)
        self.quote_block.move(100, 120)

        self.quote_block.setFixedWidth(370)    # 블록 가로 설정
        self.quote_block.setFixedHeight(50)    # 블록 세로 설정

        ### 입력칸 설명 ###
        # self.name_label = QtWidgets.QLabel("이름 : ", self)
        self.quote_label = QtWidgets.QLabel("위로의\n\n한마디 : ", self)
        self.load_label = QtWidgets.QLabel("", self)

        # self.name_label.resize(50, 30)
        self.quote_label.resize(50, 50)
        self.load_label.resize(400, 100)

        # self.name_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 10))
        self.quote_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 10))
        self.load_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 10))

        # self.name_label.move(630, 50)
        self.quote_label.move(35, 120)
        self.load_label.move(35, 10)

        ### 버튼 ###
        # self.name_btn = QtWidgets.QPushButton("확인", self)
        # self.name_btn.move(670, 100)
        # self.name_btn.clicked.connect(self.name_clicked)

        self.save_btn = QtWidgets.QPushButton("저장", self)
        self.save_btn.move(500, 120)
        self.save_btn.resize(70, 50)
        self.save_btn.clicked.connect(self.save_clicked)

        self.quote_btn = QtWidgets.QPushButton("나에게로 화이팅...!", self)
        self.quote_btn.move(450, 30)
        self.quote_btn.resize(120, 50)
        self.quote_btn.clicked.connect(self.answer_clicked)

    def center(self):
        """
        Application 실행 시 윈도우의 정중앙에 배치
        """
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def name_clicked(self):
        """
        이름 변수 저장
        """
        self.name = self.name_block.text()

    def save_clicked(self):
        """
        명언 저장
        """
        quote_num = len(os.listdir('./quote_data'))
        f = open("./quote_data/" + str(quote_num+1) + ".txt", 'w')
        f.write(self.quote_block.text())
        f.close()
        self.quote_block.clear()

    def answer_clicked(self):
        """
        명언 불러오기
        """
        quote_num = len(os.listdir('./quote_data'))
        rand_num = random.randrange(1, quote_num+1)
        f = open("./quote_data/" + str(rand_num) + ".txt", 'r', encoding='utf-8')
        # quote = f.readline()
        quote = ""
        lines = f.readlines()
        for line in lines:
            if len(line) > 30:
                quote += line[:30]
                quote += "\n"
                quote += line[30:]
            else:
                quote += line + "\n"
        f.close()
        self.load_label.setText(quote)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()
