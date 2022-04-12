import random

from ChessGame import Game


#game = Game()

class AIFunctions:
    def __init__(self, game: Game, color):
        self.game = game
        self.color = color
        self.board = self.game._get_board()
        self.total_success_moves = 0
        self.total_moves_attempted = 0
        self.last_turn = 0
        self.hostilemap = \
            [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    def updateBoard(self):
        self.board = self.game._get_board()

    def corpBalance(self):
        lcore = 0
        rcore = 0
        kcore = 0
        pawnString = ""
        rookString = ""
        for item in self.board:
            for item2 in item:
                if item2.piece:
                    if self.color == item2.piece.is_white():
                        if item2.piece.get_corp() == 'corpW1' or item2.piece.get_corp() == 'corpB1':
                            kcore = kcore + self.pieceweight(item2.piece)
                        elif item2.piece.get_corp() == 'corpW2' or item2.piece.get_corp() == 'corpB2':
                            lcore = lcore + self.pieceweight(item2.piece)
                        elif item2.piece.get_corp() == 'corpW2'  or item2.piece.get_corp() == 'corpB3':
                            rcore = rcore + self.pieceweight(item2.piece)

        #checks if a corp has more than the king
        #if so, the king takes a piece from that corp
        if kcore - rcore > kcore - lcore:
            print(lcore - kcore)
            if(lcore - kcore>=2):
                print("taking rook from lcore")
                # TODO: get location of designated piece(ensuring its still in play)
                #  and return the piece as an object along with the corp it should be changed to
            else:
                print("taking pawn from lcore")
        elif kcore - rcore < kcore - lcore:
            print(rcore - kcore)
            if (rcore - kcore >= 2):
                print("taking rook from rcore")
            else:
                print("taking pawn from rcore")



    #rcore 7
    #lcore 7
    #kcore 10
    #idea is to balance corps out. IE, if the kings corp loses
    #a power piece, the bishops will
    def pieceweight(self, piece):
        if piece.get_type() == 'Pawn':
            return 1
        elif piece.get_type() == 'Rook':
            return 2
        elif piece.get_type() == 'Knight':
            return 4
        elif piece.get_type() == 'Queen':
            return 4

    def __get_position_of_piece(self, piece_name: str):
        if len(piece_name) == 0 or piece_name[0] not in ('w', 'b'):
            print('empty or not w or not b')
            return (-1, -1)

        some_pieces = {
            'Kt': ["1", "2"],
            'R': ["1", "2"],
            'B': ["1", "2"],
            'P': ["1", "2", "3", "4", "5", "6", "7", "8"]
        }

        if "Kg" in piece_name or "Q" in piece_name:
            if len(piece_name) != 3:
                print('invalid royalty piece name')
                return (-1, -1)
        elif not (piece_name[1:-1] in some_pieces and piece_name[-1] in some_pieces[piece_name[1:-1]]):
            print('invalid non royalty piece name')
            return (-1, -1)

        for y, row in enumerate(self.game.get_board()):
            for x, spot in enumerate(row):
                pc, corp = spot
                if pc == piece_name:
                    return (x, y)
        print('piece not on board')
        return (-1, -1)

    # weights attack areas based on friendly piece power
    def attackRef(self, x, y, piece):
        defpiece = None
        for item in self.board:
            for item2 in item:
                if item2.piece:
                    if a == x and b == y:
                        defpiece = item2.piece
                a = a + 1
            b = b + 1
            a = 0
        #case needs to be handled where defpiece isn't assigned or determine why it isn't
        if defpiece:
            type = defpiece.get_type()
        else:
            return 0

        if piece.get_type() == 'Pawn':
            if type == 'Pawn':
                return 3
            elif type == 'Bishop':
                return 2
            else:
                return 1
        elif piece.get_type() == 'Rook':
            if type == 'Pawn' or type == 'Bishop' or type == 'Rook':
                return 2
            else:
                return 3
        elif piece.get_type() == 'Bishop':
            if type == 'Pawn':
                return 4
            if type == 'Bishop':
                return 3
            else:
                return 2
        elif piece.get_type() == 'Knight':
            if type == 'Pawn':
                return 5
            else:
                return 2
        elif piece.get_type() == 'Queen':
            if type == 'Rook':
                return 2
            if type == 'Pawn':
                return 5
            else:
                return 3
        elif piece.get_type() == 'King':
            if type == 'Rook':
                return 2
            if type == 'Pawn':
                return 6
            else:
                return 3

    def genHostileMap(self):
        x = 0
        y = 0

        KingLocation = (0, 5)

        self.hostilemap = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]]

        for item in self.board:
            for item2 in item:
                if item2.piece:
                    if self.color != item2.piece.is_white():
                        moveList = self.game.get_possible_moves_for_piece_at(x=y, y=x, ai_backdoor=True)

                        if (item2.piece.get_type() == 'Pawn'):
                            spotVal = .2
                        elif (item2.piece.get_type() == 'Bishop' or item2.piece.get_type() == 'King'):
                            spotVal = .3
                        else:
                            spotVal = .4
                        for a, b, c in moveList:
                            self.hostilemap[b][a] += spotVal

                            found = False
                            for y_c in (-1, 0, 1):
                                for x_c in (-1, 0, 1):
                                    if (x_c, y_c) == (0, 0):
                                        continue
                                    la_x = a + x_c
                                    la_y = b + y_c
                                    if la_x > 7 or la_y > 7 or la_x < 0 or la_y < 0:
                                        continue
                                    found = (la_x, la_y) == KingLocation
                                    if found:
                                        print(self.hostilemap[b][a])
                                        self.hostilemap[b][a] -= 1000
                                        print(self.hostilemap[b][a])
                                        break
                                if found:
                                    break

                y = y + 1
            x = x + 1
            y = 0

    # returns piece object and its potential movement areas
    def moveMap(self):
        self.updateBoard()
        self.genHostileMap()
        kCore = []
        xCore = []
        yCore = []

        heatmap = [[0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0],
                   [0, 0, 0, 0, 0, 0, 0, 0]]

        x = 0
        y = 0

        player = "white" if self.game.tracker.get_current_player() else "black"

        for item in self.board:
            for item2 in item:
                if item2.piece:
                    if self.color == item2.piece.is_white():
                        moveList = self.game.get_possible_moves_for_piece_at(x=y, y=x)

                        if (item2.piece.get_type() == 'Pawn'):
                            spotVal = 2
                        elif (item2.piece.get_type() == 'Bishop' or item2.piece.get_type() == 'King'):
                            # originally 2, changed to 1 as weights for movement effect choices
                            spotVal = 1
                        else:
                            spotVal = 4
                        for l, m, p in moveList:
                            if (p):
                                heatmap[m][l] += self.attackRef(x, y, item2.piece)

                            # weighting longer moves higher
                            if (m - x == 2 or x - m == 2 or y - l == 2 or l - y == 2):
                                heatmap[m][l] += 1
                                if player == "white":
                                    if (m - x == 2 or x - m == 2 or y - l == 2):
                                        heatmap[m][l] += 2
                                if player == "black":
                                    if (m - x == 2 or x - m == 2 or l - y == 2):
                                        heatmap[m][l] += 2
                            elif (m - x == 3 or x - m == 3 or y - l == 3 or l - y == 3):
                                heatmap[m][l] += 2
                                if player == "white":
                                    if (m - x == 3 or x - m == 3 or y - l == 3):
                                        heatmap[m][l] += 3
                                if player == "black":
                                    if (m - x == 3 or x - m == 3 or l - y == 3):
                                        heatmap[m][l] += 3
                            elif (m - x == 4 or x - m == 4 or y - l == 4 or l - y == 4):
                                heatmap[m][l] += 3
                                if player == "white":
                                    if (m - x == 4 or x - m == 4 or y - l == 4):
                                        heatmap[m][l] += 4
                                if player == "black":
                                    if (m - x == 2 or x - m == 2 or l - y == 2):
                                        heatmap[m][l] += 4
                            elif (m - x == 5 or x - m == 5 or y - l == 5 or l - y == 5):
                                heatmap[m][l] += 3
                                if player == "white":
                                    if (m - x == 5 or x - m == 5 or y - l == 5):
                                        heatmap[m][l] += 4
                                if player == "black":
                                    if (m - x == 5 or x - m == 5 or l - y == 5):
                                        heatmap[m][l] += 4
                            if item2.piece.get_type() != 'King':
                                hosval = self.hostilemap[m][l] % 1000
                            else:
                                hosval = self.hostilemap[m][l]
                                print ('King Testing=======================:', hosval)

                            print ('hosval Testing=======================:', hosval)
                            heatmap[m][l] += spotVal - self.hostilemap[m][l]

                        dataChunk = [item2.piece, heatmap]

                        if (item2.piece.get_corp() == 'corpW1' or item2.piece.get_corp() == 'corpB1'):
                            kCore.append(dataChunk)
                        elif (item2.piece.get_corp() == 'corpW2' or item2.piece.get_corp() == 'corpB2'):
                            xCore.append(dataChunk)
                        else:
                            yCore.append(dataChunk)

                        heatmap = [[0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0],
                                   [0, 0, 0, 0, 0, 0, 0, 0]]



                y = y + 1
            x = x + 1
            y = 0
            print('\n')
        #self.corpSplitData(moveData)
        return kCore, xCore, yCore

    def displayMoveData(self, kCore, xCore, yCore):

        for element, array in kCore:
            print(element.get_name())
            for row in array:
                print(row)
        for element, array in xCore:
            print(element.get_name())
            for row in array:
                print(row)
        for element, array in yCore:
            print(element.get_name())
            for row in array:
                print(row)

    def best_move(self, kCore, xCore, yCore):
        max_weight = None
        BKingLocation = self.__get_position_of_piece('bKg')
        WKingLocation = self.__get_position_of_piece('wKg')
        BestSameScore = []
        print(kCore[2])

        # print('start check')
        for element, array in kCore[2]:
            SameScore = []
            max_weight_piece = None

            self.__get_position_of_piece('bKg')
            self.__get_position_of_piece('wKg')

            for y, row in enumerate(array):
                if max(row) > 0:
                    for x, weight in enumerate(row):
                        if weight != 0:
                            if ((x == WKingLocation[0] and y == WKingLocation[1])
                                    or (x == BKingLocation[0] and y == BKingLocation[1])):
                                print("Testing1========================================")
                                max_weight_piece = (x, y, weight + 20, element.get_name(), element.x_loc, element.y_loc)
                                SameScore = [max_weight_piece]
                            if not max_weight_piece:
                                if ((x == WKingLocation[0] and y == WKingLocation[1])
                                        or (x == BKingLocation[0] and y == BKingLocation[1])):
                                    max_weight_piece = (
                                    x, y, weight + 20, element.get_name(), element.x_loc, element.y_loc)
                                    SameScore = [max_weight_piece]
                                    print("Testing2========================================")
                                else:
                                    max_weight_piece = (x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                    SameScore = [max_weight_piece]
                                # sets up a max weight if there is not one already set
                                # max_weight_piece = (x, y, weight, element.get_name() , element.x_loc, element.y_loc)
                                # SameScore = [max_weight_piece]
                            else:
                                if weight > max_weight_piece[2]:
                                    if ((x == WKingLocation[0] and y == WKingLocation[1])
                                            or (x == BKingLocation[0] and y == BKingLocation[1])):
                                        max_weight_piece = (
                                        x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                        SameScore = [max_weight_piece]
                                        print("Testing3========================================")
                                    else:
                                        max_weight_piece = (
                                        x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                        SameScore = [max_weight_piece]

                                    # max_weight_piece = (x, y, weight, element.get_name() , element.x_loc, element.y_loc)
                                    # SameScore = [max_weight_piece]

                                elif weight == max_weight_piece[2]:
                                    SameScore.append((x, y, weight, element.get_name(), element.x_loc, element.y_loc))

            # # to check max weight piece after every from piece is checked
            # if max_weight_piece:
            #     print('max pc', max_weight_piece)

            if len(SameScore) > 0:
                # Shuffles the SameScore Array twice to pull a random move
                random.shuffle(SameScore)
                max_weight_piece = SameScore[0]

                if not max_weight:
                    max_weight = max_weight_piece[2]
                elif max_weight < max_weight_piece[2]:
                    BestSameScore = []
                    max_weight = max_weight_piece[2]

                if max_weight == max_weight_piece[2]:
                    BestSameScore.append(max_weight_piece)

        for element, array in xCore[0]:
            SameScore = []
            max_weight_piece = None

            self.__get_position_of_piece('bKg')
            self.__get_position_of_piece('wKg')

            for y, row in enumerate(array):
                if max(row) > 0:
                    for x, weight in enumerate(row):
                        if weight != 0:
                            if ((x == WKingLocation[0] and y == WKingLocation[1])
                                    or (x == BKingLocation[0] and y == BKingLocation[1])):
                                print("Testing1========================================")
                                max_weight_piece = (x, y, weight + 20, element.get_name(), element.x_loc, element.y_loc)
                                SameScore = [max_weight_piece]
                            if not max_weight_piece:
                                if ((x == WKingLocation[0] and y == WKingLocation[1])
                                        or (x == BKingLocation[0] and y == BKingLocation[1])):
                                    max_weight_piece = (
                                    x, y, weight + 20, element.get_name(), element.x_loc, element.y_loc)
                                    SameScore = [max_weight_piece]
                                    print("Testing2========================================")
                                else:
                                    max_weight_piece = (x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                    SameScore = [max_weight_piece]
                                # sets up a max weight if there is not one already set
                                # max_weight_piece = (x, y, weight, element.get_name() , element.x_loc, element.y_loc)
                                # SameScore = [max_weight_piece]
                            else:
                                if weight > max_weight_piece[2]:
                                    if ((x == WKingLocation[0] and y == WKingLocation[1])
                                            or (x == BKingLocation[0] and y == BKingLocation[1])):
                                        max_weight_piece = (
                                        x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                        SameScore = [max_weight_piece]
                                        print("Testing3========================================")
                                    else:
                                        max_weight_piece = (
                                        x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                        SameScore = [max_weight_piece]

                                    # max_weight_piece = (x, y, weight, element.get_name() , element.x_loc, element.y_loc)
                                    # SameScore = [max_weight_piece]

                                elif weight == max_weight_piece[2]:
                                    SameScore.append((x, y, weight, element.get_name(), element.x_loc, element.y_loc))

            # # to check max weight piece after every from piece is checked
            # if max_weight_piece:
            #     print('max pc', max_weight_piece)

            if len(SameScore) > 0:
                # Shuffles the SameScore Array twice to pull a random move
                random.shuffle(SameScore)
                max_weight_piece = SameScore[0]

                if not max_weight:
                    max_weight = max_weight_piece[2]
                elif max_weight < max_weight_piece[2]:
                    BestSameScore = []
                    max_weight = max_weight_piece[2]

                if max_weight == max_weight_piece[2]:
                    BestSameScore.append(max_weight_piece)

        for element, array in yCore[1]:
            SameScore = []
            max_weight_piece = None

            self.__get_position_of_piece('bKg')
            self.__get_position_of_piece('wKg')

            for y, row in enumerate(array):
                if max(row) > 0:
                    for x, weight in enumerate(row):
                        if weight != 0:
                            if ((x == WKingLocation[0] and y == WKingLocation[1])
                                    or (x == BKingLocation[0] and y == BKingLocation[1])):
                                print("Testing1========================================")
                                max_weight_piece = (x, y, weight + 20, element.get_name(), element.x_loc, element.y_loc)
                                SameScore = [max_weight_piece]
                            if not max_weight_piece:
                                if ((x == WKingLocation[0] and y == WKingLocation[1])
                                        or (x == BKingLocation[0] and y == BKingLocation[1])):
                                    max_weight_piece = (
                                    x, y, weight + 20, element.get_name(), element.x_loc, element.y_loc)
                                    SameScore = [max_weight_piece]
                                    print("Testing2========================================")
                                else:
                                    max_weight_piece = (x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                    SameScore = [max_weight_piece]
                                # sets up a max weight if there is not one already set
                                # max_weight_piece = (x, y, weight, element.get_name() , element.x_loc, element.y_loc)
                                # SameScore = [max_weight_piece]
                            else:
                                if weight > max_weight_piece[2]:
                                    if ((x == WKingLocation[0] and y == WKingLocation[1])
                                            or (x == BKingLocation[0] and y == BKingLocation[1])):
                                        max_weight_piece = (
                                        x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                        SameScore = [max_weight_piece]
                                        print("Testing3========================================")
                                    else:
                                        max_weight_piece = (
                                        x, y, weight, element.get_name(), element.x_loc, element.y_loc)
                                        SameScore = [max_weight_piece]

                                    # max_weight_piece = (x, y, weight, element.get_name() , element.x_loc, element.y_loc)
                                    # SameScore = [max_weight_piece]

                                elif weight == max_weight_piece[2]:
                                    SameScore.append((x, y, weight, element.get_name(), element.x_loc, element.y_loc))



            if len(SameScore) > 0:
                # Shuffles the SameScore Array twice to pull a random move
                random.shuffle(SameScore)
                max_weight_piece = SameScore[0]

                if not max_weight:
                    max_weight = max_weight_piece[2]
                elif max_weight < max_weight_piece[2]:
                    BestSameScore = []
                    max_weight = max_weight_piece[2]

                if max_weight == max_weight_piece[2]:
                    BestSameScore.append(max_weight_piece)

        if len(BestSameScore) == 0:
            self.game.tracker.end_turn()
            BestMove = (element.x_loc, element.x_loc, 0, element.get_name(), element.x_loc, element.y_loc)
        else:
            random.shuffle(BestSameScore)
            BestMove = BestSameScore[0]


        print("Best Move after everything: ", BestMove, "\n\n")

        return BestMove

    def AI_move(self, BestMove):


        print(BestMove)
        print("Moving ", BestMove[3], " from x: ", BestMove[4], " y: ", BestMove[5], "Moving to x: ", BestMove[0],
              " y: ", BestMove[1])

        if self.game.move_piece(from_x=BestMove[4], from_y=BestMove[5], to_x=BestMove[0], to_y=BestMove[1]):
            self.total_success_moves += 1
        self.total_moves_attempted += 1


    def make_move(self):
        if not self.game.is_game_over():
            if self.last_turn != self.game.tracker.get_turn_count():
                self.total_success_moves = 0
                self.total_moves_attempted = 0
            print("starting new move:")
            player = "white" if self.game.tracker.get_current_player() else "black"
            print('current player:', player)
            K = self.moveMap()
            X = self.moveMap()
            T = self.moveMap()
            y = self.best_move(K,X,T)
            self.AI_move(y)
            self.last_turn = self.game.tracker.get_turn_count()
            colour = "white" if self.color else "black"
            print(colour, "team had", self.total_success_moves, 'successful moves out of', self.total_moves_attempted,
                  'this turn')

