import random


def find_random_move(availableMoves):
    move = availableMoves[random.randint(0,len(availableMoves)-1)]  # [['w'], 'C', '1', '0', 'DD']
    text = move[1:]
    text_move = ' '.join(text)
    return text_move
