# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tictactoe.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(480, 800)
        Form.setMinimumSize(QtCore.QSize(480, 800))
        Form.setMaximumSize(QtCore.QSize(480, 800))
        self.frame = QtWidgets.QFrame(Form)
        self.frame.setGeometry(QtCore.QRect(0, 0, 480, 800))
        self.frame.setStyleSheet("QFrame {\n"
"    background-color: #222222;\n"
"}")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.button_7 = QtWidgets.QPushButton(self.frame)
        self.button_7.setGeometry(QtCore.QRect(60, 610, 121, 121))
        self.button_7.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_7.setText("")
        self.button_7.setObjectName("button_7")
        self.button_8 = QtWidgets.QPushButton(self.frame)
        self.button_8.setGeometry(QtCore.QRect(180, 610, 121, 121))
        self.button_8.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_8.setText("")
        self.button_8.setObjectName("button_8")
        self.button_9 = QtWidgets.QPushButton(self.frame)
        self.button_9.setGeometry(QtCore.QRect(300, 610, 121, 121))
        self.button_9.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_9.setText("")
        self.button_9.setObjectName("button_9")
        self.button_5 = QtWidgets.QPushButton(self.frame)
        self.button_5.setGeometry(QtCore.QRect(180, 490, 121, 121))
        self.button_5.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_5.setText("")
        self.button_5.setObjectName("button_5")
        self.button_6 = QtWidgets.QPushButton(self.frame)
        self.button_6.setGeometry(QtCore.QRect(300, 490, 121, 121))
        self.button_6.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_6.setText("")
        self.button_6.setObjectName("button_6")
        self.button_4 = QtWidgets.QPushButton(self.frame)
        self.button_4.setGeometry(QtCore.QRect(60, 490, 121, 121))
        self.button_4.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_4.setText("")
        self.button_4.setObjectName("button_4")
        self.button_2 = QtWidgets.QPushButton(self.frame)
        self.button_2.setGeometry(QtCore.QRect(180, 370, 121, 121))
        self.button_2.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_2.setText("")
        self.button_2.setObjectName("button_2")
        self.button_3 = QtWidgets.QPushButton(self.frame)
        self.button_3.setGeometry(QtCore.QRect(300, 370, 121, 121))
        self.button_3.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_3.setText("")
        self.button_3.setObjectName("button_3")
        self.button_1 = QtWidgets.QPushButton(self.frame)
        self.button_1.setGeometry(QtCore.QRect(60, 370, 121, 121))
        self.button_1.setStyleSheet("QPushButton {\n"
"    background-color: #535353;\n"
"    border: 5px solid #222222;\n"
"    border-radius: 1em;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    \n"
"}\n"
"\n"
"QPushButton:hover {\n"
"\n"
"}")
        self.button_1.setText("")
        self.button_1.setObjectName("button_1")
        self.tic_tac_toe_label = QtWidgets.QLabel(self.frame)
        self.tic_tac_toe_label.setGeometry(QtCore.QRect(50, 0, 361, 91))
        self.tic_tac_toe_label.setStyleSheet("#tic_tac_toe_label {\n"
"    font: 75 italic 11pt \"Z003\"; \n"
"    color: white;\n"
"    font-size: 50px;\n"
"}")
        self.tic_tac_toe_label.setAlignment(QtCore.Qt.AlignCenter)
        self.tic_tac_toe_label.setObjectName("tic_tac_toe_label")
        self.coded_by_label = QtWidgets.QLabel(self.frame)
        self.coded_by_label.setGeometry(QtCore.QRect(110, 750, 261, 41))
        self.coded_by_label.setStyleSheet("#coded_by_label {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    color: white;\n"
"    font-size: 24px;\n"
"    background-color: transparent;\n"
"    margin-left: 25px;\n"
"}")
        self.coded_by_label.setObjectName("coded_by_label")
        self.tivole_label = QtWidgets.QLabel(self.frame)
        self.tivole_label.setGeometry(QtCore.QRect(250, 750, 121, 41))
        self.tivole_label.setStyleSheet("#tivole_label {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    color: #00ff2d;\n"
"    font-size: 24px;\n"
"    background-color: transparent;\n"
"}")
        self.tivole_label.setObjectName("tivole_label")
        self.pick_to_start_label = QtWidgets.QLabel(self.frame)
        self.pick_to_start_label.setGeometry(QtCore.QRect(130, 80, 211, 81))
        self.pick_to_start_label.setStyleSheet("#pick_to_start_label {\n"
"    font: 75 11pt \"Latin Modern Mono Prop\";\n"
"    color: #eeeeee;\n"
"    font-size: 18px;\n"
"}")
        self.pick_to_start_label.setAlignment(QtCore.Qt.AlignCenter)
        self.pick_to_start_label.setObjectName("pick_to_start_label")
        self.X_button = QtWidgets.QPushButton(self.frame)
        self.X_button.setGeometry(QtCore.QRect(100, 140, 64, 64))
        self.X_button.setStyleSheet("#X_button {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    background-color: green;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #eeeeee;\n"
"    font-size: 30px;\n"
"}")
        self.X_button.setObjectName("X_button")
        self.O_button = QtWidgets.QPushButton(self.frame)
        self.O_button.setGeometry(QtCore.QRect(170, 140, 64, 64))
        self.O_button.setStyleSheet("#O_button {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    background-color: #444444;\n"
"    color: #ffffff;\n"
"    border-radius: 8px;\n"
"    border: 2px solid #eeeeee;\n"
"    font-size: 30px;\n"
"}")
        self.O_button.setObjectName("O_button")
        self.start_reset_button = QtWidgets.QPushButton(self.frame)
        self.start_reset_button.setGeometry(QtCore.QRect(240, 140, 128, 64))
        self.start_reset_button.setStyleSheet("#start_reset_button {\n"
"    /* START version */\n"
"    background-color: #00bb00;\n"
"    color: white;\n"
"    font-size: 16px;\n"
"    border-radius: 15px;\n"
"    border: 3px solid #00ff47;\n"
"}\n"
"\n"
"\n"
"#start_reset_button:pressed {\n"
"    background-color: #00aa00;\n"
"}\n"
"")
        self.start_reset_button.setCheckable(False)
        self.start_reset_button.setChecked(False)
        self.start_reset_button.setObjectName("start_reset_button")
        self.which_turn_label = QtWidgets.QLabel(self.frame)
        self.which_turn_label.setGeometry(QtCore.QRect(60, 230, 361, 41))
        self.which_turn_label.setStyleSheet("#which_turn_label {\n"
"    color: #ffa100;\n"
"}")
        self.which_turn_label.setAlignment(QtCore.Qt.AlignCenter)
        self.which_turn_label.setObjectName("which_turn_label")
        self.score_round = QtWidgets.QLabel(self.frame)
        self.score_round.setGeometry(QtCore.QRect(210, 270, 61, 51))
        self.score_round.setStyleSheet("#score_round {\n"
"    border: 2px solid #ffa100;\n"
"    color: white;\n"
"    background-color: #000000;\n"
"    font-size: 12px;\n"
"}")
        self.score_round.setTextFormat(QtCore.Qt.AutoText)
        self.score_round.setAlignment(QtCore.Qt.AlignCenter)
        self.score_round.setIndent(-1)
        self.score_round.setObjectName("score_round")
        self.score_second = QtWidgets.QLabel(self.frame)
        self.score_second.setGeometry(QtCore.QRect(270, 270, 101, 51))
        self.score_second.setStyleSheet("#score_second {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    border: 2px solid #ffa100;\n"
"    padding-left: 8px;\n"
"    background-color: #000000;\n"
"    color: white;\n"
"    font-size: 13px;\n"
"}")
        self.score_second.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.score_second.setObjectName("score_second")
        self.score_first = QtWidgets.QLabel(self.frame)
        self.score_first.setGeometry(QtCore.QRect(110, 270, 101, 51))
        self.score_first.setStyleSheet("#score_first {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    border: 2px solid #ffa100;\n"
"    padding-right: 8px;\n"
"    color: white;\n"
"    background-color: #000000;\n"
"    font-size: 13px;\n"
"}")
        self.score_first.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.score_first.setObjectName("score_first")
        self.score_point_first = QtWidgets.QLabel(self.frame)
        self.score_point_first.setGeometry(QtCore.QRect(60, 270, 71, 51))
        self.score_point_first.setStyleSheet("#score_point_first {\n"
"    border: 2px solid #ffa100;\n"
"    border-radius: 25px;\n"
"    color: white;\n"
"    font-size: 32px;\n"
"    background-color: #8c5900;\n"
"}")
        self.score_point_first.setAlignment(QtCore.Qt.AlignCenter)
        self.score_point_first.setObjectName("score_point_first")
        self.score_point_second = QtWidgets.QLabel(self.frame)
        self.score_point_second.setGeometry(QtCore.QRect(350, 270, 71, 51))
        self.score_point_second.setStyleSheet("#score_point_second {\n"
"    border: 2px solid #ffa100;\n"
"    border-radius: 25px;\n"
"    color: white;\n"
"    font-size: 32px;\n"
"    background-color: #8c5900;\n"
"}")
        self.score_point_second.setAlignment(QtCore.Qt.AlignCenter)
        self.score_point_second.setObjectName("score_point_second")
        self.button_back = QtWidgets.QPushButton(self.frame)
        self.button_back.setGeometry(QtCore.QRect(10, 10, 49, 49))
        self.button_back.setStyleSheet("#button_back {\n"
"    background-color: transparent;\n"
"    border: 0;\n"
"}")
        self.button_back.setText("")
        self.button_back.setObjectName("button_back")
        self.frame_home = QtWidgets.QFrame(Form)
        self.frame_home.setGeometry(QtCore.QRect(0, 0, 481, 801))
        self.frame_home.setStyleSheet("#frame_home {\n"
"    background-color: #222222;\n"
"}")
        self.frame_home.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_home.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_home.setObjectName("frame_home")
        self.icon_place = QtWidgets.QPushButton(self.frame_home)
        self.icon_place.setGeometry(QtCore.QRect(110, 140, 256, 256))
        self.icon_place.setStyleSheet("#icon_place {\n"
"    background-color: transparent;\n"
"    border: 0;\n"
"}")
        self.icon_place.setText("")
        self.icon_place.setObjectName("icon_place")
        self.button_one_player = QtWidgets.QPushButton(self.frame_home)
        self.button_one_player.setGeometry(QtCore.QRect(70, 470, 351, 61))
        self.button_one_player.setStyleSheet("#button_one_player {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    background-color: #ffffff;\n"
"    border: 5px solid #354aff;\n"
"    color: #354aff;\n"
"    font-size: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#button_one_player:hover {\n"
"    background-color: #354aff;\n"
"    border: 5px solid #ffffff;\n"
"    color: #ffffff;\n"
"    font-size: 23px;\n"
"}\n"
"\n"
"#button_one_player:pressed {\n"
"    background-color: #1128f6;\n"
"}\n"
"\n"
"")
        self.button_one_player.setObjectName("button_one_player")
        self.tic_tac_toe_label_2 = QtWidgets.QLabel(self.frame_home)
        self.tic_tac_toe_label_2.setGeometry(QtCore.QRect(60, 20, 361, 91))
        self.tic_tac_toe_label_2.setStyleSheet("#tic_tac_toe_label_2 {\n"
"    font: 75 italic 11pt \"Z003\"; \n"
"    color: white;\n"
"    font-size: 50px;\n"
"}")
        self.tic_tac_toe_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.tic_tac_toe_label_2.setObjectName("tic_tac_toe_label_2")
        self.button_two_players = QtWidgets.QPushButton(self.frame_home)
        self.button_two_players.setGeometry(QtCore.QRect(70, 610, 351, 61))
        self.button_two_players.setStyleSheet("#button_two_players {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    background-color: #ffffff;\n"
"    border: 5px solid #ff3f3f;\n"
"    color: #ff3f3f;\n"
"    font-size: 20px;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"#button_two_players:hover {\n"
"    background-color: #ff3f3f;\n"
"    border: 5px solid #ffffff;\n"
"    color: #ffffff;\n"
"    font-size: 23px;\n"
"}\n"
"\n"
"#button_two_players:pressed {\n"
"    background-color: #ff0000;\n"
"}\n"
"\n"
"")
        self.button_two_players.setObjectName("button_two_players")
        self.coded_by_label_2 = QtWidgets.QLabel(self.frame_home)
        self.coded_by_label_2.setGeometry(QtCore.QRect(110, 750, 261, 41))
        self.coded_by_label_2.setStyleSheet("#coded_by_label_2 {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    color: white;\n"
"    font-size: 24px;\n"
"    background-color: transparent;\n"
"    margin-left: 25px;\n"
"}")
        self.coded_by_label_2.setObjectName("coded_by_label_2")
        self.tivole_label_2 = QtWidgets.QLabel(self.frame_home)
        self.tivole_label_2.setGeometry(QtCore.QRect(250, 750, 121, 41))
        self.tivole_label_2.setStyleSheet("#tivole_label_2 {\n"
"    font: 75 bold 11pt \"Cantarell\";\n"
"    color: #00ff2d;\n"
"    font-size: 24px;\n"
"    background-color: transparent;\n"
"}")
        self.tivole_label_2.setObjectName("tivole_label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MainWindow"))
        self.tic_tac_toe_label.setText(_translate("Form", "Tic Tac Toe"))
        self.coded_by_label.setText(_translate("Form", "Coded by"))
        self.tivole_label.setText(_translate("Form", "tivole"))
        self.pick_to_start_label.setText(_translate("Form", "Pick X or O to Start"))
        self.X_button.setText(_translate("Form", "X"))
        self.O_button.setText(_translate("Form", "O"))
        self.start_reset_button.setText(_translate("Form", "START"))
        self.which_turn_label.setText(_translate("Form", "Computer\'s turn"))
        self.score_round.setText(_translate("Form", "<html><head/><body><p>Round<br/>1</p></body></html>"))
        self.score_second.setText(_translate("Form", "Player 2"))
        self.score_first.setText(_translate("Form", "Player 1"))
        self.score_point_first.setText(_translate("Form", "0"))
        self.score_point_second.setText(_translate("Form", "0"))
        self.button_one_player.setText(_translate("Form", "One Player"))
        self.tic_tac_toe_label_2.setText(_translate("Form", "Tic Tac Toe"))
        self.button_two_players.setText(_translate("Form", "Two Players"))
        self.coded_by_label_2.setText(_translate("Form", "Coded by"))
        self.tivole_label_2.setText(_translate("Form", "tivole"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

