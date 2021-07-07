import sys

from PyQt5 import QtCore
from PyQt5 import QtWidgets
from PyQt5 import QtGui


class App(QtWidgets.QMainWindow):
    """
    UI of Application
    """

    def __init__(self):
        super().__init__()
        # Application Window
        self.setWindowTitle("정은성 화이팅")
        # self.setWindowIcon((QtGui.QIcon(abs_path + '/etc/icon.png')))
        self.setFixedSize(800, 450)
        # self.center()
        # self.statusBar().showMessage('Ready')

        ### 입력칸 설정 ###
        self.name_block = QtWidgets.QLineEdit(self)
        # self.quote_block = QtWidgets.QLineEdit(self)
        self.quote_block = QtWidgets.QTextEdit(self)

        self.name_block.setAlignment(QtCore.Qt.AlignCenter)
        # self.quote_block.setAlignment(QtCore.Qt.AlignCenter)

        self.name_block.setFont(QtGui.QFont("나눔바른고딕", 10))
        self.quote_block.setFont(QtGui.QFont("나눔바른고딕", 10))

        self.name_block.move(670, 50)
        self.quote_block.move(100, 350)

        self.quote_block.setFixedWidth(550)    # 블록 가로 설정
        self.quote_block.setFixedHeight(50)    # 블록 세로 설정

        ### 입력칸 설명 ###
        self.name_label = QtWidgets.QLabel("이름 : ", self)
        self.quote_label = QtWidgets.QLabel("명언 : ", self)

        self.name_label.resize(50, 30)
        self.quote_label.resize(50, 30)

        self.name_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 10))
        self.quote_label.setFont(QtGui.QFont("나눔스퀘어라운드 Bold", 12))

        self.name_label.move(630, 50)
        self.quote_label.move(50, 360)


        ### 버튼 ###
        self.name_btn = QtWidgets.QPushButton("확인", self)
        self.name_btn.move(670, 100)
        # self.name_btn.clicked.connect(self.save_clicked)

        self.save_btn = QtWidgets.QPushButton("저장", self)
        self.save_btn.move(670, 350)
        self.save_btn.resize(100, 50)
        # self.save_btn.clicked.connect(self.save_clicked)

        self.save_btn = QtWidgets.QPushButton("나에게로 화이팅...!", self)
        self.save_btn.move(100, 50)
        self.save_btn.resize(300, 200)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    ex = App()
    ex.show()
    app.exec_()
