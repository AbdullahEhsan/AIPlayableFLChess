from math import floor
from typing import Tuple
from xmlrpc.client import Boolean
from PyQt5.QtCore import Qt, QPoint, QSize, QTimer, QCoreApplication, QDir, QUrl
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QPushButton, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, \
    QComboBox, QRadioButton, QButtonGroup
from PyQt5.QtGui import QPixmap, QMouseEvent, QFont, QMovie, QIcon
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEnginePage
from qpageview import view

from ChessAI import AIFunctions

from ChessGame import Game as chess_game

game_over = False
ai_turn = False
screentheme = "default"

def make_larger(self):
    global squareSize, wSizew, wSizeh, sbSizew, bSizew, bSizeh, lSizew, lSizeh, blSizeh, helpScreenWidth, helpScreenHeight, themeButtonWidth
    global themeButtonHeight, sizeSelectWidth, sizeSelectHeight, welcomeTextOffsetY, welcomeTextW, welcomeTextH, okayButtonOffsetY
    global whiteTeamTextOffsetX, whiteTeamTextOffsetY, blackTeamTextOffsetY, highlightTextOffsetY, gameTypeTextOffsetY, radioButtonTextCSS
    global whiteButtonH, whiteButtonOffsetX, whiteButtonOffsetY, whiteButtonAIOffsetY, blackButtonOffsetY, blackButtonAIOffsetY, highlightButtonOffsetY
    global highlightOffButtonOffsetY, gameTypeButtonOffsetY, gameTypeCorpButtonOffsetY, optionScreenOffsetX, optionScreenOffsetY, tableOptionOffsetX
    global tableOptionOffsetY1, tableOptionOffsetY2, reStartbuttonfsize, corpButtonOffsetX, corpButtonOffsetY, capWhiteOffsetX, capWhiteOffsetY
    global whiteBoxOffsetX, whiteBoxOffsetY, whiteBoxH, whiteBoxW, capBlackOffsetX, capBlackOffsetY, blackBoxOffsetY, endButtonOffsetX
    global endButtonOffsetY1, endButtonOffsetY2, restartButtonOffsetY, startButtonOffsetY

    global screenSize,screentheme

    screenSize = "large"
    # large
    squareSize = 95
    # window size
    wSizew = 1150
    wSizeh = 855
    # Button Size
    sbSizew = 180
    bSizew = 210
    bSizeh = 50
    # Lable Size
    lSizew = 230
    lSizeh = 30
    blSizeh = 120
    # helper screen
    helpScreenWidth = 750
    helpScreenHeight = 800
    # theme selector
    themeButtonWidth = 65
    themeButtonHeight = 65
    sizeSelectWidth = 65
    sizeSelectHeight = 65
    # wSizew = 725
    # wSizeh = 520

    # Start screen
    welcomeTextOffsetY = 375
    welcomeTextW = 1125
    welcomeTextH = 160
    okayButtonOffsetY = 350

    whiteTeamTextOffsetX = 260
    whiteTeamTextOffsetY = 215
    blackTeamTextOffsetY = 120
    highlightTextOffsetY = 0
    gameTypeTextOffsetY = 120

    radioButtonTextCSS = 'color: white; font-size: 16px'
    whiteButtonH = 0.5
    whiteButtonOffsetX = -20
    whiteButtonOffsetY = 160
    whiteButtonAIOffsetY = 125
    blackButtonOffsetY = 60
    blackButtonAIOffsetY = 25
    highlightButtonOffsetY = 55
    highlightOffButtonOffsetY = 90
    gameTypeButtonOffsetY = 180
    gameTypeCorpButtonOffsetY = 215
    # optionScreen offset
    # optionScreenOffsetX = 240
    # optionScreenOffsetY = 200
    optionScreenOffsetX = 250
    optionScreenOffsetY = 220
    # tableOption offset
    tableOptionOffsetX = 15
    tableOptionOffsetY1 = 95
    tableOptionOffsetY2 = 30
    reStartbuttonfsize = 0.9
    corpButtonOffsetX = 60
    corpButtonOffsetY = 35
    capWhiteOffsetX = 70
    capWhiteOffsetY = 510
    whiteBoxOffsetX = 12
    whiteBoxOffsetY = 545
    whiteBoxW = 230
    whiteBoxH = 180
    capBlackOffsetX = 70
    capBlackOffsetY = 135
    blackBoxOffsetY = 165
    endButtonOffsetX = 60
    endButtonOffsetY1 = 330
    endButtonOffsetY2 = 30
    restartButtonOffsetY = 395
    startButtonOffsetY = 320

def make_smaller(self):
    global squareSize, wSizew, wSizeh, sbSizew, bSizew, bSizeh, lSizew, lSizeh, blSizeh, helpScreenWidth, helpScreenHeight, themeButtonWidth
    global themeButtonHeight, sizeSelectWidth, sizeSelectHeight, welcomeTextOffsetY, welcomeTextW, welcomeTextH, okayButtonOffsetY
    global whiteTeamTextOffsetX, whiteTeamTextOffsetY, blackTeamTextOffsetY, highlightTextOffsetY, gameTypeTextOffsetY, radioButtonTextCSS
    global whiteButtonH, whiteButtonOffsetX, whiteButtonOffsetY, whiteButtonAIOffsetY, blackButtonOffsetY, blackButtonAIOffsetY, highlightButtonOffsetY
    global highlightOffButtonOffsetY, gameTypeButtonOffsetY, gameTypeCorpButtonOffsetY, optionScreenOffsetX, optionScreenOffsetY, tableOptionOffsetX
    global tableOptionOffsetY1, tableOptionOffsetY2, reStartbuttonfsize, corpButtonOffsetX, corpButtonOffsetY, capWhiteOffsetX, capWhiteOffsetY
    global whiteBoxOffsetX, whiteBoxOffsetY, whiteBoxH, whiteBoxW, capBlackOffsetX, capBlackOffsetY, blackBoxOffsetY, endButtonOffsetX
    global endButtonOffsetY1, endButtonOffsetY2, restartButtonOffsetY, startButtonOffsetY
    global screenSize,screentheme

    screenSize = "small"
    # Small window
    squareSize = 55
    # window size
    wSizew = 700
    wSizeh = 495
    # Button Size
    sbSizew = 120
    bSizew = 150
    bSizeh = 30
    # Lable Size
    lSizew = 170
    lSizeh = 20
    blSizeh = 80
    # helper screen
    helpScreenWidth = 450
    helpScreenHeight = 400
    # wSizew = 725
    # wSizeh = 520
    # theme button selector
    themeButtonWidth = 35
    themeButtonHeight = 35
    sizeSelectWidth = 35
    sizeSelectHeight = 35
    # Start screen
    welcomeTextOffsetY = 225
    welcomeTextW = 675
    welcomeTextH = 80
    okayButtonOffsetY = 150
    whiteTeamTextOffsetX = 175
    whiteTeamTextOffsetY = 135
    blackTeamTextOffsetY = 70
    highlightTextOffsetY = 10
    gameTypeTextOffsetY = 50
    radioButtonTextCSS = 'color: white; font-size: 14px'
    whiteButtonH = 0.3
    whiteButtonOffsetX = 50
    whiteButtonOffsetY = 100
    whiteButtonAIOffsetY = 75
    blackButtonOffsetY = 40
    blackButtonAIOffsetY = 15
    highlightButtonOffsetY = 25
    highlightOffButtonOffsetY = 50
    gameTypeButtonOffsetY = 80
    gameTypeCorpButtonOffsetY = 105
    # optionScreen offset
    optionScreenOffsetX = 120
    optionScreenOffsetY = 100
    # tableOption offset
    tableOptionOffsetX = 5
    tableOptionOffsetY1 = 55
    tableOptionOffsetY2 = 10
    reStartbuttonfsize = 0.5
    corpButtonOffsetX = 40
    corpButtonOffsetY = 15
    capWhiteOffsetX = 50
    capWhiteOffsetY = 270
    whiteBoxOffsetX = 8
    whiteBoxOffsetY = 295
    whiteBoxW = 170
    whiteBoxH = 100
    capBlackOffsetX = 50
    capBlackOffsetY = 55
    blackBoxOffsetY = 85
    endButtonOffsetX = 40
    endButtonOffsetY1 = 170
    endButtonOffsetY2 = 10
    restartButtonOffsetY = 205
    startButtonOffsetY = 180

def make_default(self):
    global squareSize, wSizew, wSizeh, sbSizew, bSizew, bSizeh, lSizew, lSizeh, blSizeh, helpScreenWidth, helpScreenHeight, themeButtonWidth
    global themeButtonHeight, sizeSelectWidth, sizeSelectHeight, welcomeTextOffsetY, welcomeTextW, welcomeTextH, okayButtonOffsetY
    global whiteTeamTextOffsetX, whiteTeamTextOffsetY, blackTeamTextOffsetY, highlightTextOffsetY, gameTypeTextOffsetY, radioButtonTextCSS
    global whiteButtonH, whiteButtonOffsetX, whiteButtonOffsetY, whiteButtonAIOffsetY, blackButtonOffsetY, blackButtonAIOffsetY, highlightButtonOffsetY
    global highlightOffButtonOffsetY, gameTypeButtonOffsetY, gameTypeCorpButtonOffsetY, optionScreenOffsetX, optionScreenOffsetY, tableOptionOffsetX
    global tableOptionOffsetY1, tableOptionOffsetY2, reStartbuttonfsize, corpButtonOffsetX, corpButtonOffsetY, capWhiteOffsetX, capWhiteOffsetY
    global whiteBoxOffsetX, whiteBoxOffsetY, whiteBoxH, whiteBoxW, capBlackOffsetX, capBlackOffsetY, blackBoxOffsetY, endButtonOffsetX
    global endButtonOffsetY1, endButtonOffsetY2, restartButtonOffsetY, startButtonOffsetY
    global screenSize,screentheme

    screenSize = "default"
    # Medium
    squareSize = 75
    # window size
    wSizew = 925
    wSizeh = 675
    # Button Size
    sbSizew = 150
    bSizew = 180
    bSizeh = 40
    # Lable Size
    lSizew = 200
    lSizeh = 25
    blSizeh = 100
    # helper screen
    helpScreenWidth = 600
    helpScreenHeight = 600
    # theme selector
    themeButtonWidth = 50
    themeButtonHeight = 50
    sizeSelectWidth = 50
    sizeSelectHeight = 50
    # wSizew = 725
    # wSizeh = 520
    # Start screen
    welcomeTextOffsetY = 300
    welcomeTextW = 900
    welcomeTextH = 100
    okayButtonOffsetY = 250
    whiteTeamTextOffsetX = 200
    whiteTeamTextOffsetY = 175
    blackTeamTextOffsetY = 95
    highlightTextOffsetY = 5
    gameTypeTextOffsetY = 85
    radioButtonTextCSS = 'color: white; font-size: 15px'
    whiteButtonH = 0.4
    whiteButtonOffsetX = 0
    whiteButtonOffsetY = 130
    whiteButtonAIOffsetY = 100
    blackButtonOffsetY = 40
    blackButtonAIOffsetY = 10
    highlightButtonOffsetY = 50
    highlightOffButtonOffsetY = 80
    gameTypeButtonOffsetY = 140
    gameTypeCorpButtonOffsetY = 170
    # optionScreen offset
    optionScreenOffsetX = 180
    optionScreenOffsetY = 150
    # tableOption offset
    tableOptionOffsetX = 10
    tableOptionOffsetY1 = 75
    tableOptionOffsetY2 = 20
    reStartbuttonfsize = 0.7
    corpButtonOffsetX = 50
    corpButtonOffsetY = 25
    capWhiteOffsetX = 60
    capWhiteOffsetY = 390
    whiteBoxOffsetX = 10
    whiteBoxOffsetY = 420
    whiteBoxW = 200
    whiteBoxH = 140
    capBlackOffsetX = 60
    capBlackOffsetY = 95
    blackBoxOffsetY = 125
    endButtonOffsetX = 50
    endButtonOffsetY1 = 250
    endButtonOffsetY2 = 20
    restartButtonOffsetY = 300
    startButtonOffsetY = 250

def corp_to_color(corp_num):
    colors = ['', 'rd', 'bl', 'gr']
    return colors[corp_num]

def board_to_screen(x, y, size):
    new_x = (x+1) * size
    new_y = (y+1) * size
    return (new_x, new_y)

def screen_to_board(x, y, size):
    b_x = int(x / size) -1
    b_y = int(y / size) -1

    return (b_x, b_y)

def piece_to_img_name(piece):
    k_pieces = {
            "wKt": "wk",
            "bKt": "bk",
            "wKg": "wki",
            "bKg": "bki"
        }
    if piece == "___":
        return None
    if piece[:3] in k_pieces.keys():
        piece_name = k_pieces[piece[:3]]
    else:
        piece_name = piece[:2]
    return piece_name

class corpVis(QLabel):
    def __init__(self, vis, name, size, parent=None):
        super(corpVis, self).__init__()
        self.default_vis = QPixmap('./picture/' + vis).scaled(size, size, Qt.KeepAspectRatio, Qt.FastTransformation)
        self.set_img()
        self.piece_name = name

    def set_img(self):
        self.setPixmap(self.default_vis)
    #This function is snap the piece back to it place when the person releases wrong place
    #obsoleted

class PieceVis(QLabel):
    def __init__(self, visual, x_pos, y_pos, color:str='', parent=None):
        super(PieceVis, self).__init__(parent)

        if color not in ('white', 'black'):
            color = ''
        self.color = color
        self.piece_type = ""
        if "ki" in visual.lower():
            self.piece_type = 'King'
        else:
            pcs = {
                'p': 'Pawn',
                'r': 'Rook',
                'b': 'Bishop',
                'k': 'Knight',
                'q': 'Queen'
                }
            for pc_type in pcs:
                if pc_type == visual[1].lower():
                    self.piece_type = pcs[pc_type]
                    break


        # Set up some properties
        self.labelPos = QPoint()
        self.vis = visual
        self.onBoarder = False
        self._h_mode = False
        self.moves = []                    # is only accurate between picking up and placing a piece
        self.start = [x_pos ,y_pos ]
        self.end = [0, 0]       # pieces will ask chessgame if they can move
        self.default_vis = QPixmap('./picture/' + visual)
        self.set_img()

    def set_h_mode(self, val):
        self._h_mode = val

    def get_h_mode(self):
        return self._h_mode

    def set_img(self):
        self.setPixmap(self.default_vis)

    def not_same_team(self):
        is_white = self.color == 'white'
        whites_turn = (self.parent().controller.tracker.get_current_player()==1)
        return whites_turn != is_white

    def should_freeze(self):
        tile_not_active = not self.parent().tilePos[self.start[1]][self.start[0]].get_active()

        return game_over or ai_turn or (tile_not_active and self.not_same_team())

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        if self.should_freeze():
            return
        #If user clicks on a piece, it will be moved to the starting position
        #self.start =  screen_to_board(ev.windowPos().x(), ev.windowPos().y(), self.parent().tileSize)
        #print("start x: ", self.start[0], " y: ", self.start[1])
        self.moves = self.parent().controller.get_possible_moves_for_piece_at(x=self.start[0], y=self.start[1])
        self.raise_()

    # Set the region limits of the board that the piece can move to
    def mouseMoveEvent(self, ev: QMouseEvent) -> None:
        # doesn't use should_freeze to allow for attacks
        if game_over or ai_turn or self.not_same_team():
            return
        if ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).x() < (0 + (self.parent().tileSize / 2)) \
                and ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).y() < \
                (0 + (self.parent().tileSize / 2)):
            self.labelPos = QPoint(0 + (self.parent().tileSize / 2),
                                    0 + (self.parent().tileSize / 2))
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).y() < (0 + (self.parent().tileSize / 2)) \
                and ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).x() > \
                (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)):
            self.labelPos = QPoint(self.parent().tileSize * 9.25 - (self.parent().tileSize / 2),
                                    0 + (self.parent().tileSize / 2))
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).x() > \
                (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)) and \
                ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).y() > \
                (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)):
            self.labelPos = QPoint(self.parent().tileSize * 9.25 - (self.parent().tileSize / 2),
                                    self.parent().tileSize * 9.25 - (self.parent().tileSize / 2))
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).x() < (0 + (self.parent().tileSize / 2)) \
                and ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).y() > \
                (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)):
            self.labelPos = QPoint(0 + (self.parent().tileSize / 2),
                                    self.parent().tileSize * 9.25 - (self.parent().tileSize / 2))
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).x() < (0 + (self.parent().tileSize / 2)):
            self.labelPos = QPoint(0 + (self.parent().tileSize / 2),
                                    (ev.globalPos().y() - self.parent().pos().y()) - 30)
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).y() < (0 + (self.parent().tileSize / 2)):
            self.labelPos = QPoint((ev.globalPos().x() - self.parent().pos().x()) - 0,
                                    0 + (self.parent().tileSize / 2))
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).x() > \
                (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)):
            self.labelPos = QPoint(self.parent().tileSize * 9.25 - (self.parent().tileSize / 2),
                                    (ev.globalPos().y() - self.parent().pos().y()) - 30)
            self.onBoarder = True
        elif ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30)).y() > \
                (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)):
            self.labelPos = QPoint((ev.globalPos().x() - self.parent().pos().x()) - 0,
                                    (self.parent().tileSize * 9.25 - (self.parent().tileSize / 2)))
            self.onBoarder = True

        if not self.onBoarder:
            self.labelPos = ((ev.globalPos() - self.parent().pos()) - QPoint(0, 30))
        self.move(self.labelPos - QPoint(self.parent().tileSize / 2, (self.parent().tileSize / 2)))
        self.onBoarder = False


    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        drag_move = False
        click_end = False
        if self.should_freeze():
            return
        self.onBoarder = False
        print(self)
        self.end = screen_to_board(ev.windowPos().x(), ev.windowPos().y(), self.parent().tileSize)      # set new end pos
                   # set movement val on board object
        print(self.start, self.end)
        if self.same_loc(self.start, self.end):
            # we did not move, just clicked the piece, store it on the board object as start of click to move
            self.set_h_mode(not self._h_mode)   # highlighting logic
            if self.parent().moving_piece and self.parent().controller.is_enemy(self.end[0], self.end[1]):
                # this is the piece getting attacked
                click_end = True
            # board needs reference to this piece to make changes to it
            else:
                self.parent().moving_piece = self
                self.parent().setMoveStart(self.start)
            # we still might have moved the piece some amount so set it back to the center of its start tile
            move_spot = board_to_screen(self.start[0], self.start[1], self.parent().tileSize)
            self.move(move_spot[0], move_spot[1])
        else:
            drag_move = True
            self.set_h_mode(False)
        self.parent().remove_all_h()
        if self._h_mode:
            self.parent().add_group_h(self.moves)

        if drag_move:
            self.parent().setMoveStart(self.start)
            self.parent().move_end = self.end
            self.parent().do_piece_move(self, drag_move)

        if click_end:
            self.parent().move_end = self.end
            self.parent().do_piece_move(None)
        """ isAttack = (self.end[0], self.end[1], True) in self.moves
        moveSuccessful = self.parent().controller.move_piece(from_x=self.start[0], from_y=self.start[1],
                                                             to_x=self.end[0], to_y=self.end[1])        # or whatever the show dice roll function is
        self.parent().diceRollResult = self.parent().controller.get_result_of_dice_roll()
        self.parent().make_AI_move()
        if moveSuccessful:
            self.parent()._update_pieces()
            new_spot = board_to_screen(self.end[0], self.end[1],
                                       self.parent().tileSize)  # create pixel position of new piece
            self.start[0] = self.end[0]
            self.start[1] = self.end[1]
        else:
            new_spot = board_to_screen(self.start[0], self.start[1], self.parent().tileSize)
        self.move(new_spot[0], new_spot[1])

        if isAttack:
            self.parent().rollDiceScreen(moveSuccessful)
        self.parent().update_labels() """


        #self.parent().movePieceRelease(self.start, self.end)
    def same_loc(self, s_loc, f_loc):
        return (s_loc[0] == f_loc[0]) and (s_loc[1] == f_loc[1])

class TileVis(QLabel):
    def __init__(self, visual, move, attack, parent=None):
        super(TileVis, self).__init__(parent)
        # Set up some properties
        self.is_active = False
        self.move_highlight = QLabel(parent=self)
        self.move_highlight.setStyleSheet("background-color: rgba(255,255,0,150)")
        self.move_highlight.resize(squareSize, squareSize)
        self.atk_highlight = QLabel(parent=self)
        self.atk_highlight.setStyleSheet("background-color: rgba(255,69,0,150)")
        self.atk_highlight.resize(squareSize, squareSize)
        self.default_vis = QPixmap('./picture/' + visual)
        self.set_img(False)

    def set_default_vis(self, new_pixmap:QPixmap):
        self.default_vis = new_pixmap
        self.set_img(False)

    def set_active(self, val, atk=False):
        self.is_active = val
        self.set_img(atk)

    def set_img(self, atk):
        if self.is_active:
            self.atk_highlight.show() if atk else self.move_highlight.show()
        else:
            self.move_highlight.hide()
            self.atk_highlight.hide()
            self.setPixmap(self.default_vis)

    def get_active(self):
        return self.is_active

    def mousePressEvent(self, ev: QMouseEvent) -> None:
        self.start_click = screen_to_board(ev.windowPos().x(), ev.windowPos().y(), self.parent().tileSize)


    def mouseReleaseEvent(self, ev: QMouseEvent) -> None:
        self.end_click = screen_to_board(ev.windowPos().x(), ev.windowPos().y(), self.parent().tileSize)
        if self.same_loc(self.start_click, self.end_click):
            if self.parent().moving_piece:
                self.parent().move_end = self.end_click
                self.parent().do_piece_move(self.parent().moving_piece)

    def same_loc(self, s_loc, f_loc):
        return (s_loc[0] == f_loc[0]) and (s_loc[1] == f_loc[1])

class BoardVis(QMainWindow):
    def __init__(self):
        super(BoardVis,self).__init__()
        make_default(self)
        # make_larger(self)
        # make_smaller(self)
        self.controller = chess_game()
        self.__game_type = ""
        self.h_mode = True
        self.white_pov = True
        self.move_start = None
        self.move_end = None
        self.moving_piece = None
        #This block sets up the window properties
        #self.setGeometry(500, 200, 300, 300)
        self.setFixedSize(wSizew, wSizeh)
        self.setWindowIcon(QIcon('./picture/chessIcon.png'))
        self.setWindowTitle("AIFLChess")
        self.highlighted = []
        self.corp_menu = CorpMenu(self)

        self.tileSize = squareSize
        self.boardSize = self.tileSize * 9.5

        self.theme_menu = ThemeMenu(400,400, self)
        self.corner_tile = None
        self.theme_menu.move(150, 200)

        # buttons:
        #displays theme menu
        self.options = QPushButton('', self)
        self.options.setFixedSize(themeButtonWidth,themeButtonHeight)
        self.options.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        gear_image = QPixmap('./picture/settingsGear')
        gear_icon = QIcon(gear_image)
        self.options.setIcon(gear_icon)
        self.options.setIconSize(QSize(themeButtonWidth,themeButtonHeight))
        self.options.clicked.connect(self.theme_menu.show)

        # size selection menu
        self.sizeOptions = QPushButton('change size', self)
        self.sizeOptions.setFixedSize(sizeSelectWidth, sizeSelectHeight)
        self.sizeOptions.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
        change_img = QPixmap('/Users/kpgunasingh/NewSenior/AIPlayableFLChess/picture/another-change-4.png')
        change_icon = QIcon(change_img)
        self.sizeOptions.setIconSize(QSize(sizeSelectWidth, sizeSelectHeight))
        self.sizeOptions.show()
        # self.sizeOptions.clicked.connect(self.sizeOptions.show())

        # This button allow you can stop your turn
        self.endTurnButton = QPushButton("End Turn", self)

        # This button allow you can reset the game when you want to start new game
        self.restartButton = QPushButton("Restart", self)

        # choose highlight mode on/off
        self.corpButton = QPushButton("Manage Corps", self)

        # This button can display the rules
        self.helperButton = QPushButton("i", self)
        self.show_the_rules = displayRules()

        self.tableOption = QLabel(self)

        #Show remaining moves
        self.moveIndicator = QLabel(self)
        # Holds labels for the tiles on the board.
        self.tilePos = [["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"]]

        # Holds labels for the pieces on the board.
        self.piecePos = [["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"],
                        ["0", "0", "0", "0", "0", "0", "0", "0"]]

        self.border = []

        self.welcomeText = QLabel(self)
        self.startScreen = QLabel(self)
        self.optionScreen = QLabel(self)
        self.whiteTeamText = QLabel(self)
        self.blackTeamText = QLabel(self)
        self.highlightText = QLabel(self)
        self.gameTypeText = QLabel(self)

        #set up the buttons
        self.startGameButton= QPushButton("Start game",self)
        self.smallSelectButton = QPushButton("Small", self)
        self.largeSelectButton = QPushButton("Large", self)
        self.revertDefault = QPushButton("Default", self)

        self.whiteHumanButton = QRadioButton("Human", self)
        self.whiteAIButton = QRadioButton("Computer", self)
        self.blackHumanButton = QRadioButton("Human", self)
        self.blackAIButton = QRadioButton("Computer", self)

        self.offhighlight = QRadioButton("Off", self)
        self.onhighlight = QRadioButton("On", self)
        self.medievalButton = QRadioButton("Medieval", self)
        self.corpCommanderButton = QRadioButton("Corp Command", self)

        # Set up the roll dice screen
        self.pauseBackground = QLabel(self)
        self.rollText = QLabel(self)
        self.rollDiceAnimation = QLabel(self)
        self.resultCaptureText = QLabel(self)
        self.aiPieceInfoText = QLabel(self)
        self.okayButton = QPushButton("Return to Board", self)
        self.attackSuccess = None
        self.diceRollResult = -1

        self.sbs_delay_ms = 400

        self.ai_player = None
        self.ai_v_ai_players = []

        self.ai_attack_info = None

        self.ai_move_delay = QTimer(self)
        self.ai_move_delay_ms = 1000
        self.ai_move_delay.timeout.connect(self.ai_single_move)

        self.theme = None

        self.showBoard()

    def set_theme(self, theme:str = 'default'):
        themes = {
            'default': {
                'splash': './picture/defaultChessSplash.png',
                'color': 'rgb(0, 204, 204)',
                'board': ('wt', 'bt', 'bt') #light_tile, dark_tile, border_tile
                },
            'wood': {
                'splash': './picture/woodChessSplash.png',
                'color': 'rgb(227, 217, 197)',
                'board': ('lwt', 'dwt', 'lwt')
                },
            'marble': {
                'splash': './picture/marbleChessSplash.png',
                'color': 'white',
                'board': ('wmt', 'gmt', 'wmt')
                },
        }

        if theme not in themes:
            print("didnt find theme")
            theme = "default"

        self.theme = themes[theme]
        splash_img = self.theme["splash"]
        color = self.theme["color"]

        self.startScreen.setStyleSheet(f'background-image: url({splash_img});')
        self.pauseBackground.setStyleSheet(f'background-image: url({splash_img});')

        button_css = f'''
            QPushButton {{
                background-color: {color};
                color: black;
                border: 0.1em solid #000000;
            }}
            QPushButton:hover {{
                background-color: black;
                color: {color};
                border-color: {color};
            }}
            '''

        text_css = f'font-weight: bold; color: {color}'
        alt_text_css = 'font-weight: bold; color: rgb(10, 110, 80)'

        # start screen
        self.welcomeText.setStyleSheet(alt_text_css if theme=='marble' else text_css)

        self.whiteTeamText.setStyleSheet(text_css)
        self.gameTypeText.setStyleSheet(text_css)
        self.blackTeamText.setStyleSheet(text_css)
        self.highlightText.setStyleSheet(text_css)

        self.startGameButton.setStyleSheet(button_css)
        self.smallSelectButton.setStyleSheet(button_css)
        self.largeSelectButton.setStyleSheet(button_css)
        self.revertDefault.setStyleSheet(button_css)
        # roll dice screen
        self.rollText.setStyleSheet(alt_text_css if theme=='marble' else text_css)
        self.resultCaptureText.setStyleSheet(alt_text_css if theme=='marble' else text_css)
        self.aiPieceInfoText.setStyleSheet(text_css+';background-color: rgba(0, 0, 0, 0.8)')

        self.okayButton.setStyleSheet(button_css)

        self.helperButton.setStyleSheet(f'''
            QPushButton {{
                font-family: "Times New Roman";
                font-size: 25px;
                background-color: {color};
                color: black;
                border: 0.1em solid #000000;
                border-radius: 25px;
            }}
            QPushButton:hover {{
                background-color: black;
                color: {color};
                border-color: {color};
            }}
            ''')

        # board
        self.set_non_playables()

    def update_chosen_theme(self):
        theme = self.theme_menu.get_theme()
        self.set_theme(theme)

    def do_piece_move(self, mvd_piece: PieceVis, dragged:bool=False):
        print("was called")
        piece = mvd_piece
        if not piece:
            piece = self.moving_piece
        piece.set_h_mode(False)
        self.remove_all_h()
        isAttack = (self.move_end[0], self.move_end[1], True) in piece.moves
        moveSuccessful = self.controller.move_piece(from_x=self.move_start[0], from_y=self.move_start[1],
                                                    to_x=self.move_end[0], to_y=self.move_end[1])
        self.diceRollResult = self.controller.get_result_of_dice_roll()
        new_spots = []
        if moveSuccessful:
            for x, y in self.controller.get_move_path():
                new_spot = board_to_screen(x, y, self.tileSize)  # create pixel position of new piece
                new_spots.append(new_spot)
            if len(new_spots) == 0:
                new_spot = board_to_screen(self.move_start[0], self.move_start[1], self.tileSize)
            piece.start[0] = self.move_end[0]
            piece.start[1] = self.move_end[1]
        else:
            new_spot = board_to_screen(self.move_start[0], self.move_start[1], self.tileSize)
        print("moved piece: ", piece)
        # piece.move(new_spot[0], new_spot[1])
        if len(new_spots)>1 and not dragged:
            new_spots.reverse()

            sbs_delay = QTimer(self)

            def spot_by_spot():
                if len(new_spots)==0:
                    sbs_delay.stop()
                    return
                x, y = new_spots.pop()
                print(x,y)
                piece.move(x, y)

            sbs_delay.timeout.connect(spot_by_spot)
            sbs_delay.start(self.sbs_delay_ms)
        else:
            piece.move(new_spot[0], new_spot[1])

        if isAttack:
            self._update_pieces()
            self.rollDiceScreen(moveSuccessful)
        else:
            self.make_AI_move() #TODO: find place for this after update pieces is fixed

        self.update_labels()

        self.reset_movement_data()

    def reset_movement_data(self):
        self.moving_piece = None
        self.move_start = None
        self.move_end = None

    def closeEvent(self,event):
        self.show_the_rules.close()
        self.corp_menu.close()
        self.theme_menu.close()
        event.accept()

    def set_h_mode(self, val: Boolean):
        self.h_mode = val

    def add_to_h(self, tile: TileVis):
        if not self.h_mode:
            return
        if tile not in self.highlighted:
            tile.set_active(True)
            self.highlighted.append(tile)

    def add_group_h(self, squares: Tuple):
        if not self.h_mode:
            return
        for pos in squares:
            tile = self.tilePos[pos[1]][pos[0]]
            tile.set_active(True, pos[2])
            self.highlighted.append(tile)

    def remove_all_h(self):
        if not self.highlighted:
            return
        for row in self.tilePos:
            for tile in row:
                if type(tile) is TileVis:
                    tile.set_active(False, False)
        for tile in self.highlighted:
            self.list_remove(tile)

    def list_remove(self, tile:TileVis):
        tile.set_active(False, False)
        self.highlighted.remove(tile)

    def setMoveStart(self, position):
        self.move_start = position

    def showBoard(self):
        # Initialize the board.
        self.setBoard()
        self.showStartScreen()
        self.resize(self.boardSize + self.tableOption.width(), self.boardSize )

    def setBoard(self):
        self.boardSize = self.tileSize * 9.5

        #get data from controller and display it

    #Create table option properties
        self.tableOption.setText("Current Turn: White")
        self.tableOption.setAlignment(Qt.AlignCenter)
        self.tableOption.resize(lSizew, lSizeh)
        font = QFont()
        font.setFamily("Impact")
        font.setPixelSize(self.tableOption.height() * 0.8)
        self.tableOption.setFont(font)
        self.tableOption.move(int(self.boardSize) - tableOptionOffsetX,
                              int(self.boardSize /2 -tableOptionOffsetY1) - (self.tableOption.height()) * 0.5 +tableOptionOffsetY2)
        self.tableOption.hide()

    #Create show information of move indicator
        self.moveIndicator.setText("Remaining Move:")
        self.moveIndicator.setAlignment(Qt.AlignCenter)
        self.moveIndicator.resize(lSizew, lSizeh)
        font = QFont()
        font.setFamily("impact")
        font.setPixelSize(self.moveIndicator.height() * 0.8)
        self.moveIndicator.setFont(font)
        self.moveIndicator.move(int(self.boardSize) - tableOptionOffsetX,
                                int(self.boardSize /2)- (self.moveIndicator.height()) * 0.5 - tableOptionOffsetY2)
        self.moveIndicator.hide()

    #manage corp button setup:
        self.__set_button(self.corpButton, reStartbuttonfsize)
        self.corpButton.setCheckable(True)
        self.corpButton.clicked.connect(self.corpBClicked)
        self.corpButton.resize(bSizew,bSizeh)
        self.corpButton.move(int(self.boardSize - ((self.restartButton.width() - self.tableOption.width()) / 2)) - corpButtonOffsetX,
                             corpButtonOffsetY)

        self.wCapturedText = QLabel(self)
        self.wCapturedFrame = QFrame(self)

        self.bCapturedText = QLabel(self)
        self.bCapturedFrame = QFrame(self)

        # Create white pieces captured
        self.wCapturedText.setText("CAPTURED BY WHITE")
        self.wCapturedText.setAlignment(Qt.AlignCenter)
        self.wCapturedText.resize(lSizew, lSizeh)
        font = QFont()
        font.setBold(True)
        font.setFamily("Baskerville")
        font.setPixelSize(self.moveIndicator.height() * 0.6)
        self.wCapturedText.setFont(font)
        self.wCapturedText.move(int(self.boardSize - ((self.restartButton.width() - self.tableOption.width()) / 2)) - capWhiteOffsetX,
                             capWhiteOffsetY)

        #set frame for wCapturedPic:
        self.wCapturedFrame.setFrameShape(QFrame.Box)
        self.wCapturedFrame.setLineWidth(2)
        self.wCapturedFrame.setGeometry(int(self.boardSize) - whiteBoxOffsetX,
                                      whiteBoxOffsetY,
                                      whiteBoxW, whiteBoxH)
        self.wCapLayout = QVBoxLayout()
        self.wCapLayout.addWidget(QWidget())
        self.wCapturedFrame.setLayout(self.wCapLayout)

        # Create black pieces captured
        self.bCapturedText.setText("CAPTURED BY BLACK")
        self.bCapturedText.setAlignment(Qt.AlignCenter)
        self.bCapturedText.resize(lSizew, lSizeh)
        font = QFont()
        font.setBold(True)
        font.setFamily("Baskerville")
        font.setPixelSize(self.moveIndicator.height() * 0.6)
        self.bCapturedText.setFont(font)
        self.bCapturedText.move(
            int(self.boardSize - ((self.restartButton.width() - self.tableOption.width()) / 2)) - capBlackOffsetX,
            capBlackOffsetY)

        # set frame for bCapturedPic:
        self.bCapturedFrame.setFrameShape(QFrame.Box)
        self.bCapturedFrame.setLineWidth(2)
        self.bCapturedFrame.setGeometry(int(self.boardSize) - whiteBoxOffsetX,
                                        blackBoxOffsetY,
                                        whiteBoxW, whiteBoxH)
        self.bCapLayout = QVBoxLayout()
        self.bCapLayout.addWidget(QWidget())
        self.bCapturedFrame.setLayout(self.bCapLayout)

        if self.__game_type != "Corp":
            self.corpButton.hide()

    #Create stop button properties
        self.__set_button(self.endTurnButton, reStartbuttonfsize)
        self.endTurnButton.clicked.connect(self.endTurnClicked)
        self.endTurnButton.move(int(self.boardSize - ((self.endTurnButton.width() - self.tableOption.width()) / 2))-endButtonOffsetX,
                              int(self.boardSize / 2 + endButtonOffsetY1) - (self.endTurnButton.height() * 0.5)-endButtonOffsetY2)

        self.endTurnButton.resize(bSizew,bSizeh)
        self.endTurnButton.hide()

    #Create restart button properties
        self.__set_button(self.restartButton, reStartbuttonfsize)
        self.restartButton.move(int(self.boardSize - ((self.restartButton.width() - self.tableOption.width()) / 2))-endButtonOffsetX,
                             int(self.boardSize / 2 + restartButtonOffsetY) - (self.restartButton.height() * 0.5)-endButtonOffsetY2)

        self.restartButton.resize(bSizew,bSizeh)
        self.restartButton.clicked.connect(self.returnToStartScreen)
        self.restartButton.hide()

        # create properties for the helper button
        self.helperButton.clicked.connect(lambda: self.show_the_rules.show())
        self.helperButton.move(self.tileSize/6, self.tileSize/6)
        self.helperButton.resize(self.tileSize*2/3, self.tileSize*2/3)
        self.helperButton.show()
        self.helperButton.raise_()

        # Create StartScreen properties
        self.startScreen.setAlignment(Qt.AlignCenter)
        self.startScreen.resize(self.width(), self.height())
        self.startScreen.setStyleSheet("background-image: url(./picture/defaultChessSplash.png);")
        self.startScreen.move(0, 0)

        moveIntoSidePanel = ((self.width()-self.boardSize)/2)

        # Set up choose side text properties
        self.welcomeText.setAlignment(Qt.AlignCenter)
        self.welcomeText.setText("Welcome to Fuzzy Logic Chess!"
                                    "\nGame Setup:")
        self.welcomeText.resize(welcomeTextW, welcomeTextH)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.welcomeText.height() * 0.4)
        self.welcomeText.setFont(font)
        self.welcomeText.move(int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + moveIntoSidePanel,
                                 int((self.boardSize / 2) - welcomeTextOffsetY))
        self.welcomeText.hide()

        self.options.move(self.tileSize/6, self.tileSize/6)

        # Create start screen properties
        self.pauseBackground.setAlignment(Qt.AlignCenter)
        self.pauseBackground.resize(self.width(), self.height())
        self.pauseBackground.setStyleSheet('background-color: black')
        self.pauseBackground.setStyleSheet("background-image: url(./picture/defaultChessSplash.png);")
        self.pauseBackground.move(0, 0)
        self.pauseBackground.hide()

        # Set up for okay button properties
        self.okayButton.clicked.connect(self.okayButtonClicked)
        self.okayButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.okayButton.height() * 0.4)
        self.okayButton.setFont(font)
        self.okayButton.move(int((self.boardSize / 2) - (self.okayButton.width() / 2)) + moveIntoSidePanel
                             , int((self.boardSize / 2) + okayButtonOffsetY))
        self.okayButton.hide()

        #set up the option screen properties
        self.optionScreen.setAlignment(Qt.AlignCenter)
        self.optionScreen.resize(self.boardSize / 1.5, self.boardSize / 2)
        self.optionScreen.setStyleSheet('background-color: rgba(0, 0, 0, .8)')
        self.optionScreen.move(int((self.boardSize / 2) - (self.onhighlight.width() / 2)) - optionScreenOffsetX + moveIntoSidePanel
                               , int((self.boardSize / 2) - optionScreenOffsetY))
        self.optionScreen.hide()

        # Set up for start game button properties
        self.startGameButton.clicked.connect(self.startGameClicked)
        self.startGameButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.startGameButton.height() * 0.4)
        self.startGameButton.setFont(font)
        self.startGameButton.move(int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel
                            , int((self.boardSize / 2) + startButtonOffsetY))
        self.startGameButton.hide()

        # set up for small size selector

        # set up for small size selector
        self.smallSelectButton.clicked.connect(self.smallSelectButtonClicked)
        self.smallSelectButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.smallSelectButton.height() * 0.4)
        self.smallSelectButton.setFont(font)
        self.smallSelectButton.move(
            int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel - 345
            , int((self.boardSize / 2) + startButtonOffsetY - 97))
        self.smallSelectButton.hide()

        # set up for large size selector
        self.largeSelectButton.clicked.connect(self.largeSelectButtonClicked)
        self.largeSelectButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.largeSelectButton.height() * 0.4)
        self.largeSelectButton.setFont(font)
        self.largeSelectButton.move(
            int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel - 345
            , int((self.boardSize / 2) + startButtonOffsetY + 7))
        self.largeSelectButton.hide()

        # set up for selecting revert to default
        self.revertDefault.clicked.connect(self.revertToDefaultClicked)
        self.revertDefault.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.revertDefault.height() * 0.4)
        self.revertDefault.setFont(font)
        self.revertDefault.move(
            int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel - 345
            , int((self.boardSize / 2) + startButtonOffsetY - 45))
        self.revertDefault.hide()

        #set up team text properties
        self.whiteTeamText.setAlignment(Qt.AlignCenter)
        self.whiteTeamText.setText("White Player:")
        self.whiteTeamText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.whiteTeamText.setFont(font)
        self.whiteTeamText.move(int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel,
                                  int((self.boardSize / 2) - whiteTeamTextOffsetY))
        self.whiteTeamText.hide()

        #set up opponent text properties
        self.blackTeamText.setAlignment(Qt.AlignCenter)
        self.blackTeamText.setText("Black Player: ")
        self.blackTeamText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.blackTeamText.setFont(font)
        self.blackTeamText.move(int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel,
                               int((self.boardSize / 2) - blackTeamTextOffsetY))
        self.blackTeamText.hide()



        #set up highlight text properties
        self.highlightText.setAlignment(Qt.AlignCenter)
        self.highlightText.setText("Highlight: ")
        self.highlightText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.highlightText.setFont(font)
        self.highlightText.move(int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel,
                                int((self.boardSize / 2) - highlightTextOffsetY))
        self.highlightText.hide()

        #set up game type text properties
        self.gameTypeText.setAlignment(Qt.AlignCenter)
        self.gameTypeText.setText("Game Type: ")
        self.gameTypeText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.gameTypeText.setFont(font)
        self.gameTypeText.move(int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel,
                               int((self.boardSize / 2) + gameTypeTextOffsetY))
        self.gameTypeText.hide()

        #radioButtonTextCSS = 'color: white; font-size: 15px'

        #set up white/black button properties
        self.whitegroup = QButtonGroup()

        self.whitegroup.addButton(self.whiteHumanButton)
        self.__set_button(self.whiteHumanButton, whiteButtonH)
        self.whiteHumanButton.move(int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                              , int((self.boardSize / 2) - whiteButtonOffsetY))

         # Set up for black button properties
        self.whitegroup.addButton(self.whiteAIButton)
        self.__set_button(self.whiteAIButton, whiteButtonH)
        self.whiteAIButton.move(int((self.boardSize / 2) - (self.whiteAIButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                              , int((self.boardSize / 2) - whiteButtonAIOffsetY))

        self.whiteHumanButton.setChecked(True)

        self.whiteHumanButton.setStyleSheet(radioButtonTextCSS)
        self.whiteAIButton.setStyleSheet(radioButtonTextCSS)
        self.whiteHumanButton.adjustSize()
        self.whiteAIButton.adjustSize()

        #set up human/computer button properties
        self.blackgroup = QButtonGroup(self)

        self.blackgroup.addButton(self.blackHumanButton, 1)
        self.__set_button(self.blackHumanButton, whiteButtonH)
        self.blackHumanButton.move(int((self.boardSize / 2) - (self.blackHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                              , int((self.boardSize / 2) - blackButtonOffsetY))

        self.blackgroup.addButton(self.blackAIButton, 2)
        self.__set_button(self.blackAIButton, whiteButtonH)
        self.blackAIButton.move(int((self.boardSize / 2) - (self.blackAIButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                                 , int((self.boardSize / 2) - blackButtonAIOffsetY))

        self.blackHumanButton.setChecked(True)

        self.blackHumanButton.setStyleSheet(radioButtonTextCSS)
        self.blackAIButton.setStyleSheet(radioButtonTextCSS)
        self.blackHumanButton.adjustSize()
        self.blackAIButton.adjustSize()

        #set up highlight on/off button properties
        self.highlight_group = QButtonGroup(self)

        self.highlight_group.addButton(self.onhighlight, 1)
        self.__set_button(self.onhighlight, whiteButtonH)
        self.onhighlight.move(int((self.boardSize / 2) - (self.onhighlight.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                              , int((self.boardSize / 2) + highlightButtonOffsetY))

        self.highlight_group.addButton(self.offhighlight, 2)
        self.__set_button(self.offhighlight, whiteButtonH)
        self.offhighlight.move(int((self.boardSize / 2) - (self.offhighlight.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                               , int((self.boardSize / 2) + highlightOffButtonOffsetY))
        self.onhighlight.setChecked(True)

        self.onhighlight.setStyleSheet(radioButtonTextCSS)
        self.offhighlight.setStyleSheet(radioButtonTextCSS)
        self.onhighlight.adjustSize()
        self.offhighlight.adjustSize()

        #set up medieval/corp button properties
        self.gameType_group = QButtonGroup(self)

        self.gameType_group.addButton(self.medievalButton, 1)
        self.__set_button(self.medievalButton, whiteButtonH)
        self.medievalButton.move(int((self.boardSize / 2) - (self.medievalButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                                 , int((self.boardSize / 2) + gameTypeButtonOffsetY))

        self.gameType_group.addButton(self.corpCommanderButton, 2)
        self.__set_button(self.corpCommanderButton, whiteButtonH)
        self.corpCommanderButton.move(int((self.boardSize / 2) - (self.corpCommanderButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
                                      , int((self.boardSize / 2) + gameTypeCorpButtonOffsetY))
        self.corpCommanderButton.setChecked(True)

        self.medievalButton.setStyleSheet(radioButtonTextCSS)
        self.corpCommanderButton.setStyleSheet(radioButtonTextCSS)
        self.medievalButton.adjustSize()
        self.corpCommanderButton.adjustSize()

        self.set_theme()

        self.captured_by = {
            "white": [],
            "black": []
        }

        # set up the win congratulation screen properties
        self.winCon = QLabel(self)
        self.winCon.setAlignment(Qt.AlignCenter)
        self.winCon.resize(wSizew, wSizeh)
        self.winCon.setStyleSheet('background-color: rgba(0, 0, 0, .8)')
        self.winCon.move(0, 0)
        self.winCon.hide()

    # Reset Board Size
    def resetBoardSize(self):
        print("Reset Board Size")

        self.setFixedSize(wSizew, wSizeh)
        self.tileSize = squareSize
        self.boardSize = self.tileSize * 9.5

        self.tableOption.resize(lSizew, lSizeh)
        font = QFont()
        font.setFamily("Impact")
        font.setPixelSize(self.tableOption.height() * 0.8)
        self.tableOption.setFont(font)
        self.tableOption.move(int(self.boardSize) - tableOptionOffsetX,
                              int(self.boardSize / 2 - tableOptionOffsetY1) - (
                                  self.tableOption.height()) * 0.5 + tableOptionOffsetY2)
        self.tableOption.hide()

        # Create show information of move indicator

        self.moveIndicator.resize(lSizew, lSizeh)
        font = QFont()
        font.setFamily("impact")
        font.setPixelSize(self.moveIndicator.height() * 0.8)
        self.moveIndicator.setFont(font)
        self.moveIndicator.move(int(self.boardSize) - tableOptionOffsetX,
                                int(self.boardSize / 2) - (self.moveIndicator.height()) * 0.5 - tableOptionOffsetY2)
        self.moveIndicator.hide()

        # Create restart button properties
        self.restartButton.resize(bSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(bSizeh * 0.4)
        self.restartButton.setFont(font)

        #self.restartButton.move(
        #    int(self.boardSize - ((bSizew - lSizew) / 2)) - endButtonOffsetX,
        #    int(self.boardSize / 2 + restartButtonOffsetY) - (bSizeh * 0.5) - endButtonOffsetY2)
        self.restartButton.move(
                int(self.boardSize - ((bSizew - lSizew) / 2)) - 20,
                int(self.boardSize / 2 + restartButtonOffsetY) - (bSizeh * 0.5) - endButtonOffsetY2)

        self.restartButton.hide()
        # manage corp button setup:
        self.corpButton.resize(bSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(bSizeh * 0.4)
        self.corpButton.setFont(font)
        self.corpButton.move(
           # int(self.boardSize - ((bSizew - self.tableOption.width()) / 2)) - corpButtonOffsetX,
            int(self.boardSize - ((bSizew - lSizew) / 2)) - 20,
            corpButtonOffsetY)

        # Create white pieces captured
        self.wCapturedText.setAlignment(Qt.AlignCenter)
        self.wCapturedText.resize(lSizew, lSizeh)
        font = QFont()
        font.setBold(True)
        font.setFamily("Baskerville")
        font.setPixelSize(self.moveIndicator.height() * 0.6)
        self.wCapturedText.setFont(font)
        self.wCapturedText.move(
            int(self.boardSize - ((bSizew - lSizew) / 2)) - 20,
            capWhiteOffsetY)

        # set frame for wCapturedPic:

        self.wCapturedFrame.setGeometry(int(self.boardSize) - whiteBoxOffsetX,
                                        whiteBoxOffsetY,
                                        whiteBoxW, whiteBoxH)

        # Create black pieces captured
        self.bCapturedText.setAlignment(Qt.AlignCenter)
        self.bCapturedText.resize(lSizew, lSizeh)
        font = QFont()
        font.setBold(True)
        font.setFamily("Baskerville")
        font.setPixelSize(self.moveIndicator.height() * 0.6)
        self.bCapturedText.setFont(font)
        self.bCapturedText.move(
            int(self.boardSize - ((bSizew - lSizew) / 2)) - 20,
            capBlackOffsetY)

        # set frame for bCapturedPic:
        # self.bCapturedFrame.setFrameShape(QFrame.Box)
        # self.bCapturedFrame.setLineWidth(2)
        self.bCapturedFrame.setGeometry(int(self.boardSize) - whiteBoxOffsetX,
                                        blackBoxOffsetY,
                                        whiteBoxW, whiteBoxH)
        # self.bCapLayout = QVBoxLayout()
        # self.bCapLayout.addWidget(QWidget())
        # self.bCapturedFrame.setLayout(self.bCapLayout)

        # Create stop button properties


        self.endTurnButton.resize(bSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(bSizeh * 0.4)
        self.endTurnButton.setFont(font)
        self.endTurnButton.move(
            int(self.boardSize - ((bSizew - lSizew) / 2)) - 20,
            int(self.boardSize / 2 + endButtonOffsetY1) - (self.endTurnButton.height() * 0.5) - endButtonOffsetY2)

        self.endTurnButton.hide()



        # create properties for the helper button

        self.helperButton.move(self.tileSize / 6, self.tileSize / 6)
        self.helperButton.resize(self.tileSize * 2 / 3, self.tileSize * 2 / 3)
        self.helperButton.show()
        self.helperButton.raise_()

        # Create StartScreen properties
        self.startScreen.setAlignment(Qt.AlignCenter)
        self.startScreen.resize(self.width(), self.height())
        self.startScreen.setStyleSheet("background-image: url(./picture/defaultChessSplash.png);")
        self.startScreen.move(0, 0)

        moveIntoSidePanel = ((self.width() - self.boardSize) / 2)

        # Set up choose side text properties
        self.welcomeText.setAlignment(Qt.AlignCenter)

        self.welcomeText.resize(welcomeTextW, welcomeTextH)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.welcomeText.height() * 0.4)
        self.welcomeText.setFont(font)
        self.welcomeText.move(int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + moveIntoSidePanel,
                              int((self.boardSize / 2) - welcomeTextOffsetY))
        self.welcomeText.hide()

        self.options.move(self.tileSize / 6, self.tileSize / 6)

        # Create start screen properties
        self.pauseBackground.setAlignment(Qt.AlignCenter)
        self.pauseBackground.resize(self.width(), self.height())
        self.pauseBackground.setStyleSheet('background-color: black')
        self.pauseBackground.setStyleSheet("background-image: url(./picture/defaultChessSplash.png);")
        self.pauseBackground.move(0, 0)
        self.pauseBackground.hide()

        # Set up for okay button properties

        self.okayButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.okayButton.height() * 0.4)
        self.okayButton.setFont(font)
        self.okayButton.move(int((self.boardSize / 2) - (self.okayButton.width() / 2)) + moveIntoSidePanel
                             , int((self.boardSize / 2) + okayButtonOffsetY))
        self.okayButton.hide()

        # set up the option screen properties
        self.optionScreen.setAlignment(Qt.AlignCenter)
        self.optionScreen.resize(self.boardSize / 1.5, self.boardSize / 2)
        self.optionScreen.setStyleSheet('background-color: rgba(0, 0, 0, .8)')
        self.optionScreen.move(
            int((self.boardSize / 2) - (self.onhighlight.width() / 2)) - optionScreenOffsetX + moveIntoSidePanel
            , int((self.boardSize / 2) - optionScreenOffsetY))
        self.optionScreen.hide()

        # Set up for start game button properties

        self.startGameButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.startGameButton.height() * 0.4)
        self.startGameButton.setFont(font)
        self.startGameButton.move(int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel
                                  , int((self.boardSize / 2) + startButtonOffsetY))
        self.startGameButton.hide()

        # set up for small size selector

        # set up for small size selector

        self.smallSelectButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.smallSelectButton.height() * 0.4)
        self.smallSelectButton.setFont(font)
        self.smallSelectButton.move(
            int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel - 280
            , int((self.boardSize / 2) + startButtonOffsetY - 97))
        self.smallSelectButton.hide()

        # set up for large size selector

        self.largeSelectButton.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.largeSelectButton.height() * 0.4)
        self.largeSelectButton.setFont(font)
        self.largeSelectButton.move(
            int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel - 280
            , int((self.boardSize / 2) + startButtonOffsetY + 7))
        self.largeSelectButton.hide()

        # set up for selecting revert to default

        self.revertDefault.resize(sbSizew, bSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.revertDefault.height() * 0.4)
        self.revertDefault.setFont(font)
        self.revertDefault.move(
            int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + moveIntoSidePanel - 280
            , int((self.boardSize / 2) + startButtonOffsetY - 45))
        self.revertDefault.hide()

        # set up team text properties
        self.whiteTeamText.setAlignment(Qt.AlignCenter)
        self.whiteTeamText.setText("White Player:")
        self.whiteTeamText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.whiteTeamText.setFont(font)
        self.whiteTeamText.move(
            int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel + 20,
            int((self.boardSize / 2) - whiteTeamTextOffsetY))
        self.whiteTeamText.hide()

        # set up opponent text properties
        self.blackTeamText.setAlignment(Qt.AlignCenter)
        self.blackTeamText.setText("Black Player: ")
        self.blackTeamText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.blackTeamText.setFont(font)
        self.blackTeamText.move(
            int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel + 20,
            int((self.boardSize / 2) - blackTeamTextOffsetY))
        self.blackTeamText.hide()

        # set up highlight text properties
        self.highlightText.setAlignment(Qt.AlignCenter)
        self.highlightText.setText("Highlight: ")
        self.highlightText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.highlightText.setFont(font)
        self.highlightText.move(
            int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel + 10,
            int((self.boardSize / 2) - highlightTextOffsetY))
        self.highlightText.hide()

        # set up game type text properties
        self.gameTypeText.setAlignment(Qt.AlignCenter)
        self.gameTypeText.setText("Game Type: ")
        self.gameTypeText.resize(lSizew, blSizeh)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.whiteTeamText.height() * 0.2)
        self.gameTypeText.setFont(font)
        self.gameTypeText.move(
            int((self.boardSize / 2) - (self.welcomeText.width() / 2)) + whiteTeamTextOffsetX + moveIntoSidePanel + 10,
            int((self.boardSize / 2) + gameTypeTextOffsetY))
        self.gameTypeText.hide()

        # radioButtonTextCSS = 'color: white; font-size: 15px'

        # set up white/black button properties
        self.whiteHumanButton.setStyleSheet(radioButtonTextCSS)
        self.whiteAIButton.setStyleSheet(radioButtonTextCSS)
        self.whiteHumanButton.adjustSize()
        self.whiteAIButton.adjustSize()
        self.whiteHumanButton.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) - whiteButtonOffsetY))

        # Set up for black button properties
        self.whiteAIButton.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) - whiteButtonAIOffsetY))

        # set up human/computer button properties
        self.blackHumanButton.setStyleSheet(radioButtonTextCSS)
        self.blackAIButton.setStyleSheet(radioButtonTextCSS)
        self.blackHumanButton.adjustSize()
        self.blackAIButton.adjustSize()
        self.blackHumanButton.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) - blackButtonOffsetY))

        #self.__set_button(self.blackAIButton, whiteButtonH)
        self.blackAIButton.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) - blackButtonAIOffsetY))



        # set up highlight on/off button properties
        self.onhighlight.setStyleSheet(radioButtonTextCSS)
        self.offhighlight.setStyleSheet(radioButtonTextCSS)
        self.onhighlight.adjustSize()
        self.offhighlight.adjustSize()

        self.onhighlight.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) + highlightButtonOffsetY))

        self.offhighlight.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) + highlightOffButtonOffsetY))
        self.onhighlight.setChecked(True)


        # set up medieval/corp button properties
        self.medievalButton.setStyleSheet(radioButtonTextCSS)
        self.corpCommanderButton.setStyleSheet(radioButtonTextCSS)
        self.medievalButton.adjustSize()
        self.corpCommanderButton.adjustSize()

        self.medievalButton.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) + gameTypeButtonOffsetY))

        self.corpCommanderButton.move(
            int((self.boardSize / 2) - (self.whiteHumanButton.width() / 2)) + moveIntoSidePanel + whiteButtonOffsetX
            , int((self.boardSize / 2) + gameTypeCorpButtonOffsetY))
        self.corpCommanderButton.setChecked(True)

        #self.set_theme()

        self.captured_by = {
            "white": [],
            "black": []
        }

        # set up the win congratulation screen properties
        self.show_the_rules.resize(helpScreenWidth,helpScreenHeight)

        self.winCon.setAlignment(Qt.AlignCenter)
        self.winCon.resize(wSizew, wSizeh)
        self.winCon.setStyleSheet('background-color: rgba(0, 0, 0, .8)')
        self.winCon.move(0, 0)
        self.winCon.hide()

    def congratulations(self):
        # set up the win congratulation screen properties
        self.winCon = QLabel(self)
        self.winCon.setAlignment(Qt.AlignCenter)
        self.winCon.resize(wSizew, wSizeh)
        self.winCon.setStyleSheet('background-color: rgba(0, 0, 0, .8)')
        self.winCon.move(0, 0)
        self.winCon.show()

        self.conpic = QLabel(self)
        pic = QMovie('./picture/cr1.gif')
        self.conpic.setMovie(pic)
        self.conpic.resize(300, 300)
        self.conpic.move(0, 200)
        pic.start()
        self.conpic.show()

        self.conpic1 = QLabel(self)
        pic1 = QMovie('./picture/cr2.gif')
        self.conpic1.setMovie(pic1)
        self.conpic1.resize(500, 300)
        self.conpic1.move(300, 50)
        pic1.start()
        self.conpic1.show()

        self.conpic2 = QLabel(self)
        pic2 = QMovie('./picture/cr3.gif')
        self.conpic2.setMovie(pic2)
        self.conpic2.resize(300, 300)
        self.conpic2.move(600, 300)
        pic2.start()
        self.conpic2.show()

        # set up the win congratulation screen text properties
        self.winConText = QLabel(self)
        self.winConText.setAlignment(Qt.AlignCenter)
        self.winConText.setText("Congratulations! "
                                "\nWinner: " +
                                    ("White" if self.controller.tracker.get_current_player() else "Black") +
                                    " Team!")
        self.winConText.setStyleSheet('color: red; font-weight: bold')
        self.winConText.setFont(QFont('Arial', 30))
        self.winConText.resize(wSizew, wSizeh)
        self.winConText.move(0, -100)
        self.winConText.show()

        # set quit button
        self.quitButton = QPushButton('Quit', self)
        self.__set_button(self.quitButton, 0.9)
        self.quitButton.move(int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + 200
                            , int((self.boardSize / 2) + 250))
        self.quitButton.clicked.connect(QCoreApplication.instance().quit)
        self.quitButton.show()
        self.quitButton.raise_()

        # set restart button
        self.restartton = QPushButton('Restart', self)
        self.__set_button(self.restartton, 0.9)
        self.restartton.move(int((self.boardSize / 2) - (self.startGameButton.width() / 2)) + 80
                            , int((self.boardSize / 2) + 250))
        self.restartton.clicked.connect(self.returnToStartScreen2)
        self.restartton.show()
        self.restartton.raise_()

    def returnToStartScreen2(self):
        self.restartton.hide()
        self.winConText.hide()
        self.quitButton.hide()
        self.winCon.hide()
        self.conpic.hide()
        self.conpic1.hide()
        self.conpic2.hide()
        self.returnToStartScreen()

    def update_captured_pieces(self):
        # grab new list of captured piece labels
        wCapLabels = [item[0] for item in self.controller.get_pieces_captured_by("white")]
        bCapLabels = [item[0] for item in self.controller.get_pieces_captured_by("black")]

        # create updated capture boxes with new lists
        white = PieceGroup(wCapLabels, 5, 0, 25)
        black = PieceGroup(bCapLabels, 5, 0, 25)

        #store these new capture groups
        self.captured_by["white"] = white
        self.captured_by["black"] = black

        # check if the captured frames have layouts
        current_wBox = self.wCapLayout.itemAt(0).widget()
        current_bBox = self.bCapLayout.itemAt(0).widget()
        if current_wBox and current_bBox:
            print("has")
            self.wCapLayout.replaceWidget(current_wBox, white)
            current_wBox.setParent(None)
            self.bCapLayout.replaceWidget(current_bBox, black)
            current_bBox.setParent(None)
        else:
            print("doesnt")
            self.wCapLayout.addWidget(white)
            self.bCapLayout.addWidget(black)

        # current_group = self.wCapturedFrame.layout.itemAt(0).widget()
        # if not current_group:

        # self.col_layouts[i-1].replaceWidget(current_group, new_piece_group)
        # current_group.setParent(None)




    """ def updated_captured_by(self, color:str):
        if color == 'white':
            starting = 425
        elif color == 'black':
            starting = 130
        else:
            return

        captured = [piece_to_img_name(piece[0]).lower()+".png" for piece in self.controller.get_pieces_captured_by(color)]

        self.captured_by[color] = []

        img_size = 35
        offset = 40
        for i, pc in enumerate(captured):

            captured_pc = QLabel(self)
            captured_pc.setAlignment(Qt.AlignCenter)
            cap = QPixmap('./picture/' + pc)
            cap = cap.scaled(img_size, img_size)
            captured_pc.setPixmap(cap)
            captured_pc.resize(img_size, img_size)
            captured_pc.move(
                int(self.boardSize - ((self.restartButton.width() - self.tableOption.width()) / 2)) - 10 + (img_size*(i%5)),
                    starting + (offset*int(i/5))
            )
            self.captured_by[color].append(captured_pc)
            # setattr(self, "wCapturedPic{}".format(i), self.wCapturedPic) """



    def delete_captured_pieces(self):
        for team in self.captured_by.values():
            for captured in team:
                captured.setParent(None)

    def make_AI_move(self):
        global ai_turn
        ai_turn = True
        if game_over:
            return
        if self.whiteAIButton.isChecked() and self.blackAIButton.isChecked():
            if self.controller.is_game_over():
                ai_turn = False
                self.handle_gameover()
                return
            self.ai_player = self.ai_v_ai_players[self.controller.tracker.current_player]
        else:
            if not self.ai_player or self.ai_turn_over():
                ai_turn = False
                return      # ai not selected, bail out of function
        self.ai_move_delay.start(self.ai_move_delay_ms)

    def ai_single_move(self):
        self.ai_move_delay.stop()

        ai_mv_map_k = self.ai_player.moveMap()
        ai_mv_map_x = self.ai_player.moveMap()
        ai_mv_map_t = self.ai_player.moveMap()
        ai_mv = self.ai_player.best_move(ai_mv_map_k, ai_mv_map_x, ai_mv_map_t)
        to_x, to_y = ai_mv[0], ai_mv[1]
        from_x, from_y = ai_mv[4], ai_mv[5]
        ai_mv_piece = self.piecePos[from_y][from_x]
        if type(ai_mv_piece).__name__ != 'PieceVis':
            return

        isAttack = (to_x, to_y, True) in self.controller.get_possible_moves_for_piece_at(x=from_x, y=from_y)
        if isAttack:
            target_piece = self.piecePos[to_y][to_x]

        moveSuccessful = self.controller.move_piece(from_x=from_x, from_y=from_y,
                                                    to_x=to_x, to_y=to_y)
        self.diceRollResult = self.controller.get_result_of_dice_roll()

        if moveSuccessful:
            new_spots = []
            for x, y in self.controller.get_move_path():
                new_spot = board_to_screen(x, y, self.tileSize)  # create pixel position of new piece
                new_spots.append(new_spot)
            ai_mv_piece.start[0] = to_x
            ai_mv_piece.start[1] = to_y
        else:
            new_spots = []
            new_spot = board_to_screen(from_x, from_y, self.tileSize)

        def updates():
            if game_over:
                return
            self._update_pieces()
            self.update_labels()
            self.update_captured_pieces()
            if isAttack:
                self.ai_attack_info = {
                    'fromx': str(chr(65+from_x)),
                    'fromy': (8-from_y),
                    'fromclr': ai_mv_piece.color.title(),
                    'fromtype': ai_mv_piece.piece_type,
                    'tox': str(chr(65+to_x)),
                    'toy': (8-to_y),
                    'toclr': target_piece.color.title(),
                    'totype': target_piece.piece_type
                }
                self.rollDiceScreen(moveSuccessful)
            else:
                self.make_AI_move()


        if len(new_spots)>1:
            new_spots.reverse()

            sbs_delay = QTimer(self)

            def ai_spot_by_spot():
                if len(new_spots)==0:
                    sbs_delay.stop()
                    updates()
                    return
                x, y = new_spots.pop()
                print(x,y)
                ai_mv_piece.move(x, y)

            sbs_delay.timeout.connect(ai_spot_by_spot)
            sbs_delay.start(self.sbs_delay_ms)
        else:
            updates()

    def ai_turn_over(self):
        whites_turn = (self.controller.tracker.get_current_player()==1)
        if self.controller.is_game_over():  # special case for gameover
            self.handle_gameover()
            return True
        return self.whiteHumanButton.isChecked() == whites_turn    # the active color is the color the human chose, no longer computer's turn


    def handle_gameover(self):
        global game_over
        game_over = True
        self.endTurnButton.hide()
        self.moveIndicator.hide()
        self.tableOption.setText("Winner: " +
                                ("White" if self.controller.tracker.get_current_player() else "Black") +
                                " Team!")
        return

    def smallSelectButtonClicked(self):
        make_smaller(self)
        self.resetBoardSize()
        self.set_theme(screentheme)
        self.showStartScreen()
        self.show()

    def largeSelectButtonClicked(self):
        make_larger(self)
        self.resetBoardSize()
        self.set_theme(screentheme)
        self.showStartScreen()
        self.show()

    def revertToDefaultClicked(self):
        make_default(self)
        self.resetBoardSize()
        self.set_theme(screentheme)
        self.showStartScreen()
        self.show()

    def startGameClicked(self):
        global game_over
        game_over = False

        self.theme_menu.close()
        if self.medievalButton.isChecked():
            self.__game_type = "Medieval"
            self.corpButton.hide()
        elif self.corpCommanderButton.isChecked():
            self.__game_type = "Corp"
            self.corpButton.show()
        self.controller = chess_game(game_type=self.__game_type)
        if self.__game_type == "Corp":
            self.corp_menu = CorpMenu(self)

        self._update_pieces()
        self.update_labels()
        self.update_captured_pieces()

        if self.onhighlight.isChecked():
            self.h_mode = True
        elif self.offhighlight.isChecked():
            self.h_mode = False

        self.hideStartScreen()
        self.tableOption.show()
        self.moveIndicator.show()
        self.restartButton.show()
        self.endTurnButton.show()
        self.helperButton.show()
        self.helperButton.raise_()

        self.controller.tracker.current_player = 1

        self.ai_player = None
        self.ai_v_ai_players = []

        # whiteHuman v blackHuman default

        if self.whiteAIButton.isChecked() and self.blackAIButton.isChecked():
            # whiteAI v blackAI
            self.controller.tracker.current_player = 1
            ai_1 = AIFunctions(self.controller, 1)
            ai_2 = AIFunctions(self.controller, 0)
            self.ai_v_ai_players = [ai_2, ai_1]
            self.make_AI_move()
        elif self.whiteHumanButton.isChecked() and self.blackAIButton.isChecked():
            # whiteHuman v blackAI
            self.ai_player = AIFunctions(self.controller, 0)
        elif self.whiteAIButton.isChecked() and self.blackHumanButton.isChecked():
            # whiteAI v blackHuman
            self.ai_player = AIFunctions(self.controller, 1)
            self.make_AI_move()


    def __rolldiceWork(self):
        moveIntoSidePanel = ((self.width()-self.boardSize)/2)
        # Set up roll dice text properties
        self.rollText.setAlignment(Qt.AlignCenter)
        self.rollText.setText("Rolling Dice...")
        self.rollText.resize(900, 100)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.rollText.height() * 0.4)
        self.rollText.setFont(font)
        self.rollText.move(int((self.boardSize / 2) - (self.rollText.width() / 2)) + moveIntoSidePanel,
                           int((self.boardSize / 2) - 300))
        self.rollText.hide()

        if self.ai_attack_info:
            self.aiPieceInfoText.setAlignment(Qt.AlignCenter)
            self.aiPieceInfoText.resize(900, 100)
            font = QFont()
            font.setFamily('Arial')
            font.setPixelSize(self.aiPieceInfoText.height() * 0.3)
            self.aiPieceInfoText.setFont(font)
            self.aiPieceInfoText.move(int((self.boardSize / 2) - (self.rollText.width() / 2)) + moveIntoSidePanel,
                            int((self.boardSize / 2))+200)
            text = \
                f"{self.ai_attack_info['fromclr']} {self.ai_attack_info['fromtype']} " \
                f"({self.ai_attack_info['fromx']}{self.ai_attack_info['fromy']}) " \
                "attacking " \
                f"{self.ai_attack_info['toclr']} {self.ai_attack_info['totype']} " \
                f"({self.ai_attack_info['tox']}{self.ai_attack_info['toy']}) " \

            self.aiPieceInfoText.setText(text)
            self.aiPieceInfoText.show()
            self.aiPieceInfoText.raise_()


        # roll dice animation
        self.rollDiceAnimation.setAlignment(Qt.AlignCenter)
        self.rollDiceAnimation = QLabel(self)
        size = QSize(128, 128)
        pixmap = QMovie('./picture/dice.gif')
        self.rollDiceAnimation.setMovie(pixmap)
        pixmap.setScaledSize(size)
        self.rollDiceAnimation.resize(300, 300)
        pixmap.start()
        self.timer = QTimer(self)
        self.timer.setSingleShot(True)
        self.timer.setInterval(2000)
        self.timer.timeout.connect(self.__roll_dice)
        self.timer.start()
        self.rollDiceAnimation.move(300+moveIntoSidePanel, 200)
        self.rollDiceAnimation.hide()

    def __roll_dice(self):
        moveIntoSidePanel = ((self.width()-self.boardSize)/2)
        # Set up capture result text properties
        self.rollText.hide()
        self.resultCaptureText.setAlignment(Qt.AlignCenter)
        self.resultCaptureText.resize(900, 100)
        font = QFont()
        font.setFamily('Arial')
        font.setPixelSize(self.resultCaptureText.height() * 0.4)
        self.resultCaptureText.setFont(font)
        self.resultCaptureText.move(int((self.boardSize / 2) - (self.rollText.width() / 2)) + moveIntoSidePanel,
                           int((self.boardSize / 2) - 300))

        pixmap1 = QPixmap('./picture/die' + str(self.diceRollResult))
        pixmap1 = pixmap1.scaled(128, 128)
        self.rollDiceAnimation.setPixmap(pixmap1)
        self.rollDiceAnimation.move(300 + moveIntoSidePanel, 200)
        # update when after roll
        self.resultCaptureText.clear()
        if self.controller.is_game_over():
            self.resultCaptureText.setText("Capture Successful! \n Game Over!!")
            global game_over
            game_over = True
            self.endTurnButton.hide()
            self.moveIndicator.hide()
            self.tableOption.setText("Winner: " +
                                    ("White" if self.controller.tracker.get_current_player() else "Black") +
                                    " Team!")
        else:
            self.resultCaptureText.setText("Capture " + ("Successful!" if self.attackSuccess else "Failed!"))

        if ai_turn:
            okayTimer = QTimer(self)
            okayTimer.setSingleShot(True)
            okayTimer.setInterval(2500)
            okayTimer.timeout.connect(self.okayButtonClicked)
            okayTimer.start()
            self.ai_attack_info = None
        else:
            self.okayButton.show()
            self.okayButton.raise_()


        #clear attack var
        self.attackSuccess = None

    def okayButtonClicked(self):
        self.hidepauseBackground()
        self.update_captured_pieces()
        self.make_AI_move() #TODO: find place for this after update pieces is fixed

        #set celebrate action
        if self.controller.is_game_over():
            global game_over
            game_over = True
            self.congratulations()

    def __set_button(self, button: QPushButton, scale):
        font = QFont()
        font.setFamily("Arial")
        font.setPixelSize(button.height() * scale)
        button.setFont(font)

    def __set_facing_mode(self, val):
        self.white_pov = val
        self.set_non_playables()
        self._update_pieces()

    def endTurnClicked(self):
        if self.whiteAIButton.isChecked() and self.blackAIButton.isChecked():
            return
        self.controller.tracker.end_turn()
        self.ai_move_delay.stop()
        self._update_pieces()
        self.remove_all_h()
        self.update_labels()
        self.reset_movement_data()
        self.make_AI_move()

    def corpBClicked(self):
        for i in range(1,4):
            self.corp_menu.update_leader(i)
            self.corp_menu.update_group(i)
        self.corp_menu.show()

    def update_labels(self):
        self.tableOption.setText("Current Player: " + ("White" if self.controller.tracker.get_current_player() else "Black"))
        self.moveIndicator.setText("Remaining Moves: " + str(self.controller.tracker.get_number_of_available_moves() ))

    def showStartScreen(self):
        self.startScreen.show()
        self.startScreen.raise_()
        self.welcomeText.show()
        self.welcomeText.raise_()
        self.options.show()
        self.options.raise_()

        self.optionScreen.show()
        self.optionScreen.raise_()
        self.whiteTeamText.show()
        self.whiteTeamText.raise_()
        self.blackTeamText.show()
        self.blackTeamText.raise_()
        self.highlightText.show()
        self.highlightText.raise_()
        self.gameTypeText.show()
        self.gameTypeText.raise_()

        self.whiteHumanButton.show()
        self.whiteHumanButton.raise_()
        self.whiteAIButton.show()
        self.whiteAIButton.raise_()

        self.blackHumanButton.show()
        self.blackHumanButton.raise_()
        self.blackAIButton.show()
        self.blackAIButton.raise_()

        self.offhighlight.show()
        self.offhighlight.raise_()
        self.onhighlight.show()
        self.onhighlight.raise_()
        self.medievalButton.show()
        self.corpCommanderButton.show()
        self.medievalButton.raise_()
        self.corpCommanderButton.raise_()

        self.startGameButton.show()
        self.startGameButton.raise_()

        self.smallSelectButton.show()
        self.smallSelectButton.raise_()

        self.largeSelectButton.show()
        self.largeSelectButton.raise_()

        self.revertDefault.show()
        self.revertDefault.raise_()

    def hideStartScreen(self):
        self.startScreen.hide()
        self.welcomeText.hide()
        self.options.hide()

        self.whiteHumanButton.hide()
        self.whiteAIButton.hide()
        self.blackHumanButton.hide()
        self.blackAIButton.hide()

        self.whiteTeamText.hide()
        self.optionScreen.hide()
        self.blackTeamText.hide()

        self.offhighlight.hide()
        self.onhighlight.hide()
        self.medievalButton.hide()
        self.corpCommanderButton.hide()
        self.highlightText.hide()
        self.gameTypeText.hide()
        self.startGameButton.hide()
        self.smallSelectButton.hide()
        self.largeSelectButton.hide()
        self.revertDefault.hide()

    def returnToStartScreen(self):
        self.ai_move_delay.stop()
        global game_over
        game_over = True
        global ai_turn
        ai_turn = False
        self.restartButton.hide()
        self.endTurnButton.hide()
        self.moveIndicator.hide()
        self.tableOption.hide()
        self.corpButton.hide()
        self.helperButton.hide()
        self.hidepauseBackground()
        self.showStartScreen()
        self.remove_all_h()
        self.reset_movement_data()

    def rollDiceScreen(self, attackSuccess:bool):
        self.attackSuccess = attackSuccess
        self.pauseBackground.show()
        self.pauseBackground.raise_()
        self.__rolldiceWork()
        self.rollDiceAnimation.show()
        self.rollDiceAnimation.raise_()
        self.rollText.show()
        self.rollText.raise_()
        self.resultCaptureText.show()
        self.resultCaptureText.raise_()

    def hidepauseBackground(self):
        self.pauseBackground.hide()
        self.rollText.hide()
        self.rollDiceAnimation.hide()
        self.resultCaptureText.hide()
        self.resultCaptureText.clear()
        self.aiPieceInfoText.clear()
        self.aiPieceInfoText.hide()
        self.okayButton.hide()

    def set_non_playables(self):
        light, dark, border = self.theme['board']
        if self.corner_tile:
            self.corner_tile.setPixmap(QPixmap('./picture/' + border))
            self.corner_tile.resize(squareSize, squareSize)
            self.corner_tile.setScaledContents(True)
        else:
            self.corner_tile = self.mk_basic_label(border)
            self.corner_tile.move(0, 0)
        self.set_emptys(light, dark, "gt", "ot")
        self.set_lets_and_nums(border)

    def set_lets_and_nums(self, border_bg:str=""):
        letters = ["A", "B", "C", "D", "E", "F", "G", "H"]
        nums = ["8", "7", "6", "5", "4", "3", "2", "1"]
        if not len(self.border):
            self.border.append([])
            self.border.append([])
            if not self.white_pov:
                letters.reverse()
                nums.reverse()
            for i, (ltr, num) in enumerate(zip(letters, nums)):
                l1 = self.mk_basic_label(border_bg+ltr)
                l2 = self.mk_basic_label(border_bg+num)
                l1.move(int( (i + 1) * self.tileSize), 0)
                l2.move(0, int( (i + 1) * self.tileSize))
                l1.show()
                l2.show()
                self.border[0].append(l1)
                self.border[1].append(l2)
        else:
            for i, (ltr, num) in enumerate(zip(letters, nums)):
                self.border[0][i].setPixmap(QPixmap('./picture/' + border_bg+ltr))
                self.border[1][i].setPixmap(QPixmap('./picture/' + border_bg+num))

                label1 = self.border[0][i]
                label2 = self.border[1][i]
                label1.resize(squareSize, squareSize)
                label1.setScaledContents(True)
                label2.resize(squareSize, squareSize)
                label2.setScaledContents(True)

                label1.move(int((i + 1) * self.tileSize), 0)
                label2.move(0, int((i + 1) * self.tileSize))
                label1.show()
                label2.show()



    def set_emptys(self, white, black, move_h, atk_h):
        is_white = True
        for j in range(8):
            for i in range(8):
                name = white if is_white else black
                if self.tilePos[j][i] == "0":
                    label = TileVis(name,  move_h, atk_h, parent=self)
                    label.setPixmap(QPixmap('./picture/' + name))
                    label.resize(squareSize, squareSize)
                    label.setScaledContents(True)
                    label.move(int((i+1) * self.tileSize), int((j+1) * self.tileSize))
                    self.tilePos[j][i] = label
                else:
                    self.tilePos[j][i].set_default_vis(QPixmap('./picture/' + name))
                    label1 = self.tilePos[j][i]
                    label1.resize(squareSize, squareSize)
                    label1.setScaledContents(True)
                    label1.move(int((i + 1) * self.tileSize), int((j + 1) * self.tileSize))

                is_white = not is_white
            is_white = not is_white

    def mk_basic_label(self, name):
        label = QLabel(parent=self)
        label.setPixmap(QPixmap('./picture/' + name))
        label.resize(squareSize, squareSize)
        label.setScaledContents(True)
        return label

    def _update_pieces(self):
        print("updating pieces")
        pieces_array = self.controller.get_board()
        for y in range(8):
            for x in range(8):
                cur_p = self.piecePos[y][x]
                if cur_p and cur_p != "0":
                        cur_p.setParent(None)
                piece, corp_name = pieces_array[y][x]
                corp_color_name = ""
                if corp_name:
                    corp_num = corp_name[-1]
                    corp_color_name = corp_to_color(int(corp_num))
                piece = piece_to_img_name(piece)
                if not piece:
                    continue
                piece_color = 'white' if piece[0]=='w' else 'black'
                label = PieceVis(piece + corp_color_name, x, y, color=piece_color, parent=self)
                    # Set the image based on the array element.
                label.resize(squareSize, squareSize)
                label.setScaledContents(True)
                label.move(int((x+1) * self.tileSize), int((y+1) * self.tileSize))
                label.show()
                self.piecePos[y][x] = label

    def update_flipped(self):
        pass

class PieceGroup(QWidget):
    def __init__(self, labels, items_per_row, corp_num, label_size):
        super(PieceGroup, self).__init__()
        self.corp_color = corp_to_color(corp_num)
        self.row_items = items_per_row
        self.labels = labels
        self.create_group(label_size)
    # Changed layout mode to grid

    def create_group(self, size):

        layout = QGridLayout()
        num_rows = len(self.labels) / self.row_items
        for i in range(floor(num_rows) + 1):
            if len(self.labels) <= 0:
                self.setLayout(layout)
                return
            elif len(self.labels) >= self.row_items:
                cur_row_items = self.row_items
            else:
                cur_row_items = len(self.labels)
            for j in range(cur_row_items):
                piece_name = self.labels.pop()
                label_name = piece_to_img_name(piece_name)
                label = corpVis(label_name + self.corp_color, piece_name, size)
                layout.addWidget(label, i, j)


        self.setLayout(layout)

    def custom_size(self, x_size, y_size):
        self.setFixedSize(x_size, y_size)


class Deleg_Label(QWidget):
    def __init__(self, corp_data):
        super(Deleg_Label, self).__init__()
        layout = QHBoxLayout()
        self.corp_data = corp_data
        self.left_opt = QComboBox()
        self.left_opt.addItems(["Delegate","Recall"])
        self.left_opt.currentTextChanged.connect(self.on_left_changed)
        self.corp_opt = QComboBox()
        self.set_corp_options()
        self.corp_opt.currentTextChanged.connect(self.on_corp_changed)
        self.piece_opt = QComboBox()
        self.set_piece_options()
        self.label = QLabel()
        self.set_label_txt()

        layout.addWidget(self.left_opt)
        layout.addWidget(self.piece_opt)
        layout.addWidget(self.label)
        layout.addWidget(self.corp_opt)
        self.setLayout(layout)

    def get_swap_data(self):
        if self.left_opt.currentIndex():
            from_corp = self.corp_opt.currentText()
            to_corp = self.get_king_corp()
        else:
            from_corp = self.get_king_corp()
            to_corp = self.corp_opt.currentText()
        piece = self.piece_opt.currentText()
        return [piece, from_corp, to_corp]

    def set_corp_data(self, new_data):
        self.corp_data = new_data

    def on_left_changed(self):
        self.set_label_txt()
        self.set_piece_options()

    def on_corp_changed(self):
        self.set_piece_options()

    def set_label_txt(self):
        text = 'to' if self.left_opt.currentIndex() == 0 else 'from'
        self.label.setText(text)

    def set_corp_options(self):
        swappable = [corp_name for i, corp_name in enumerate(self.corp_data.keys()) if i in [0,2]]
        self.corp_opt.addItems(swappable)

    def get_king_corp(self):
        king_corp = list(self.corp_data.keys())
        return king_corp[1]

    def set_piece_options(self):
        self.piece_opt.clear()
        if self.left_opt.currentIndex():
            self.piece_opt.addItems(self.corp_data[self.corp_opt.currentText()])    # true is Recall
        else:
            self.piece_opt.addItems(self.corp_data[self.get_king_corp()])


class LeaderBox(QWidget):
    def __init__(self, leader, corp):

        super(LeaderBox, self).__init__()
        self.leader = leader
        self.commander = self.create_leader_icon(corp)

        commander_row = QHBoxLayout()
        commander_row.addStretch(1)
        commander_row.addWidget(self.commander)
        commander_row.addStretch(1)

        self.top = QVBoxLayout()
        self.top.addLayout(commander_row)
        self.top.setContentsMargins(0, 10, 0, 10)


        top_frame = QFrame()
        top_frame.setFrameShape(QFrame.StyledPanel)
        top_frame.setLayout(self.top)
        layout = QVBoxLayout()
        layout.addWidget(top_frame)
        self.setLayout(layout)

    def create_leader_icon(self, corp):
        size = squareSize
        color = corp_to_color(corp)
        leader_img = piece_to_img_name(self.leader)
        return corpVis(leader_img + color, self.leader, size)

class KingBox(LeaderBox):
    def __init__(self, leader, corp, corps):
        super().__init__(leader, corp)
        self.corps_ref = corps

        self.swap_line = Deleg_Label(self.get_corp_options())
        self.top.addWidget(self.swap_line)
        self.confirm_button = QPushButton("Confirm")
        self.top.addWidget(self.confirm_button)


    # could probably use the original data but this works out more nicely
    def get_corp_options(self):
        options = {}
        for i in range(1,4):
            options[self.corps_ref[i]['name']] = self.corps_ref[i]['commanding']
        return options

    def update_deleg_line(self):
        data = self.get_corp_options()
        self.swap_line.set_corp_data(data)

    def disable_button(self, val):
        self.confirm_button.setDisabled(val)

class CorpMenu(QWidget):
    def __init__(self, main_window):
        super(CorpMenu, self).__init__()
        self.setGeometry(0,0, 1, 1)
        self.setWindowTitle("Corp Delegation")
        self.main_window = main_window
        self.controller : chess_game = main_window.controller
        self.col_layouts = []
        self.leaders = []
        self.set_corps()    #used the first time to create all layouts and attach them appropriately
        self.corps_ref = {}
        self.king_box = None

    def set_corps(self):
        self.update_data()
        layout = QHBoxLayout()
        for i in (range(1,4)):
            self.create_col(layout, self.corps_ref[i]['commander'], self.corps_ref[i]['commanding'], i)
        self.setLayout(layout)

    def confirm_clicked(self):
        swap_data = self.king_box.swap_line.get_swap_data()
        self.controller.delegate_or_recall(piece=swap_data[0], from_corp=swap_data[1], to_corp=swap_data[2])
        self.update_data()
        self.king_box.corps_ref = self.corps_ref
        self.king_box.update_deleg_line()
        self.king_box.disable_button(self.controller.tracker.delegation_move_has_been_used())
        self.update_all_groups()
        self.main_window._update_pieces()

    def update_data(self):
        is_white = self.controller.tracker.get_current_player()
        self.corps_ref = self.controller.get_corp_info(white=is_white)

    def create_col(self, outer_layout, leader, group, num):
        leader_box = LeaderBox(leader, num)
        col = QVBoxLayout()
        self.col_layouts.append(col)
        col.addWidget(leader_box)
        col.addWidget(PieceGroup(group,3, num, 50))
        col.setSpacing(0)
        col.setContentsMargins(10,0,10,0)
        col_frame = QFrame()
        col_frame.setFrameShape(QFrame.StyledPanel)
        col_frame.setLayout(col)
        outer_layout.addWidget(col_frame)

    # I split these up since there are situations that we want one without the other
    # namely, when corps switch pieces
    def update_leader(self, i):
        self.update_data()
        leader = self.corps_ref[i]['commander']
        if i == 2:
            new_leader = KingBox(leader, i, self.corps_ref)
            new_leader.disable_button(self.controller.tracker.delegation_move_has_been_used())
            new_leader.confirm_button.clicked.connect(self.confirm_clicked)
            self.king_box = new_leader
        else:
            new_leader = LeaderBox(leader, i)
        current_leader = self.col_layouts[i-1].itemAt(0).widget()
        self.col_layouts[i-1].replaceWidget(current_leader, new_leader)
        current_leader.setParent(None)

    def update_all_groups(self):
        for i in range(1,4):
            self.update_group(i)

    def update_group(self, i):
        self.update_data()
        group = self.corps_ref[i]['commanding']
        new_piece_group = PieceGroup(group, 3, i, 50)
        current_group = self.col_layouts[i-1].itemAt(self.col_layouts[i-1].count() - 1).widget()
        self.col_layouts[i-1].replaceWidget(current_group, new_piece_group)
        current_group.setParent(None)

class ThemeField(QWidget):
    def __init__(self, name, img_name):
        super(ThemeField,self).__init__()
        self.theme_name = name
        self.select_button = QPushButton('', self)
        self.theme_preview = QLabel()
        image = QPixmap('./picture/'+ img_name)
        icon  = QIcon(image)
        self.select_button.setIcon(icon)
        self.select_button.setFixedSize(300,150)
        self.select_button.setIconSize(QSize(300,300))
        theme_pair = QHBoxLayout()
        theme_pair.addWidget(self.select_button)
        self.setLayout(theme_pair)

    def set_click_func(self, func):
        self.select_button.clicked.connect(lambda:  func(self.theme_name))

    def get_theme(self):
        return self.theme_name

class ThemeMenu(QWidget):
    def __init__(self, x_size, y_size, main_window):
        super(ThemeMenu, self).__init__()
        self.setWindowTitle("Theme Menu")
        self.hide()
        self.main_window = main_window
        self.theme = 'default'
        themes_layout = QVBoxLayout()
        themes_layout.addWidget( self.add_theme('default', 'defaultPreview') )
        themes_layout.addWidget( self.add_theme('wood', 'woodPreview') )
        themes_layout.addWidget( self.add_theme('marble', 'marblePreview') )
        themes_layout.addStretch(5)
        themes_layout.setSpacing(0)
        self.setLayout(themes_layout)

    def get_theme(self) -> str:
        return self.theme

    def set_theme(self, name):
        global screentheme
        screentheme = name
        self.main_window.set_theme(name)


    def add_theme(self, name, img):
        theme = ThemeField(name, img)
        theme.set_click_func(self.set_theme)
        return theme

class displayRules(QWebEngineView):
    class WebEnginePage(QWebEnginePage):
        def javaScriptConsoleMessage(self, level, msg, line, sourceID):
            pass

    def __init__(self):
        super(displayRules, self).__init__()
        self.resize(helpScreenWidth, helpScreenHeight)
        self.setPage(self.WebEnginePage(self))
        self.settings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        self.settings().setAttribute(QWebEngineSettings.PdfViewerEnabled, True)
        self.setWindowTitle("Chess Rules")
        #self.load(QUrl.fromLocalFile(QDir.current().filePath('viewer.html')))
        # url = QUrl("http://localhost:63342/AIPlayableFLChess/viewer.html?_ijt=ni08m56q8ooig04o54nbs7pt1d&_ij_reload=RELOAD_ON_SAVE")
        #self.load(QUrl.fromLocalFile(QDir.current().filePath("viewer.html")))

        self.load(QUrl(f"http://localhost:63342/AIPlayableFLChess/viewer.html"))

