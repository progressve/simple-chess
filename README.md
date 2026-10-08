# Simple Chess

A two-player chess game that runs in the terminal, written in Python using classes. White and Black take turns on the same keyboard. There are no extra libraries to install.

## Requirements

- Python 3.6 or newer

## How to run

```
python chess_template_done.py
```

## How to play

The board is printed with white at the top and black at the bottom. **White pieces are uppercase** and **black pieces are lowercase**:

```
    A   B   C   D   E   F   G   H
  --- --- --- --- --- --- --- --- 
1 | R | N | B | Q | K | B | N | R |
  --- --- --- --- --- --- --- --- 
2 | P | P | P | P | P | P | P | P |
  --- --- --- --- --- --- --- --- 
3 |   |   |   |   |   |   |   |   |
  --- --- --- --- --- --- --- --- 
4 |   |   |   |   |   |   |   |   |
  --- --- --- --- --- --- --- --- 
5 |   |   |   |   |   |   |   |   |
  --- --- --- --- --- --- --- --- 
6 |   |   |   |   |   |   |   |   |
  --- --- --- --- --- --- --- --- 
7 | p | p | p | p | p | p | p | p |
  --- --- --- --- --- --- --- --- 
8 | r | n | b | q | k | b | n | r |
  --- --- --- --- --- --- --- --- 
```

| Letter | Piece  |
|--------|--------|
| P / p  | Pawn   |
| R / r  | Rook   |
| N / n  | Knight |
| B / b  | Bishop |
| Q / q  | Queen  |
| K / k  | King   |

White always goes first. On your turn you are asked for two squares, each typed as a **letter, a space, then a number**. Upper or lower case letters both work.

```
White's turn.
Current (format: e 4): e 2
Shift: e 4
```

The numbers match the row labels printed on the board, so `e 2` is the square in column E next to the row labelled `2`.

- If a move isn't allowed, you are told why and it's still your turn.
- If you type something that isn't a square (for example `z 9`), you are asked to try again.
- Type `quit` at the first prompt to end the game.

## Rules that are included

- Every piece moves the way it does in real chess.
- Rooks, bishops and queens cannot jump over other pieces. Knights can.
- Pawns move one square forward, or two squares from their starting row. They capture one square diagonally forward and cannot capture straight ahead.
- A pawn that reaches the far end of the board automatically becomes a queen.
- You can only move your own pieces and cannot capture your own pieces.
- **The game ends when a king is captured**, and the player who captured it wins.

## What is not included

This is a simplified version of chess. It does not have:

- Check or checkmate detection. You are allowed to leave your king in check, and you win by actually capturing the king.
- Castling
- En passant
- Choosing which piece a pawn becomes (it is always a queen)
- Draw rules such as stalemate, repetition or the fifty-move rule

## How the code is organised

| Part | What it does |
|------|--------------|
| `Board` | Holds the 8x8 grid. `setup()` places the pieces, `printBoard()` draws the board, `getPiece()` looks up a square, `pathClear()` checks that nothing is in the way, and `movePiece()` checks and carries out a move. |
| `Pawn`, `Rook`, `Knight`, `Bishop`, `Queen`, `King` | One class per piece. Each stores its `color`, its `position` and its `type` (the letter shown on the board), and has a `validMove()` method describing how that piece moves. |
| `getInput()` | Asks for the two squares and turns them into board coordinates. |
| Game loop (bottom of the file) | Alternates turns, shows the board, and stops when a king is captured or the player quits. |

The board is a list of lists, `board[row][col]`. Row 0 is the row labelled `1` (white's back row) and column 0 is column `A`. Empty squares are `None`.

### Adding or changing a piece's movement

Each piece's movement lives in its own `validMove(self, n, board)` method. `n` is the target square as `[column, row]`, and `self.position` is the piece's current `(row, column)`. Return `True` if the move is allowed and `False` if not.

## Ideas for next steps

1. Check detection: stop players from making a move that leaves their own king attacked
2. Checkmate and stalemate: end the game when a player has no legal move
3. Castling and en passant
4. Letting the player choose the promotion piece
