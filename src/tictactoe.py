from PyQt5 import QtWidgets, QtGui, QtCore
from tictactoe_ui import Ui_Form

class TicTacToe_Main_Window(QtWidgets.QMainWindow, Ui_Form):

    multiplayer = True
    Player_1_score = 0
    Player_2_score = 0
    Player_1_name = 'Player'
    Player_2_name = 'Player'
    which_round = 1
    player = 'x'
    opponent = 'o'
    is_computers_turn = False
    is_second_players_turn = False
    is_game_started = False
    game_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Tic Tac Toe')
        self.setWindowIcon(QtGui.QIcon('img/icon.png'))
        self.setFixedSize(self.size())

        self.frame.setVisible(False)
        # self.pushButton_A.hide()
        
        self.show()

        # Set player names
        self.which_turn_label.setText('Choose X or O')
        self.score_point_first.setText(str(self.Player_1_score))
        self.score_point_second.setText(str(self.Player_2_score))
        self.score_first.setText(self.Player_1_name)
        self.score_second.setText(self.Player_2_name)

        # Connecting Tic Tac Toe buttons
        self.button_1.clicked.connect(self.TTT_button_pressed)
        self.button_2.clicked.connect(self.TTT_button_pressed)
        self.button_3.clicked.connect(self.TTT_button_pressed)
        self.button_4.clicked.connect(self.TTT_button_pressed)
        self.button_5.clicked.connect(self.TTT_button_pressed)
        self.button_6.clicked.connect(self.TTT_button_pressed)
        self.button_7.clicked.connect(self.TTT_button_pressed)
        self.button_8.clicked.connect(self.TTT_button_pressed)
        self.button_9.clicked.connect(self.TTT_button_pressed)

        self.X_button.clicked.connect(self.X_or_O_check_pressed)
        self.O_button.clicked.connect(self.X_or_O_check_pressed)

        self.X_button.setCheckable(True)
        self.O_button.setCheckable(True)

        self.X_button.setChecked(True)

        self.start_reset_button.clicked.connect(self.start_reset_button_pressed)

        self.button_back.setIcon(QtGui.QIcon('img/left-arrow.png'))
        self.button_back.setIconSize(QtCore.QSize(36, 49))

        self.icon_place.setIcon(QtGui.QIcon('img/icon.png'))
        self.icon_place.setIconSize(QtCore.QSize(256, 256))

        self.button_one_player.clicked.connect(self.button_one_player_pressed)
        self.button_two_players.clicked.connect(self.button_two_players_pressed)
        self.button_back.clicked.connect(self.button_back_pressed)


    def button_one_player_pressed(self):
        self.frame_home.setVisible(False)
        self.frame.setVisible(True)
        self.multiplayer = False
        self.reset_everything()


    def button_two_players_pressed(self):
        self.frame_home.setVisible(False)
        self.frame.setVisible(True)
        self.multiplayer = True
        self.reset_everything()


    def reset_everything(self):
        self.is_game_started = False
        self.Player_1_score = 0
        self.Player_2_score = 0
        self.which_round = 1

        self.which_turn_label.setText('Choose X or O')
        self.start_reset_button.setText('START')

        self.button_1.setIcon(QtGui.QIcon())
        self.button_2.setIcon(QtGui.QIcon())
        self.button_3.setIcon(QtGui.QIcon())
        self.button_4.setIcon(QtGui.QIcon())
        self.button_5.setIcon(QtGui.QIcon())
        self.button_6.setIcon(QtGui.QIcon())
        self.button_7.setIcon(QtGui.QIcon())
        self.button_8.setIcon(QtGui.QIcon())
        self.button_9.setIcon(QtGui.QIcon())

        self.Player_1_name = 'Player 1'
        self.Player_2_name = 'Computer' if not self.multiplayer else 'Player 2'

        self.score_first.setText(self.Player_1_name)
        self.score_second.setText(self.Player_2_name)

        self.score_point_first.setText(str(self.Player_1_score))
        self.score_point_second.setText(str(self.Player_2_score))
        self.score_round.setText('<html><head/><body><p>Round<br/>' + str(self.which_round) + '</p></body></html>')

        self.start_reset_button.setStyleSheet("""
            #start_reset_button {
                /* START version */
                background-color: #00bb00;
                color: white;
                font-size: 16px;
                border-radius: 15px;
                border: 3px solid #00ff47;
            }


            #start_reset_button:pressed {
                background-color: #00aa00;
            }
        """)



    def button_back_pressed(self):
        self.frame_home.setVisible(True)
        self.frame.setVisible(False)



    def TTT_button_pressed(self):

        if self.is_game_started:
            if not self.multiplayer: 
                if not self.is_computers_turn:
                    button = self.sender()

                    if button == self.button_1:
                        if self.game_board[0][0] == '_':
                            self.game_board[0][0] = self.opponent
                            if self.opponent == 'o':
                                self.button_1.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_1.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_1.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False


                    elif button == self.button_2:
                        if self.game_board[0][1] == '_':
                            self.game_board[0][1] = self.opponent
                            if self.opponent == 'o':
                                self.button_2.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_2.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_2.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False
                    

                    elif button == self.button_3:
                        if self.game_board[0][2] == '_':
                            self.game_board[0][2] = self.opponent
                            if self.opponent == 'o':
                                self.button_3.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_3.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_3.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False


                    elif button == self.button_4:
                        if self.game_board[1][0] == '_':
                            self.game_board[1][0] = self.opponent
                            if self.opponent == 'o':
                                self.button_4.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_4.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_4.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False


                    elif button == self.button_5:
                        if self.game_board[1][1] == '_':
                            self.game_board[1][1] = self.opponent
                            if self.opponent == 'o':
                                self.button_5.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_5.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_5.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False
                            

                    elif button == self.button_6:
                        if self.game_board[1][2] == '_':
                            self.game_board[1][2] = self.opponent
                            if self.opponent == 'o':
                                self.button_6.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_6.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_6.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False


                    elif button == self.button_7:
                        if self.game_board[2][0] == '_':
                            self.game_board[2][0] = self.opponent
                            if self.opponent == 'o':
                                self.button_7.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_7.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_7.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False


                    elif button == self.button_8:
                        if self.game_board[2][1] == '_':
                            self.game_board[2][1] = self.opponent
                            if self.opponent == 'o':
                                self.button_8.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_8.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_8.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False


                    elif button == self.button_9:
                        if self.game_board[2][2] == '_':
                            self.game_board[2][2] = self.opponent
                            if self.opponent == 'o':
                                self.button_9.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_9.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_9.setIconSize(QtCore.QSize(64, 64))
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                move = self.findBestMove(self.game_board)
                                self.game_board[move[0]][move[1]] = self.player
                                self.compMove(move)
                                result = self.check_game_over()
                                if result == 'x':
                                    self.X_WON()
                                elif result == 'o':
                                    self.O_WON()
                                elif result == 'd':

                                    self.which_turn_label.setText('Draw')
                                    self.is_game_started = False
            else:
                button = self.sender()

                if button == self.button_1:
                    if self.game_board[0][0] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[0][0] = self.opponent
                            if self.opponent == 'o':
                                self.button_1.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_1.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_1.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[0][0] = self.player
                            if self.player == 'o':
                                self.button_1.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_1.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_1.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')

                        
                elif button == self.button_2:
                    if self.game_board[0][1] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[0][1] = self.opponent
                            if self.opponent == 'o':
                                self.button_2.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_2.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_2.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[0][1] = self.player
                            if self.player == 'o':
                                self.button_2.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_2.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_2.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')
                

                elif button == self.button_3:
                    if self.game_board[0][2] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[0][2] = self.opponent
                            if self.opponent == 'o':
                                self.button_3.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_3.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_3.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[0][2] = self.player
                            if self.player == 'o':
                                self.button_3.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_3.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_3.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')


                elif button == self.button_4:
                    if self.game_board[1][0] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[1][0] = self.opponent
                            if self.opponent == 'o':
                                self.button_4.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_4.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_4.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[1][0] = self.player
                            if self.player == 'o':
                                self.button_4.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_4.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_4.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')


                elif button == self.button_5:
                    if self.game_board[1][1] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[1][1] = self.opponent
                            if self.opponent == 'o':
                                self.button_5.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_5.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_5.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[1][1] = self.player
                            if self.player == 'o':
                                self.button_5.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_5.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_5.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')
                        

                elif button == self.button_6:
                    if self.game_board[1][2] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[1][2] = self.opponent
                            if self.opponent == 'o':
                                self.button_6.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_6.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_6.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[1][2] = self.player
                            if self.player == 'o':
                                self.button_6.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_6.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_6.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')
                        

                elif button == self.button_7:
                    if self.game_board[2][0] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[2][0] = self.opponent
                            if self.opponent == 'o':
                                self.button_7.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_7.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_7.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[2][0] = self.player
                            if self.player == 'o':
                                self.button_7.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_7.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_7.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')
        

                elif button == self.button_8:
                    if self.game_board[2][1] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[2][1] = self.opponent
                            if self.opponent == 'o':
                                self.button_8.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_8.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_8.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[2][1] = self.player
                            if self.player == 'o':
                                self.button_8.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_8.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_8.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')
                        

                elif button == self.button_9:
                    if self.game_board[2][2] == '_':
                        if not self.is_second_players_turn:
                            self.game_board[2][2] = self.opponent
                            if self.opponent == 'o':
                                self.button_9.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_9.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_9.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = True
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_2_name + '\'s turn')
                        else:
                            self.game_board[2][2] = self.player
                            if self.player == 'o':
                                self.button_9.setIcon(QtGui.QIcon('img/O.png'))
                            else:
                                self.button_9.setIcon(QtGui.QIcon('img/X.png'))
                            self.button_9.setIconSize(QtCore.QSize(64, 64))
                            self.is_second_players_turn = False
                            result = self.check_game_over()
                            if result == 'x':
                                self.X_WON()
                            elif result == 'o':
                                self.O_WON()
                            elif result == 'd':
                                self.which_turn_label.setText('Draw')
                                self.is_game_started = False
                            else:
                                self.which_turn_label.setText(self.Player_1_name + '\'s turn')

    
    def X_WON(self):
        if self.opponent == 'x':
            self.Player_1_score += 1
            self.score_point_first.setText(str(self.Player_1_score))
            self.which_turn_label.setText(self.Player_1_name + ' Wins')
        else:
            self.Player_2_score += 1
            self.score_point_second.setText(str(self.Player_2_score))
            self.which_turn_label.setText(self.Player_2_name + ' Wins')
        self.is_game_started = False


    def O_WON(self):
        
        if self.opponent == 'o':
            self.Player_1_score += 1
            self.score_point_first.setText(str(self.Player_1_score))
            self.which_turn_label.setText(self.Player_1_name + ' Wins')
        else:
            self.Player_2_score += 1
            self.score_point_second.setText(str(self.Player_2_score))
            self.which_turn_label.setText(self.Player_2_name + ' Wins')
        self.is_game_started = False


    def X_or_O_check_pressed(self):

        button = self.sender()

        if button.text() == 'X':
            self.X_button.setChecked(True)
            self.O_button.setChecked(False)
            
            self.X_button.setStyleSheet("""
                #X_button {
                    font: 75 bold 11pt "Cantarell";
                    background-color: green;
                    color: #ffffff;
                    border-radius: 8px;
                    border: 2px solid #eeeeee;
                    font-size: 30px;
                }
            """)

            self.O_button.setStyleSheet("""
                #O_button {
                    font: 75 bold 11pt "Cantarell";
                    background-color: #444444;
                    color: #ffffff;
                    border-radius: 8px;
                    border: 2px solid #eeeeee;
                    font-size: 30px;
                }
            """)
        else:
            self.X_button.setChecked(False)
            self.O_button.setChecked(True)

            self.O_button.setStyleSheet("""
                #O_button {
                    font: 75 bold 11pt "Cantarell";
                    background-color: green;
                    color: #ffffff;
                    border-radius: 8px;
                    border: 2px solid #eeeeee;
                    font-size: 30px;
                }
            """)

            self.X_button.setStyleSheet("""
                #X_button {
                    font: 75 bold 11pt "Cantarell";
                    background-color: #444444;
                    color: #ffffff;
                    border-radius: 8px;
                    border: 2px solid #eeeeee;
                    font-size: 30px;
                }
            """)


    def start_reset_button_pressed(self):

        self.button_1.setIcon(QtGui.QIcon())
        self.button_2.setIcon(QtGui.QIcon())
        self.button_3.setIcon(QtGui.QIcon())
        self.button_4.setIcon(QtGui.QIcon())
        self.button_5.setIcon(QtGui.QIcon())
        self.button_6.setIcon(QtGui.QIcon())
        self.button_7.setIcon(QtGui.QIcon())
        self.button_8.setIcon(QtGui.QIcon())
        self.button_9.setIcon(QtGui.QIcon())

        self.start_reset_button.setStyleSheet("""
                #start_reset_button {
                    /* RESET version */
                    background-color: #bb0000;
                    color: white;
                    font-size: 16px;
                    border-radius: 15px;
                    border: 3px solid #ff0000;
                }
                
                #start_reset_button:pressed {
                    background-color: #970000;
                }
            """)

        if self.start_reset_button.text() == 'RESET':
            self.which_round += 1
            self.score_round.setText('<html><head/><body><p>Round<br/>' + str(self.which_round) + '</p></body></html>')
        
        self.start_reset_button.setText('RESET')

        self.is_game_started = True

        self.game_board = [['_', '_', '_'], ['_', '_', '_'], ['_', '_', '_']]

        if self.O_button.isChecked():
            self.player = 'x'
            self.opponent = 'o'
            self.which_turn_label.setText(self.Player_2_name + '\'s turn')

            self.is_second_players_turn = True

            if not self.multiplayer:
                move = (0, 0)
                self.game_board[move[0]][move[1]] = self.player
                self.compMove(move)
                self.is_computers_turn = False
                self.which_turn_label.setText(self.Player_1_name + '\'s turn')

        else:
            self.is_computers_turn = False
            self.is_second_players_turn = False
            self.player = 'o'
            self.opponent = 'x'
            self.which_turn_label.setText(self.Player_1_name + '\'s turn')


    def compMove(self, move):
        if move == (0, 0):
            if self.player == 'x':
                self.button_1.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_1.setIcon(QtGui.QIcon('img/O.png'))
            self.button_1.setIconSize(QtCore.QSize(64, 64))
        elif move == (0, 1):
            if self.player == 'x':
                self.button_2.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_2.setIcon(QtGui.QIcon('img/O.png'))
            self.button_2.setIconSize(QtCore.QSize(64, 64))
        elif move == (0, 2):
            if self.player == 'x':
                self.button_3.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_3.setIcon(QtGui.QIcon('img/O.png'))
            self.button_3.setIconSize(QtCore.QSize(64, 64))
        elif move == (1, 0):
            if self.player == 'x':
                self.button_4.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_4.setIcon(QtGui.QIcon('img/O.png'))
            self.button_4.setIconSize(QtCore.QSize(64, 64))
        elif move == (1, 1):
            if self.player == 'x':
                self.button_5.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_5.setIcon(QtGui.QIcon('img/O.png'))
            self.button_5.setIconSize(QtCore.QSize(64, 64))
        elif move == (1, 2):
            if self.player == 'x':
                self.button_6.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_6.setIcon(QtGui.QIcon('img/O.png'))
            self.button_6.setIconSize(QtCore.QSize(64, 64))
        elif move == (2, 0):
            if self.player == 'x':
                self.button_7.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_7.setIcon(QtGui.QIcon('img/O.png'))
            self.button_7.setIconSize(QtCore.QSize(64, 64))
        elif move == (2, 1):
            if self.player == 'x':
                self.button_8.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_8.setIcon(QtGui.QIcon('img/O.png'))
            self.button_8.setIconSize(QtCore.QSize(64, 64))
        elif move == (2, 2):
            if self.player == 'x':
                self.button_9.setIcon(QtGui.QIcon('img/X.png'))
            else:
                self.button_9.setIcon(QtGui.QIcon('img/O.png'))
            self.button_9.setIconSize(QtCore.QSize(64, 64))


    def check_game_over(self):
        
        if self.game_board[0][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][2] and self.game_board[2][2] == 'o':
            return 'o'
        elif self.game_board[0][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][2] and self.game_board[2][2] == 'x':
            """
                * _ _
                _ * _
                _ _ *
            """
            return 'x'
        
        elif self.game_board[0][0] == self.game_board[0][1] and self.game_board[0][1] == self.game_board[0][2] and self.game_board[0][2] == 'o':
            return 'o'
        elif self.game_board[0][0] == self.game_board[0][1] and self.game_board[0][1] == self.game_board[0][2] and self.game_board[0][2] == 'x':
            """
                * * *
                _ _ _
                _ _ _
            """
            return 'x'

        elif self.game_board[1][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[1][2] and self.game_board[1][2] == 'o':
            return 'o'
        elif self.game_board[1][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[1][2] and self.game_board[1][2] == 'x':
            """
                _ _ _
                * * *
                _ _ _
            """
            return 'x'
        
        elif self.game_board[2][0] == self.game_board[2][1] and self.game_board[2][1] == self.game_board[2][2] and self.game_board[2][2] == 'o':
            return 'o'
        elif self.game_board[2][0] == self.game_board[2][1] and self.game_board[2][1] == self.game_board[2][2] and self.game_board[2][2] == 'x':
            """
                _ _ _
                _ _ _
                * * *
            """
            return 'x'
        
        elif self.game_board[0][2] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][0] and self.game_board[2][0] == 'o':
            return 'o'
        elif self.game_board[0][2] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][0] and self.game_board[2][0] == 'x':
            """
                _ _ *
                _ * _
                * _ _
            """
            return 'x'
        
        elif self.game_board[0][0] == self.game_board[1][0] and self.game_board[1][0] == self.game_board[2][0] and self.game_board[2][0] == 'o':
            return 'o'
        elif self.game_board[0][0] == self.game_board[1][0] and self.game_board[1][0] == self.game_board[2][0] and self.game_board[2][0] == 'x':
            """
                * _ _
                * _ _
                * _ _
            """
            return 'x'
        
        elif self.game_board[0][1] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][1] and self.game_board[2][1] == 'o':
            return 'o'
        elif self.game_board[0][1] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][1] and self.game_board[2][1] == 'x':
            """
                _ * _
                _ * _
                _ * _
            """
            return 'x'

        elif self.game_board[0][2] == self.game_board[1][2] and self.game_board[1][2] == self.game_board[2][2] and self.game_board[2][2] == 'o':
            return 'o'
        elif self.game_board[0][2] == self.game_board[1][2] and self.game_board[1][2] == self.game_board[2][2] and self.game_board[2][2] == 'x':
            """
                _ _ *
                _ _ *
                _ _ *
            """
            return 'x'
        
        elif self.game_board[0][0] == '_' or self.game_board[0][1] == '_' or self.game_board[0][2] == '_' or self.game_board[1][0] == '_' or self.game_board[1][1] == '_' or self.game_board[1][2] == '_' or self.game_board[2][0] == '_' or self.game_board[2][1] == '_' or self.game_board[2][2] == '_':
            return 'c'
        else:
            return 'd'


    def isMovesLeft(self, game_board):
        for i in range(3):
            for j in range(3):
                if game_board[i][j] == '_':
                    return True
        return False


    def evaluate(self, b):
        for row in range(3):
            if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
                if b[row][0] == self.player:
                    return +10
                elif b[row][0] == self.opponent:
                    return -10

        for col in range(3):
            if b[0][col] == b[1][col] and b[1][col] == b[2][col]:
                if b[0][col] == self.player:
                    return +10
                elif b[0][col] == self.opponent:
                    return -10

        if b[0][0] == b[1][1] and b[1][1] == b[2][2]:
            if b[0][0] == self.player:
                return +10
            elif b[0][0] == self.opponent:
                return -10

        if b[0][2] == b[1][1] and b[1][1] == b[2][0]:
            if b[0][2] == self.player:
                return +10
            elif b[0][2] == self.opponent:
                return -10

        return 0


    def minimax(self, game_board, depth, isMax):
        score = self.evaluate(game_board)

        if score == 10 or score == -10:
            return score
        
        if not self.isMovesLeft(game_board):
            return 0

        if isMax:
            best = -1000

            for i in range(3):
                for j in range(3):
                    if game_board[i][j] == '_':
                        game_board[i][j] = self.player
                        best = max(best, self.minimax(game_board, depth + 1, not isMax))
                        game_board[i][j] = '_'

            return best
        else:
            best = 1000

            for i in range(3):
                for j in range(3):
                    if game_board[i][j] == '_':
                        game_board[i][j] = self.opponent
                        best = min(best, self.minimax(game_board, depth + 1, not isMax))
                        game_board[i][j] = '_'

            return best


    def findBestMove(self, game_board):
        bestVal = -1000

        for i in range(3):
            for j in range(3):
                if game_board[i][j] == '_':
                    game_board[i][j] = self.player
                    moveVal = self.minimax(game_board, 0, False)

                    game_board[i][j] = '_'

                    if moveVal > bestVal:
                        bestMove = (i, j)
                        bestVal = moveVal

        return bestMove