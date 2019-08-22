import sys
from PyQt5.QtWidgets import QApplication
from tictactoe import TicTacToe_Main_Window

app = QApplication(sys.argv)

Ti_TicTacToe = TicTacToe_Main_Window()

sys.exit(app.exec_())