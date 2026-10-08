l = [' ', "A", "B", "C", "D", "E", "F", "G", "H"]


class Board:
    def __init__(self):
        self.board = [[None for i in range(8)] for j in range(8)]
        self.gameOver = False
        self.setup()

    def setup(self):
        for c in range(8): self.board[1][c] = Pawn('white', (1, c))
        for c in range(8): self.board[6][c] = Pawn('black', (6, c))

        self.board[0][0] = Rook('white', (0, 0))
        self.board[0][7] = Rook('white', (0, 7))
        self.board[7][7] = Rook('black', (7, 7))
        self.board[7][0] = Rook('black', (7, 0))

        self.board[0][2] = Bishop('white', (0, 2))
        self.board[0][5] = Bishop('white', (0, 5))
        self.board[7][5] = Bishop('black', (7, 5))
        self.board[7][2] = Bishop('black', (7, 2))

        self.board[0][1] = Knight('white', (0, 1))
        self.board[0][6] = Knight('white', (0, 6))
        self.board[7][6] = Knight('black', (7, 6))
        self.board[7][1] = Knight('black', (7, 1))

        self.board[0][3] = Queen('white', (0, 3))
        self.board[7][3] = Queen('black', (7, 3))

        self.board[0][4] = King('white', (0, 4))
        self.board[7][4] = King('black', (7, 4))

    def printBoard(self):
        l = [' ', "A", "B", "C", "D", "E", "F", "G", "H"]
        n = 1

        print('   '.join(l))
        print("  --- --- --- --- --- --- --- --- ")

        for row in self.board:
            row_display = []
            for cell in row:
                if cell is None:
                    row_display.append(' ')
                else:
                    row_display.append(cell.type if cell.color == 'white' else cell.type.lower())
            print(f"{n} | " + " | ".join(row_display) + " |")
            print("  --- --- --- --- --- --- --- --- ")
            n += 1
        print()

    def getPiece(self, row, col):
        return self.board[row][col]

    def pathClear(self, r1, c1, r2, c2):
        rowStep = (r2 > r1) - (r2 < r1)
        colStep = (c2 > c1) - (c2 < c1)
        r = r1 + rowStep
        c = c1 + colStep
        while (r, c) != (r2, c2):
            if self.board[r][c] is not None:
                return False
            r += rowStep
            c += colStep
        return True

    def movePiece(self, c, n, turn):
        current = self.board[c[1]][c[0]]
        new = self.board[n[1]][n[0]]

        if current is None:
            print("There is no piece on that square.")
            return False
        if current.color != turn:
            print("That's not your piece!")
            return False
        if new is not None and new.color == turn:
            print("You can't capture your own piece.")
            return False
        if not current.validMove(n, self):
            print("That piece can't move like that.")
            return False

        self.board[n[1]][n[0]] = current
        self.board[c[1]][c[0]] = None
        current.position = (n[1], n[0])

        # Promotion
        if current.type == 'P' and (n[1] == 0 or n[1] == 7):
            self.board[n[1]][n[0]] = Queen(current.color, (n[1], n[0]))
            print("Your pawn became a queen!")

        # King capture
        if new is not None and new.type == 'K':
            self.gameOver = True

        return True


def getInput():
    cur = input("Current (format: e 4): ").split()
    if len(cur) == 1 and cur[0].lower() == "quit":
        return None, None
    new = input("Shift: ").split()
    c = [l.index(cur[0].capitalize()) - 1, int(cur[1]) - 1]
    n = [l.index(new[0].capitalize()) - 1, int(new[1]) - 1]
    return c, n


class Pawn:
    def __init__(self, color, position):
        self.color = color.lower()
        self.position = position
        self.type = 'P'

    def validMove(self, n, board):
        row, col = self.position
        newRow, newCol = n[1], n[0]
        target = board.getPiece(newRow, newCol)

        if self.color == 'white':
            step = 1
            startRow = 1
        else:
            step = -1
            startRow = 6

        if newCol == col and target is None:
            if newRow == row + step:
                return True
            # Two squares
            if row == startRow and newRow == row + 2 * step and board.getPiece(row + step, col) is None:
                return True

        # Capture diagonally
        if abs(newCol - col) == 1 and newRow == row + step and target is not None:
            return True

        return False


class Rook:
    def __init__(self, color, position):
        self.color = color.lower()
        self.position = position
        self.type = 'R'

    def validMove(self, n, board):
        row, col = self.position
        newRow, newCol = n[1], n[0]
        if row == newRow or col == newCol:
            return board.pathClear(row, col, newRow, newCol)
        return False


class Bishop:
    def __init__(self, color, position):
        self.color = color.lower()
        self.position = position
        self.type = 'B'

    def validMove(self, n, board):
        row, col = self.position
        newRow, newCol = n[1], n[0]
        if abs(newRow - row) == abs(newCol - col):
            return board.pathClear(row, col, newRow, newCol)
        return False


class Queen:
    def __init__(self, color, position):
        self.color = color.lower()
        self.position = position
        self.type = 'Q'

    def validMove(self, n, board):
        row, col = self.position
        newRow, newCol = n[1], n[0]
        straight = row == newRow or col == newCol
        diagonal = abs(newRow - row) == abs(newCol - col)
        if straight or diagonal:
            return board.pathClear(row, col, newRow, newCol)
        return False


class King:
    def __init__(self, color, position):
        self.color = color.lower()
        self.position = position
        self.type = 'K'

    def validMove(self, n, board):
        row, col = self.position
        newRow, newCol = n[1], n[0]
        return abs(newRow - row) <= 1 and abs(newCol - col) <= 1


class Knight:
    def __init__(self, color, position):
        self.color = color.lower()
        self.position = position
        self.type = 'N'

    def validMove(self, n, board):
        row, col = self.position
        newRow, newCol = n[1], n[0]
        return (abs(newRow - row), abs(newCol - col)) in [(1, 2), (2, 1)]


chess_board = Board()
turn = 'white'
print("Welcome to Simple Chess! Type squares like: e 2   (type 'quit' to exit)")

while not chess_board.gameOver:
    chess_board.printBoard()
    print(turn.capitalize() + "'s turn.")
    try:
        c, n = getInput()
    except (ValueError, IndexError):
        print("Please type squares like: e 2 (letter a-h, number 1-8)")
        continue

    if c is None:
        print("Game ended.")
        break

    if chess_board.movePiece(c, n, turn):
        if chess_board.gameOver:
            chess_board.printBoard()
            print(turn.capitalize() + " wins by capturing the king!")
        else:
            turn = 'black' if turn == 'white' else 'white'
