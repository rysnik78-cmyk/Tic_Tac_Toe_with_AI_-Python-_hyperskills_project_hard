# write your code here
import random
import string














def computer_moves(actual_grid_string, who_moves_x_or_o):
    while True:
        index_to_change = random.randint(0, 8)
        if actual_grid_string[index_to_change] == '_':
            break
    print(index_to_change)
    return actual_grid_string[:index_to_change] + who_moves_x_or_o + actual_grid_string[index_to_change + 1:]


class Grid:
    def __init__(self, grid_string):
        self.actual_grid_string = grid_string

    def print_grid(self):
        grid_string = self.actual_grid_string.replace('_', ' ')
        print('---------')
        for row in range(3):
            line = '|'
            for column in range(3):
                line += f' {grid_string[row * 3 + column]}'
            line += ' |'
            print(line)
        print('---------')

class Game():
    def __init__(self, game_parameters, grid_string):
        self.game_parameters = game_parameters
        self.who_moves_x_or_o = 'X'
        self.actual_grid_string = grid_string
        self.grid_for_this_game = Grid(self.actual_grid_string)
        self.game_loop()

    def three_in_row(self, grid_string, char):
        tir_patterns = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
        tir_number = 0
        for pattern in tir_patterns:
            # print(pattern)
            for index in range(3):

                if grid_string[pattern[index]] != char:
                    break
                if index == 2:
                    tir_number += 1
        return tir_number

    def analyze_game_state(self, grid_string):
        number_of_x = grid_string.count('X')
        number_of_y = grid_string.count('O')
        empty_cell_number = 9 - number_of_x - number_of_y

        three_x = self.three_in_row(grid_string, 'X')
        three_o = self.three_in_row(grid_string, 'O')

        if abs(number_of_x - number_of_y) > 1 or three_x == three_o == 1:
            return 'Impossible'
        if three_x == three_o == 0 and empty_cell_number > 0:
            return 'Game not finished'
        if three_x == three_o == 0 and empty_cell_number == 0:
            return 'Draw'
        if three_x == 1:
            return 'X wins'
        if three_o == 1:
            return 'O wins'
        return '?'

    def index_from_coordinates(self,user_move_input):
        coordinates = user_move_input.split(' ')
        column = int(coordinates[1])
        row = int(coordinates[0])
        index_to_change = (row - 1) * 3 + (column - 1)
        return index_to_change

    def update_grid_string(self, grid_string, user_move_input, who_moves_x_or_o):
        index_to_change = self.index_from_coordinates(user_move_input)
        new_grid_string = grid_string[:index_to_change] + who_moves_x_or_o + grid_string[index_to_change + 1:]
        # print(updated_string)
        return new_grid_string

    def verify(self, actual_grid, user_move):
        for part in user_move.split(' '):
            if part not in string.digits:
                return 'You should enter numbers!'
            elif int(part) > 3 or int(part) < 1:
                return 'Coordinates should be from 1 to 3!'
        if actual_grid[self.index_from_coordinates(user_move)] != '_':
            return 'This cell is occupied! Choose another one!'

        return 'valid'

    def next_move(self):
        if self.who_moves_x_or_o == 'X':
            self.who_moves_x_or_o = 'O'
        else:
            self.who_moves_x_or_o = 'X'


    def game_loop(self):
        self.grid_for_this_game.print_grid()
        while True:
            # if user moves
            if self.game_parameters[self.who_moves_x_or_o] == 'user':
                while True:
                    user_move_input = input('Enter the coordinates: ')
                    verification_status = self.verify(self.actual_grid_string, user_move_input)
                    if verification_status == 'valid':

                        self.actual_grid_string = self.update_grid_string(self.actual_grid_string, user_move_input, self.who_moves_x_or_o)

                        break
                    else:
                        print(verification_status)
                        continue

            elif self.game_parameters[self.who_moves_x_or_o] == 'easy':
                print('Making move level "easy"')
                self.actual_grid_string = computer_moves(self.actual_grid_string, self.who_moves_x_or_o)


            # print(actual_grid_string)
            self.grid_for_this_game.actual_grid_string = self.actual_grid_string
            self.grid_for_this_game.print_grid()
            game_state = self.analyze_game_state(self.actual_grid_string)
            self.next_move()
            if game_state != 'Game not finished':
                print(game_state)
                break
            # print(game_state)
            # break


def main():
    while True:
        right_commands = ['user', 'easy']
        game_parameters = {'X': None, 'O': None}
        while True:
            command = input('Input command: ').lower()
            if command == 'exit':
                break
            command_split = command.split()
            if len(command_split) == 3 and command_split[0] == 'start':
                if command_split[1] in right_commands:
                    game_parameters['X'] = command_split[1]
                if command_split[2] in right_commands:
                    game_parameters['O'] = command_split[2]
                if game_parameters['X'] and game_parameters['O']:
                    my_game = Game(game_parameters, '_________')
                    continue
            print('Bad parameters!')
            continue
        if command == 'exit':
            break


if __name__ == '__main__':
    main()
