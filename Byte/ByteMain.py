import time

import pygame as p
import sys
from Byte import ByteEngine
import ByteAI
from tkinter import simpledialog
from tkinter import messagebox
from easygui import *

SQ_SIZE = 50
MAX_FPS = 15
IMAGES = {}


def load_images(dimension):
    sq_size = 50

    pieces = ["w", "b", "wb", "bw", "bb", "ww", "www", "wwb", "wbw", "wbb", "bww", "bwb", "bbw", "bbb", "wwww", "wwwb",
              "wwbw", "wwbb", "wbww", "wbwb", "wbbw", "wbbb", "bwww", "bwwb", "bwbw", "bwbb", "bbww", "bbwb", "bbbw",
              "bbbb", "wwwww", "wwwwb", "wwwbw", "wwwbb", "wwbww", "wwbwb", "wwbbw", "wwbbb", "wbwww", "wbwwb", "wbwbw",
              "wbwbb", "wbbww", "wbbwb", "wbbbw", "wbbbb", "bwwww", "bwwwb", "bwwbw", "bwwbb", "bwbww", "bwbwb",
              "bwbbw", "bwbbb", "bbwww", "bbwwb", "bbwbw", "bbwbb", "bbbww", "bbbwb", "bbbbw", "bbbbb", "wwwwww",
              "wwwwwb", "wwwwbw", "wwwwbb", "wwwbww", "wwwbwb", "wwwbbw", "wwwbbb", "wwbwww", "wwbwwb", "wwbwbw",
              "wwbwbb", "wwbbww", "wwbbwb", "wwbbbw", "wwbbbb", "wbwwww", "wbwwwb", "wbwwbw", "wbwwbb", "wbwbww",
              "wbwbwb", "wbwbbw", "wbwbbb", "wbbwww", "wbbwwb", "wbbwbw", "wbbwbb", "wbbbww", "wbbbwb", "wbbbbw",
              "wbbbbb", "bwwwww", "bwwwwb", "bwwwbw", "bwwwbb", "bwwbww", "bwwbwb", "bwwbbw", "bwwbbb", "bwbwww",
              "bwbwwb", "bwbwbw", "bwbwbb", "bwbbww", "bwbbwb", "bwbbbw", "bwbbbb", "bbwwww", "bbwwwb", "bbwwbw",
              "bbwwbb", "bbwbww", "bbwbwb", "bbwbbw", "bbwbbb", "bbbwww", "bbbwwb", "bbbwbw", "bbbwbb", "bbbbww",
              "bbbbwb", "bbbbbw", "bbbbbb", "wwwwwww", "wwwwwwb", "wwwwwbw", "wwwwwbb", "wwwwbww", "wwwwbwb", "wwwwbbw",
              "wwwwbbb", "wwwbwww", "wwwbwwb", "wwwbwbw", "wwwbwbb", "wwwbbww", "wwwbbwb", "wwwbbbw", "wwwbbbb",
              "wwbwwww", "wwbwwwb", "wwbwwbw", "wwbwwbb", "wwbwbww", "wwbwbwb", "wwbwbbw", "wwbwbbb", "wwbbwww",
              "wwbbwwb", "wwbbwbw", "wwbbwbb", "wwbbbww", "wwbbbwb", "wwbbbbw", "wwbbbbb", "wbwwwww", "wbwwwwb",
              "wbwwwbw", "wbwwwbb", "wbwwbww", "wbwwbwb", "wbwwbbw", "wbwwbbb", "wbwbwww", "wbwbwwb", "wbwbwbw",
              "wbwbwbb", "wbwbbww", "wbwbbwb", "wbwbbbw", "wbwbbbb", "wbbwwww", "wbbwwwb", "wbbwwbw", "wbbwwbb",
              "wbbwbww", "wbbwbwb", "wbbwbbw", "wbbwbbb", "wbbbwww", "wbbbwwb", "wbbbwbw", "wbbbwbb", "wbbbbww",
              "wbbbbwb", "wbbbbbw", "wbbbbbb", "bwwwwww", "bwwwwwb", "bwwwwbw", "bwwwwbb", "bwwwbww", "bwwwbwb",
              "bwwwbbw", "bwwwbbb", "bwwbwww", "bwwbwwb", "bwwbwbw", "bwwbwbb", "bwwbbww", "bwwbbwb", "bwwbbbw",
              "bwwbbbb", "bwbwwww", "bwbwwwb", "bwbwwbw", "bwbwwbb", "bwbwbww", "bwbwbwb", "bwbwbbw", "bwbwbbb",
              "bwbbwww", "bwbbwwb", "bwbbwbw", "bwbbwbb", "bwbbbww", "bwbbbwb", "bwbbbbw", "bwbbbbb", "bbwwwww",
              "bbwwwwb", "bbwwwbw", "bbwwwbb", "bbwwbww", "bbwwbwb", "bbwwbbw", "bbwwbbb", "bbwbwww", "bbwbwwb",
              "bbwbwbw", "bbwbwbb", "bbwbbww", "bbwbbwb", "bbwbbbw", "bbwbbbb", "bbbwwww", "bbbwwwb", "bbbwwbw",
              "bbbwwbb", "bbbwbww", "bbbwbwb", "bbbwbbw", "bbbwbbb", "bbbbwww", "bbbbwwb", "bbbbwbw", "bbbbwbb",
              "bbbbbww", "bbbbbwb", "bbbbbbw", "bbbbbbb"]
    print(len(pieces))
    for piece in pieces:
        IMAGES[piece] = p.transform.scale(p.image.load("images/" + piece + ".png"), (sq_size, sq_size))


def input_game_mode():
    text = "Izaberite mod igre"

    # window title
    title = "Opcije"

    # item choices
    choices = ["Covek_vs_kompjuter", "Covek_vs_covek"]

    # creating a button box
    output = choicebox(text, title, choices)

    # GAME_MODE = output
    return output


def input_board_first_player(gs):
    dialog = messagebox.askyesno("Opcije", "Da li zelite da igrate prvi?")
    if dialog:
        gs.computerToPlay = False
    else:
        gs.computerToPlay = True


def input_board_dimension():
    dimension = simpledialog.askinteger("Opcije", "Unesite dimenziju table")
    dimension_status = check_dimension_input(dimension)
    if dimension_status:
        return dimension
    else:
        return input_board_dimension()


def draw_game_state(screen, gs, dimension):
    draw_board(screen, dimension)
    draw_pieces(screen, gs.board, dimension)


def check_dimension_input(dimension):
    if dimension == 0:
        messagebox.showerror("Uneta dimenzija nije validna!")
        return False
    if dimension % 2 != 0 or ((dimension * dimension - dimension * 2) // 2) % 8 != 0 or dimension > 16:
        messagebox.showerror("Uneta dimenzija nije validna!")
        return False
    else:
        return True


def draw_board(screen, dimension):
    colors = [p.Color(117, 117, 117), p.Color(243, 227, 203)]
    border_color = p.Color("White")
    border_width = 256
    border_line_width = 2
    height = SQ_SIZE * dimension
    width = SQ_SIZE * dimension + 256
    p.draw.rect(screen, border_color, p.Rect(SQ_SIZE * dimension, 0, SQ_SIZE * dimension + 256, height), border_width)
    p.draw.line(screen, p.Color("Black"), [SQ_SIZE * dimension, 0], [SQ_SIZE * dimension, height], border_line_width)

    for r in range(dimension):
        for c in range(dimension):
            color = colors[((r + c) % 2)]
            p.draw.rect(screen, color, p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))
    p.draw.line(screen, p.Color("Black"), [0, 0], [0, height], border_line_width)
    p.draw.line(screen, p.Color("Black"), [0, 0], [SQ_SIZE * dimension, 0], border_line_width)
    p.draw.line(screen, p.Color("Black"), [0, height], [SQ_SIZE * dimension, height], border_line_width)
    potez = p.TEXTINPUT


def draw_pieces(screen, board, dimension):
    for r in range(dimension):
        for c in range(dimension):
            piece = board[r][c]
            if piece != "-":
                screen.blit(IMAGES[piece], p.Rect(c * SQ_SIZE, r * SQ_SIZE, SQ_SIZE, SQ_SIZE))


def check_move(gs, board, input_text, dimension, color):
    if color == 'b' and not gs.BlackPlayerToPlay:
        return False
    if color == 'w' and gs.BlackPlayerToPlay:
        return False

    splited_text = input_text.split()
    if len(splited_text)!=4:
        return False
    # Inputs from user
    piece_current_column = splited_text[0]
    piece_current_row = splited_text[1]
    piece_stack_index = splited_text[2]
    piece_movement_way = splited_text[3]

    piece_current_column = map_alphanumerical_to_numerical(piece_current_column)
    if piece_current_column > dimension - 1 or piece_current_column < 0:
        return False

    piece_current_row = int(piece_current_row) - 1
    if piece_current_row > dimension - 1 or piece_current_row < 0:
        return False

    # piece_movement_way.upper()
    if piece_movement_way.upper() not in ['DD', 'DL', 'GD', 'GL']:
        return False

    piece = board[piece_current_column][piece_current_row]
    if piece == '-':
        return False
    if int(piece_stack_index) > len(piece) - 1:
        return False

    if piece_movement_way.upper() == 'GD':
        if piece_current_column - 1 not in range(0, dimension) or piece_current_row + 1 not in range(0, dimension):
            return False
        if (len(board[piece_current_column - 1][piece_current_row + 1]) + len(
                piece[int(piece_stack_index):])) > 8:
            return False
    elif piece_movement_way.upper() == 'GL':
        if piece_current_column - 1 not in range(0, dimension) or piece_current_row - 1 not in range(0, dimension):
            return False
        if (len(board[piece_current_column - 1][piece_current_row - 1]) + len(piece[int(piece_stack_index):])) > 8:
            return False
    elif piece_movement_way.upper() == 'DL':

        if piece_current_column + 1 not in range(0, dimension) or piece_current_row - 1 not in range(0,
                                                                                                     dimension):  # KAKO MOZE FALSE ZA B 8 0 DL ,PCCC=2,PCCR-6?????????????
            return False
        if (len(board[piece_current_column + 1][piece_current_row - 1]) + len(piece[int(piece_stack_index):])) > 8:
            return False
    elif piece_movement_way.upper() == 'DD':
        if piece_current_column + 1 not in range(0, dimension) or piece_current_row + 1 not in range(0, dimension):
            return False
        if (len(board[piece_current_column + 1][piece_current_row + 1]) + len(piece[int(piece_stack_index):])) > 8:
            return False
    else:
        print("Nepoznat input")

    if piece[int(piece_stack_index)] != color:  # ako figura nije prave boje
        return False

    if not check_valid_move(gs, piece_current_column, piece_current_row, piece_stack_index, piece_movement_way):
        return False

    if not check_stack_valid_height(gs, piece_current_column, piece_current_row, piece_stack_index, piece_movement_way):
        return False

    return True


def play_move(gs, dimension, input_text, color):
    splited_text = input_text.split()

    # Inputs from user
    piece_current_column = splited_text[0]
    piece_current_row = splited_text[1]
    piece_stack_index = splited_text[2]
    piece_movement_way = splited_text[3]

    piece_current_column = map_alphanumerical_to_numerical(piece_current_column)
    piece_current_row = int(piece_current_row) - 1
    piece_movement_way.upper()

    piece = gs.board[piece_current_column][piece_current_row]

    if piece_movement_way.upper() == 'GD':
        gs.board[piece_current_column - 1][piece_current_row + 1] += piece[int(piece_stack_index):]
        gs.board[piece_current_column][piece_current_row] = piece[:int(piece_stack_index)] + ""
        if gs.board[piece_current_column][piece_current_row] == "":
            gs.board[piece_current_column][piece_current_row] = "-"

        if len(gs.board[piece_current_column - 1][
                   piece_current_row + 1]) == 8:  # TODO: funkccija add_stack_to_player da se sredi
            # TODO: preterano ponavljanje koda
            curr = gs.board[piece_current_column - 1][piece_current_row + 1]
            if curr[-1] == 'b':
                gs.BlackPlayerStacks += 1
            elif curr[-1] == 'w':
                gs.WhitePlayerStacks += 1
            gs.board[piece_current_column - 1][piece_current_row + 1] = '-'
        else:
            if '-' in gs.board[piece_current_column - 1][piece_current_row + 1]:
                gs.board[piece_current_column - 1][piece_current_row + 1] = gs.board[piece_current_column - 1][
                    piece_current_row + 1].replace('-', '')

    elif piece_movement_way.upper() == 'GL':
        gs.board[piece_current_column - 1][piece_current_row - 1] += piece[int(piece_stack_index):]
        gs.board[piece_current_column][piece_current_row] = piece[:int(piece_stack_index)] + ""
        if gs.board[piece_current_column][piece_current_row] == "":
            gs.board[piece_current_column][piece_current_row] = "-"
        if len(gs.board[piece_current_column - 1][piece_current_row - 1]) == 8:
            curr = gs.board[piece_current_column - 1][piece_current_row - 1]
            if curr[-1] == 'b':
                gs.BlackPlayerStacks += 1
            elif curr[-1] == 'w':
                gs.WhitePlayerStacks += 1
            gs.board[piece_current_column - 1][piece_current_row - 1] = '-'
        else:
            if '-' in gs.board[piece_current_column - 1][piece_current_row - 1]:
                gs.board[piece_current_column - 1][piece_current_row - 1] = gs.board[piece_current_column - 1][
                    piece_current_row - 1].replace('-', '')

    elif piece_movement_way.upper() == 'DL':
        gs.board[piece_current_column + 1][piece_current_row - 1] += piece[int(piece_stack_index):]
        gs.board[piece_current_column][piece_current_row] = piece[:int(piece_stack_index)] + ""
        if gs.board[piece_current_column][piece_current_row] == "":
            gs.board[piece_current_column][piece_current_row] = "-"
        if len(gs.board[piece_current_column + 1][piece_current_row - 1]) == 8:
            curr = gs.board[piece_current_column + 1][piece_current_row - 1]
            if curr[-1] == 'b':
                gs.BlackPlayerStacks += 1
            elif curr[-1] == 'w':
                gs.WhitePlayerStacks += 1
            gs.board[piece_current_column + 1][piece_current_row - 1] = '-'
        else:
            if '-' in gs.board[piece_current_column + 1][piece_current_row - 1]:
                gs.board[piece_current_column + 1][piece_current_row - 1] = gs.board[piece_current_column + 1][
                    piece_current_row - 1].replace('-', '')


    elif piece_movement_way.upper() == 'DD':
        gs.board[piece_current_column + 1][piece_current_row + 1] += piece[int(piece_stack_index):]
        gs.board[piece_current_column][piece_current_row] = piece[:int(piece_stack_index)] + ""
        if gs.board[piece_current_column][piece_current_row] == "":
            gs.board[piece_current_column][piece_current_row] = "-"
        if len(gs.board[piece_current_column + 1][piece_current_row + 1]) == 8:
            curr = gs.board[piece_current_column + 1][piece_current_row + 1]
            if curr[-1] == 'b':
                gs.BlackPlayerStacks += 1
            elif curr[-1] == 'w':
                gs.WhitePlayerStacks += 1
            gs.board[piece_current_column + 1][piece_current_row + 1] = '-'
        else:
            if '-' in gs.board[piece_current_column + 1][piece_current_row + 1]:
                gs.board[piece_current_column + 1][piece_current_row + 1] = gs.board[piece_current_column + 1][
                    piece_current_row + 1].replace('-', '')

    else:
        print("Nepoznat input")

    gs.BlackPlayerToPlay = not gs.BlackPlayerToPlay
    gs.computerToPlay = not gs.computerToPlay
    gs.AvailableMoves = check_available_moves(gs , color)
    print(' ')
    print('Black Player To Play: ' + str(gs.BlackPlayerToPlay))
    print('Computer To Play: ' + str(gs.computerToPlay))
    print('Available Moves:' + str(gs.AvailableMoves))
def check_game_status_ongoing(gs):
    dim = gs.dimension
    total_stacks = ((dim * dim - dim * 2) // 2) // 8
    if gs.BlackPlayerStacks > (total_stacks / 2):
        return False
    if gs.WhitePlayerStacks > (total_stacks / 2):
        return False
    return True


def computer_make_move(gs,color):
    move = ByteAI.find_random_move(gs.AvailableMoves)
    print(' ')
    play_move(gs,gs.dimension,move,color)



def check_who_won(gs):
    if gs.BlackPlayerStacks > gs.WhitePlayerStacks:
        return 'Igrac sa crnim figurama je pobedio'
    else:
        return 'Igrac sa belim figurama je pobedio'


def reset_board(gs):
    gs.board = []

    empty_row = ['-'] * gs.dimension
    empty_row2 = ['-'] * gs.dimension
    gs.board.append(empty_row)

    for i in range(1, gs.dimension - 1):
        red = []
        if i % 2 != 0:
            for j in range(gs.dimension):
                if j % 2 == 0:
                    red.append('-')
                else:
                    red.append('b')
        else:
            for j in range(gs.dimension):
                if j % 2 == 0:
                    red.append('w')
                else:
                    red.append('-')

        gs.board.append(red)
    gs.board.append(empty_row2)
    gs.WhitePlayerStacks = 0
    gs.BlackPlayerStacks = 0
    gs.moveLog = []


def draw_letters_and_numbers(base_font, screen, dimension):
    for i in range(0, dimension):
        letter = chr(ord('A') + i)
        letter_draw = base_font.render(letter, True, (0, 0, 0))
        screen.blit(letter_draw, (SQ_SIZE * dimension + 5, i * SQ_SIZE + 17))
    for i in range(0, dimension):
        number = str(i + 1)
        number_draw = base_font.render(number, True, (0, 0, 0))
        screen.blit(number_draw, (i * SQ_SIZE + 17, dimension * SQ_SIZE + 5))


def check_valid_move(gs, column, row, index, move):
    if not has_neighbour(gs, column, row):
        if no_piece_has_neighbour(gs, column, row):
            if check_shortest_path(gs, column, row, move) == True:
                return True
    else:
        if move.upper() == 'GD':
            if column == 0 or row == gs.dimension - 1 or gs.board[column - 1][row + 1] == '-':
                return False
        elif move.upper() == 'GL':
            if column == 0 or row == 0 or gs.board[column - 1][row - 1] == '-':
                return False
        elif move.upper() == 'DL':
            if column == gs.dimension - 1 or row == 0 or gs.board[column + 1][row - 1] == '-':
                return False
        elif move.upper() == 'DD':
            if column == gs.dimension - 1 or row == gs.dimension - 1 or gs.board[column + 1][row + 1] == '-':
                return False
        return True


def check_shortest_path(gs, column, row, move):
    if gs.BlackPlayerToPlay:
        color = 'b'
    else:
        color = 'w'
    end_position = find_nearest_piece(gs, column, row)

    if end_position is None:
        return False
    return check_shortest_path_helper(gs, column, row, end_position, move)


def check_shortest_path_helper(gs, column, row, end_pos, move):
    start_col = column
    start_row = row
    end_col, end_row = end_pos

    target_distance = abs(end_col - start_col) + abs(end_row - start_row)

    new_col, new_row = start_col, start_row
    if move.upper() == "GL":
        new_col -= 1
        new_row -= 1
    elif move.upper() == "GD":
        new_col -= 1
        new_row += 1
    elif move.upper() == "DL":
        new_col += 1
        new_row -= 1
    elif move.upper() == "DD":
        new_col += 1
        new_row += 1

    if 0 <= new_col < len(gs.board[0]) and 0 <= new_row < len(gs.board):
        # Calculate the Manhattan distance for the new position
        move_distance = abs(end_col - new_col) + abs(end_row - new_row)

        # Check if the move is on the shortest path
        return move_distance == target_distance


def no_piece_has_neighbour(gs, column, row):
    no_piece_has_neighbour = True
    if gs.BlackPlayerToPlay:
        color = 'b'
    else:
        color = 'w'
    for c in range(gs.dimension):
        for r in range(gs.dimension):
            # piece = gs.board[r][c]
            if color in gs.board[c][r]:
                if has_neighbour(gs, c, r) == True:
                    no_piece_has_neighbour = False
                    break
        if not no_piece_has_neighbour:
            break

    return no_piece_has_neighbour


def check_stack_valid_height(gs, column, row, index, move):
    if move.upper() == 'GD':
        if int(index) + 1 >= len(gs.board[column - 1][row + 1]) + 1:
            return False
    elif move.upper() == 'GL':
        if int(index) + 1 >= len(gs.board[column - 1][row - 1]) + 1:
            return False
    elif move.upper() == 'DL':
        if int(index) + 1 >= len(gs.board[column + 1][row - 1]) + 1:
            return False
    elif move.upper() == 'DD':
        if int(index) + 1 >= len(gs.board[column + 1][row + 1]) + 1:
            return False
    return True


def has_neighbour(gs, column, row):
    if column == 0:
        if gs.board[column + 1][row - 1] != '-' or gs.board[column + 1][row + 1] != '-':
            return True
        else:
            return False
    if row == 0:
        if gs.board[column - 1][row + 1] != '-' or gs.board[column + 1][row + 1] != '-':
            return True
        else:
            return False
    if column == 7:
        if gs.board[column - 1][row - 1] != '-' or gs.board[column - 1][row + 1] != '-':
            return True
        else:
            return False
    if row == 7:
        if gs.board[column - 1][row - 1] != '-' or gs.board[column + 1][row - 1] != '-':
            return True
        else:
            return False

    if gs.board[column - 1][row - 1] != '-' or gs.board[column - 1][row + 1] != '-' or gs.board[column + 1][
        row - 1] != '-' or gs.board[column + 1][row + 1] != '-':
        return True
    else:
        return False


def find_nearest_piece(gs, column, row):
    if gs.BlackPlayerToPlay:
        color = 'b'
    else:
        color = 'w'
    min_distance = float('inf')
    nearest_piece_pos = None

    for r in range(len(gs.board)):
        for c in range(len(gs.board[0])):
            if gs.board[r][c] != '-':
                distance = abs(column - c) + abs(row - r)
                if distance < min_distance and distance != 0:
                    min_distance = distance
                    nearest_piece_pos = (c, r)
    return nearest_piece_pos


def check_move_availability(gs, color):
    moves = []
    for c in range(len(gs.board)):
        for r in range(len(gs.board[0])):
            if gs.board[c][r] != '-':
                index = len(gs.board[c][r])
                for i in range(0, index):
                    piece = gs.board[c][r]
                    if piece[i] == color:
                        for m in ['DD', 'DL', 'GL', 'GD']:
                            if check_valid_move(gs, c, r, i, m) and check_stack_valid_height(gs, c, r, i, m):
                                column = map_numerical_to_alphanumerical(c)
                                row = r + 1
                                move = [[str(gs.board[c][r])], str(column), str(row), str(i), m]
                                moves.append(move)
    if not moves:
        return False
    else:
        gs.AvailableMoves = moves
        return True


def possible_game_states(gs):
    # new_gs = gs
    boards = []
    for move in gs.AvailableMoves:  # [['bbw',column,row,index,move]
        new_gs = ByteEngine.GameState(gs.dimension)
        new_gs = gs
        column = str(move[1])
        row = str(move[2])
        index = str(move[3])
        way = str(move[4])

        ulaz = column + ' ' + row + ' ' + index + ' ' + way

        color = move[0][int(index)]

        play_move(new_gs, new_gs.dimension, ulaz, color)

        boards.append(new_gs.board)

    gs.PossibleGameStates = boards
    return boards


def check_available_moves(gs, color):
    moves = []
    for c in range(len(gs.board)):
        for r in range(len(gs.board[0])):
            if gs.board[c][r] != '-':
                index = len(gs.board[c][r])
                for i in range(0, index):
                    piece = gs.board[c][r]
                    if piece[i] == color:
                        for m in ['DD', 'DL', 'GL', 'GD']:
                            if check_valid_move(gs, c, r, i, m) and check_stack_valid_height(gs, c, r, i, m):
                                column = map_numerical_to_alphanumerical(c)
                                row = r + 1
                                move = [[str(gs.board[c][r])], str(column), str(row), str(i), m]
                                moves.append(move)
    return moves

def main():
    p.init()

    dimension = input_board_dimension()

    height = SQ_SIZE + (SQ_SIZE * dimension)
    width = SQ_SIZE + (SQ_SIZE * dimension + 256)
    screen = p.display.set_mode((width, height))

    game_mode = input_game_mode()

    print(game_mode)

    clock = p.time.Clock()
    gs = ByteEngine.GameState(dimension)
    print(gs.board)

    if game_mode == "Covek_vs_kompjuter":
        input_board_first_player(gs)
        if gs.computerToPlay == False:
            player_piece_color = 'b'
        else:
            player_piece_color = 'w'
    else:
        player_piece_color = 'b'

    base_font = p.font.Font(None, 32)
    smaller_font = p.font.Font(None, 25)
    user_text = ''
    input_rect = p.Rect(SQ_SIZE * dimension + 78, SQ_SIZE, 0, 32)
    white_rect = p.Rect(SQ_SIZE * dimension + 28, 0, 256, 32)
    color_active = p.Color('lightskyblue3')
    color_passive = p.Color('lightgray')
    color_light_gray = p.Color('lightgray')
    color = color_passive
    black_player_to_move_text = "Black player to move:"
    white_player_to_move_text = "White player to move:"
    active = False

    score_rect_bp = p.Rect(SQ_SIZE * dimension + 103, SQ_SIZE * (dimension - 0.75), 50, 50)
    score_rect_wp = p.Rect(SQ_SIZE * dimension + 203, SQ_SIZE * (dimension - 0.75), 50, 50)

    color_score = p.Color('black')

    load_images(dimension)

    gs.board = [
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'b', '-', '-', '-', 'w'],
        ['b', '-', 'bw', '-', '-', '-', '-', '-'],
        ['-', '-', '-', 'b', '-', '-', '-', '-'],
        ['-', '-', 'b', '-', 'w', '-', '-', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-'],
        ['-', '-', '-', '-', 'w', '-', 'w', '-'],
        ['-', '-', '-', '-', '-', '-', '-', '-']
    ]

    # gs.board[2][2] = 'bwbwbwb'#radi lakseg testiranja, zavrsetka igre
    # gs.board[4][4] = 'bwbwbwb'
    # print(gs.board)

    p.draw.rect(screen, p.Color("White"),
                p.Rect(0, SQ_SIZE * dimension - 2, SQ_SIZE * dimension + SQ_SIZE + 256, SQ_SIZE))
    #check_move_availability(gs, player_piece_color)
    #print(gs.AvailableMoves)
    gs.AvailableMoves=check_available_moves(gs,player_piece_color)
    print(' ')
    print('Black Player To Play: ' + str(gs.BlackPlayerToPlay))
    print('Computer To Play: ' + str(gs.computerToPlay))
    print('Available Moves:' + str(gs.AvailableMoves))

    running = True
    while running:

        for e in p.event.get():
            if e.type == p.QUIT:
                running = False
            if e.type == p.QUIT:
                p.quit()
                sys.exit()
            if e.type == p.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(e.pos):
                    active = True
                else:
                    active = False
            if e.type == p.KEYDOWN:
                if e.key == p.K_BACKSPACE:
                    user_text = user_text[:-1]
                else:
                    if len(user_text) < 9:
                        user_text += e.unicode
            if e.type == p.KEYDOWN:
                if (e.key == p.K_KP_ENTER or e.key == p.K_RETURN) and gs.computerToPlay == False:
                    #gs.AvailableMoves = check_available_moves(gs,player_piece_color)
                    if check_move(gs, gs.board, user_text, dimension, player_piece_color):
                        play_move(gs, dimension, user_text, player_piece_color)
                        if gs.BlackPlayerToPlay:
                            player_piece_color = 'b'
                        if not gs.BlackPlayerToPlay:
                            player_piece_color = 'w'
                        if check_game_status_ongoing(gs) == False:
                            messagebox.showinfo("GAME OVER", check_who_won(gs))
                            play_again = messagebox.askyesno("Play again?", "Do you want to play again?")
                            if play_again:
                                reset_board(gs)
                                print(gs.board)
                        user_text = ''
                        if not gs.AvailableMoves:
                            gs.BlackPlayerToPlay = not gs.BlackPlayerToPlay
                            if gs.BlackPlayerToPlay:
                                player_piece_color = 'b'
                            if not gs.BlackPlayerToPlay:
                                player_piece_color = 'w'
                        # possible_game_states(gs)
                    else:
                        messagebox.showerror("Error", "Uneti potez nije validan!")
        if gs.computerToPlay == True:
            if not gs.AvailableMoves:
                gs.BlackPlayerToPlay = not gs.BlackPlayerToPlay
                if gs.BlackPlayerToPlay:
                    player_piece_color = 'b'
                if not gs.BlackPlayerToPlay:
                    player_piece_color = 'w'
            else:
                computer_make_move(gs,player_piece_color)

                if gs.BlackPlayerToPlay:
                    player_piece_color = 'b'
                if not gs.BlackPlayerToPlay:
                    player_piece_color = 'w'
        if active:
            color = color_active
        else:
            color = color_passive
        draw_game_state(screen, gs, dimension)

        # draws scoreboard

        p.draw.rect(screen, (204, 204, 204), score_rect_bp)
        text_bp = base_font.render("Black", True, (0, 0, 0))
        screen.blit(text_bp, (score_rect_bp.x - 5, score_rect_bp.y - 30))
        text_bp_stacks = base_font.render(str(gs.BlackPlayerStacks), True, (255, 255, 255))
        screen.blit(text_bp_stacks, (score_rect_bp.x + 20, score_rect_bp.y + 15))

        p.draw.rect(screen, (204, 204, 204), score_rect_wp)
        text_wp = base_font.render("White", True, (0, 0, 0))
        screen.blit(text_wp, (score_rect_wp.x - 5, score_rect_wp.y - 30))
        text_wp_stacks = base_font.render(str(gs.WhitePlayerStacks), True, (255, 255, 255))
        screen.blit(text_wp_stacks, (score_rect_wp.x + 20, score_rect_wp.y + 15))

        # draws text input
        p.draw.rect(screen, color, input_rect)
        text_surface = base_font.render(user_text, True, (255, 255, 255))
        screen.blit(text_surface, (input_rect.x + 5, input_rect.y + 5))
        input_rect.w = max(200, text_surface.get_width() + 10)
        # p.draw.rect(screen,(255,255,255),white_rect)
        if gs.BlackPlayerToPlay:
            text_to_play = smaller_font.render(black_player_to_move_text, True, (0, 0, 0))
        else:
            text_to_play = smaller_font.render(white_player_to_move_text, True, (0, 0, 0))
        screen.blit(text_to_play, (input_rect.x, input_rect.y - 30))

        draw_letters_and_numbers(base_font, screen, dimension)

        p.display.flip()
        clock.tick(MAX_FPS)



def map_alphanumerical_to_numerical(letter):
    capital_letter = letter.upper()

    if 'A' <= capital_letter <= 'O':
        return ord(capital_letter) - ord('A')
    else:
        return -1


def map_numerical_to_alphanumerical(number):
    if 0 <= number <= 15:
        return chr(ord('A') + number)
    else:
        return None  # Povratna vrednost None ukoliko je broj izvan očekivanog opsega


if __name__ == "__main__":
    main()
