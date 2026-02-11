import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners.keypad import MatrixScanner
from kmk.scanners import DiodeOrientation

# split side
isRight = True

class KMKKeyboard(_KMKKeyboard):
    def __init__(self):
        super().__init__()
        
        # create and register the scanner
        # create and register the scanner
        if isRight:
            self.col_pins = (board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,)
            self.row_pins = (board.GP7, board.GP8, board.GP9, board.GP10, board.GP11)
        else:
            self.col_pins = (board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6)
            self.row_pins = (board.GP7, board.GP8, board.GP9, board.GP10, board.GP11)
        self.diode_orientation = DiodeOrientation.COL2ROW

