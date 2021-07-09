import sys
import os

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui

import random

import threading
import schedule
import time


class App(QtWidgets.QMainWindow):
    """
    UI of Application
    """

    def __init__(self):
        super().__init__()
        # Application Window
        self.setWindowTitle("Fighting fOr Me (FOM)")
        self.setWindowIcon((QtGui.QIcon('./icon/fom_icon.ico')))
        self.setFixedSize(700, 300)
        self.center()
        # self.statusBar().showMessage('Ready')

        self.name = ""
        self.quote = ""
        # self.timer_stop_signal = False
        # self.timer = False

        ### 입력칸 설정 ###
        self.name_block = QtWidgets.QLineEdit(self)
        self.quote_block = QtWidgets.QLineEdit(self)
        # self.quote_block = QtWidgets.QTextEdit(self)

        self.name_block.setAlignment(QtCore.Qt.AlignCenter)
        # self.quote_block.setAlignment(QtCore.Qt.AlignCenter)

        self.name_block.setFont(QtGui.QFont("나눔바른고딕", 10))
        self.quote_block.setFont(QtGui.QFont("나눔바른고딕", 10))

        self.name_block.move(580, 50)
        self.quote_block.move(100, 220)

        self.quote_block.setFixedWidth(480)    # 블록 가로 설정
        self.quote_block.setFixedHeight(50)    # 블록 세로 설정

        ### 입력칸 설명 ###
        self.name_label = QtWidgets.QLabel("이름 : ", self)
        self.quote_label = QtWidgets.QLabel("위로의\n\n한마디 : ", self)
        # self.load_label = QtWidgets.QLabel("", self)

        self.name_label.resize(50, 30)
        self.quote_label.resize(50, 50)
        # self.load_label.resize(500, 200)

        self.name_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 10))
        self.quote_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 9))
        # self.load_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 10))

        self.name_label.move(530, 50)
        self.quote_label.move(35, 220)
        # self.load_label.move(35, 10)

        ### 버튼 ###
        self.name_btn = QtWidgets.QPushButton("입력", self)
        self.name_btn.move(580, 90)
        self.name_btn.clicked.connect(self.name_clicked)

        self.save_btn = QtWidgets.QPushButton("저장", self)
        self.save_btn.move(600, 220)
        self.save_btn.resize(70, 50)
        self.save_btn.clicked.connect(self.save_clicked)

        # self.quote_btn = QtWidgets.QPushButton("나에게로 화이팅...!", self)
        self.quote_btn = QtWidgets.QPushButton("", self)
        self.quote_btn.setIcon(QtGui.QIcon('./icon/fom_icon.ico'))
        self.quote_btn.setIconSize(QtCore.QSize(45, 45))
        self.quote_btn.move(100, 50)
        self.quote_btn.resize(400, 150)
        self.quote_btn.clicked.connect(self.answer_clicked)

        # self.timer_btn = QtWidgets.QPushButton("자동으로 실행", self)
        # self.timer_btn.setIconSize(QtCore.QSize(45, 45))
        # self.timer_btn.move(580, 150)
        # self.timer_btn.resize(100, 50)
        # self.timer_btn.clicked.connect(self.timer_clicked)
        #
        # self.timer_stop_btn = QtWidgets.QPushButton("실행 중지", self)
        # self.timer_stop_btn.setIconSize(QtCore.QSize(45, 45))
        # self.timer_stop_btn.move(580, 200)
        # self.timer_stop_btn.resize(100, 50)
        # self.timer_stop_btn.clicked.connect(self.timer_stop_clicked)

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
        if len(self.quote_block.text()) < 1:
            pass
        else:
            quote_num = len(os.listdir('./quote_data'))
            f = open("./quote_data/" + str(quote_num + 1) + ".txt", 'w', encoding='utf-8')
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
        if len(self.name) < 1:
            quote = ""
        else:
            quote = self.name + "! "
        lines = f.readlines()
        for line in lines:
            quote += line + "\n"
        f.close()
        self.quote = quote
        # print(quote)

        # self.load_label.setText(quote)
        # print(self.load_label.text())

        # if timer:
        #     self.timer_clicked()

        self.quote_popup()

    def quote_popup(self):
        quote_box = QtWidgets.QMessageBox()
        # quote_box.setMinimumHeight(500)
        # quote_box.setMinimumWidth(400)
        quote_box.setStyleSheet("QLabel {min-width: 300px; min-height: 20px;}")
        if len(self.name) < 1:
            quote_box.setWindowTitle("나에게...")
        else:
            quote_box.setWindowTitle(self.name + "에게...")
        # quote_box.setInformativeText(self.load_label.text())
        quote_box.setInformativeText(self.quote)
        quote_box.setStandardButtons(QtWidgets.QMessageBox.Ok)
        ok_btn = quote_box.button(QtWidgets.QMessageBox.Ok)
        ok_btn.setText("다시")
        ok_btn.setIcon(QtGui.QIcon('./icon/fom_icon.ico'))

        # if timer:
        #     stop_btn = quote_box.addButton("종료", QtWidgets.QMessageBox.ActionRole)
        quote_box.setWindowIcon(QtGui.QIcon('./icon/fom_icon.ico'))
        quote_box.exec_()
        # if timer:
        #     # start_sec = time.time()
        #     # while True:
        #     #     cur_sec = time.time()
        #     #     if cur_sec - start_sec > 2:
        #     #         quote_box.done(1)
        #     #         break
        #     if quote_box.clickedButton() == stop_btn:
        #         self.timer_stop_signal = True


    #TODO: 시간 기능 추가

    # def timer_clicked(self):
    #     # while True:
    #     # threading.Timer(3, self.answer_clicked).start()
    #     self.timer = True
    #     schedule.every(3).seconds.do(self.answer_clicked)
    #     # schedule.run_pending()
    #     # self.answer_clicked(self.timer)
    #     while True:
    #         schedule.run_pending()
    #         # time.sleep(3)
    #         self.answer_clicked(self.timer)
    #         # self.answer_clicked()
    #         if self.timer_stop_signal:
    #             self.timer_stop_signal = False
    #             break
    #     # time.sleep(3)
    #     # print(2)
    #     # while True:
    #     #     self.answer_clicked()
    #     #     time.sleep(3)
    #
    # def timer_stop_clicked(self):
    #     self.timer_stop_signal = True


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()
