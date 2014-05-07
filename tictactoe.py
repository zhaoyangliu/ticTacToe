# coding=utf-8
import struct, string

class TicTacToeBoard:

    def __init__(self):
        self.board = (['N']*3,['N']*3,['N']*3)
        self.count = 0
        self.val = 'O'
        self.human_val = 'X'

    def PrintBoard(self):
        print(self.board[0][0] + "|" + self.board[1][0] + "|" + self.board[2][0])

        print(self.board[0][1] + "|" + self.board[1][1] + "|" + self.board[2][1])

        print(self.board[0][2] + "|" + self.board[1][2] + "|" + self.board[2][2])

    def play_square(self, col, row, val):
        self.count += 1
        self.board[col][row] = val

    def get_square(self, col, row):
        return self.board[col][row]

    def full_board(self):
        for i in range(3):
            for j in range(3):
                if(self.board[i][j]=='N'):
                    return False

        return True

    #if there is a winner this will return their symbol (either 'X' or 'O'),
    #otherwise it will return 'N'
    def winner(self):
        #check the cols
        for col in range(3):
            if(self.board[col][0]!='N' and self.board[col][0] == self.board[col][1] and self.board[col][0]==self.board[col][2] ):
                return self.board[col][0]
        #check the rows
        for row in range(3):
            if(self.board[0][row]!='N' and self.board[0][row] == self.board[1][row] and self.board[0][row]==self.board[2][row] ):
                return self.board[0][row]
        #check diagonals
        if(self.board[0][0]!='N' and self.board[0][0] == self.board[1][1] and self.board[0][0]==self.board[2][2] ):
            return self.board[0][0]
        if(self.board[2][0]!='N' and self.board[2][0] == self.board[1][1] and self.board[2][0]==self.board[0][2]):
            return self.board[2][0]
        return 'N'


def make_simple_cpu_move(board, cpuval):
    for i in range(3):
        for j in range(3):
            if board.get_square(i, j) == 'N':
                board.play_square(i, j, cpuval)
                return True
    return False


# Given a non-empty board, it fills one square in the board, according to minimax strategy.
def minimax_dicision(board, cpuval):
    position = ()
    board.val = cpuval
    board.human_val = 'X' if cpuval == 'O' else 'O'
    max = None
    value = None

    for i in range(3):
        for j in range(3):
            if board.get_square(i, j) == 'N':

                board.play_square(i, j, board.human_val)         # If human is going to win, stop it to win.
                if board.winner() == board.human_val:
                    board.play_square(i, j, cpuval)
                    return

                board.play_square(i, j, cpuval)
                if board.full_board() or board.winner() != 'N':
                    result = utility(board, cpuval)
                    return result
                else:
                    value = min_value(board, board.human_val, value)
                    if max == None:
                        max = value
                        position = (i, j)
                    elif max < value:
                        max = value
                        position = (i, j)
                board.play_square(i, j, 'N')

    board.play_square(position[0], position[1], cpuval)

def utility(board, val):
    winner = board.winner()
    return 1 if winner == board.val else 0 if winner == 'N' else -1

def min_value(board, val, a):
    min = None
    value = None

    for i in range(3):
        for j in range(3):
            if (board.get_square(i, j) == 'N'):
                board.play_square(i, j, val)
                if board.full_board() or board.winner() != 'N':
                    result = utility(board, val)
                    board.play_square(i, j, 'N')
                    return result
                else:
                    value = max_value(board, board.val, value)
                    if a != None and value <= a:
                        board.play_square(i, j, 'N')
                        return a - 1
                    if min == None:
                        min = value
                    elif min > value:
                        min = value
                board.play_square(i, j, 'N')

    return min

def max_value(board, val, b):
    max = None
    value = None

    for i in range(3):
        for j in range(3):
            if (board.get_square(i, j) == 'N'):
                board.play_square(i, j, val)
                if board.full_board() or board.winner() != 'N':
                    result = utility(board, val)
                    board.play_square(i, j, 'N')
                    return result
                else:
                    value = min_value(board, board.human_val, value)
                    if b != None and value >= b:
                        board.play_square(i, j, 'N')
                        return b + 1
                    if max == None:
                        max = value
                    elif max < value:
                        max = value
                board.play_square(i, j, 'N')
    return max


def play():
    Board = TicTacToeBoard()
    humanval = 'X'
    cpuval = 'O'
    Board.PrintBoard()

    print "Type 1 -> X(first) 2 -> O(second) "
    choice = input()

    while choice not in [1,2]:
        print "Invalid input"
        print "Type 1 -> X(first) 2 -> O(second) "
        choice = input()

    if choice == 2:
        humanval = 'O'
        cpuval = 'X'
        print("\nCPU Move\n")
        minimax_dicision(Board, cpuval)
        Board.PrintBoard()

    while( Board.full_board()==False and Board.winner() == 'N'):
        print("your move, pick a row (0-2)")
        row = int(input())
        print("your move, pick a col (0-2)")
        col = int(input())

        if(Board.get_square(col,row)!='N'):
            print("square already taken!")
            continue
        else:
            Board.play_square(col,row,humanval)
            if(Board.full_board() or Board.winner()!='N'):
                break
            else:
                Board.PrintBoard()
                print("CPU Move")
                # make_simple_cpu_move(Board,cpuval)
                minimax_dicision(Board, cpuval)
                Board.PrintBoard()

    print '-' * 30
    print 'total move:' + str(Board.count)
    Board.PrintBoard()
    if(Board.winner()=='N'):
        print("Cat game")
    elif(Board.winner()==humanval):
        print("You Win!")
    elif(Board.winner()==cpuval):
        print("CPU Wins!")


def main():
    play()

main()

