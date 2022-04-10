from player import Human,Computer,GeniusComputer
import time
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)] #single list to reprsnt 3x3 board
        self.current_winner = None #if we have a winner. game over


    def display_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print(' '+' | '.join(row))

    @staticmethod
    def default_board():
        #tells us what index corresponds to which box
        for row in [[str(i) for i in range(j*3,(j+1)*3)] for j in range(3)]:
            print(' '+' | '.join(row))

    def available_moves(self):
        moves = []
        #returns the indexes of the spots available on chess board
        for i,spot in enumerate(self.board):
            if spot == ' ':
                moves.append(i)
        return moves

    def num_avail_moves(self):
        return self.board.count(' ')

    def winner(self,select_square,letter):
        #check in row
        row_ind = select_square//3
        row = self.board[row_ind*3:(row_ind+1)*3]
        if all([spot==letter for spot in row]):
            return True
        #check in column
        col_ind = select_square%3
        column = [self.board[col_ind+(i*3)] for i in range(3)]
        if all([spot==letter for spot in column]):
            return True
        #check in diagonal
        #if select_square is even, we need to check diagonals for win
        if select_square%2==0:
            diagonal1=[self.board[i] for i in [0,4,8]]
            if all([spot==letter for spot in diagonal1]):
                return True
            diagonal2=[self.board[i] for i in [2,4,6]]
            if all([spot==letter for spot in diagonal2]):
                return True
        #if all the conditions fail, there is no winner
        return False

    def game_empty(self):
        return ' ' in self.board

    def make_move(self,select_square,letter):
        #after getting the move from player we assign the move on the board
        if self.board[select_square] == ' ':
            self.board[select_square] = letter
            #if after making the move, we have winner, we assign the winner to letter
            if self.winner(select_square,letter):
                self.current_winner = letter
            return True #if move made return true, else return false
        return False


def play(game,o_player,x_player,print_game=True):
    '''return None if tie,else returns winner(letter) of game'''
    #print_game is where we wanna watch players playing, but if only computers are playing, we dont need to see all iterations and we can put that False
    if print_game:
        #we want to see which index reference board
        game.default_board()

    letter = 'x' #we want x to start the game always

    while game.game_empty():
        if letter == 'x':
            select_square = x_player.get_move(game)
        else:
            select_square = o_player.get_move(game)

        if game.make_move(select_square,letter):
            if print_game:
                print(letter + f' makes a move to square {select_square}')
                game.display_board()
                print() #to have empty line between moves
            #just after making move, we check if we have a winner
            if game.current_winner:
                if print_game:
                    print(letter , ' wins!')
                return letter
            #once move has been made, we will alternate players
            if letter == 'x':
                letter = 'o'
            else:
                letter = 'x'
        #add a pause for next player
        if print_game:
            time.sleep(0.8)

    if print_game:
        print('it\'s a tie!')


if __name__=='__main__':
    x_player = Human('x')
    o_player = Human('o')
    t =TicTacToe()
    play(t,o_player,x_player,print_game=True)
