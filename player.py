import random
import math

class Player:
    def __init__(self,letter):
        #letter is x or o
        self.letter=letter

    def get_move(self,game):
        #we want the Player to be able to get its next move in the game
        pass

#inheritance
class Human(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_select_square = False #setting a valid move to false and looping until its a correct value i.e. integer or its a available move
        val = None
        while not valid_select_square: #loopung until we get a valid available move from user
            select_square = input(self.letter + '\'s turn. input move [0-8]:' )
            try:
                select_square = int(select_square)
                if select_square not in game.available_moves():
                    raise ValueError #raising a ValueError if its not an available move
                valid_select_square = True
            except ValueError: #raising a ValueError if it is not an integer
                print('invalid move.pls try again.')
        return select_square

#inheritance
class Computer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        select_square = random.choice(game.available_moves())
        return select_square

class GeniusComputer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        if len(game.available_moves())==9:
            select_square = random.choice(game.available_moves())
        else:
            select_square = self.minimax(game,self.letter)['position']
        return select_square

    def minimax(self,state,player):
        max_player = self.letter
        other_player = 'o' if player=='x' else 'x'

        #base-case is having a winner in current state or draw when game ends
        if state.current_winner==other_player:
            if state.current_winner==max_player:
                return {'position':None,'score': 1*(1+state.num_avail_moves())}
            else:
                return {'position':None,'score': -1*(1+state.num_avail_moves())}
        elif state.num_avail_moves()==0:
            return {'position':None,'score':0}

        #initializing dictionary in case of max_player and min_player
        if player==max_player:
            best = {'position':None,'score':-math.inf} #we want to increment the value for max_player so we take lowest possible value for score
        else:
            best = {'position':None,'score':math.inf}#we want to increment the value for min_player so we take highest possible value for score

        for possible_move in state.available_moves():
            #we make a move from the first possible move
            state.make_move(possible_move,player)
            #we recursively apply function by alternating players

            simulation_score = self.minimax(state,other_player) #we simulate by alternating players
            #we undo the move so that we can check for next possible movesprint('hey')

            state.board[possible_move] = ' '
            state.current_winner = None
            simulation_score['position'] = possible_move
            #print(simulation_score)
            #we store the result in dictionary if we get a better result
            if player == max_player:
                if simulation_score['score']>best['score']:
                    best = simulation_score #we have successfuly got a better move for max_player

            else:
                if simulation_score['score']<best['score']:
                    best= simulation_score #we have successfuly got a better move for min_player

        return best
