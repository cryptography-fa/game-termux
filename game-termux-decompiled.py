# uncompyle6 version 3.3.4
# Python bytecode 3.7
# Decompiled from: Python 3.7.3 (default, Apr 24 2019, 11:21:56) 
# [Clang 8.0.2 (https://android.googlesource.com/toolchain/clang 40173bab62ec7462
import random, os
os.system('clear')

def get_map(num1, num2):
    result = []
    idx = 0
    try:
        for x in range(num1):
            for y in range(num2):
                result.insert(idx, (x, y))
                idx += 1

            idx += 1

    except:
        print('Value Must Number')

    return (
     result, num1, num2)


CELLS, valx, valy = get_map(10, 20)
type(CELLS)

def get_location():
    start = random.choice(CELLS)
    door = random.choice(CELLS)
    monster = random.choice(CELLS)
    if start == door or start == monster or monster == door:
        return get_location()
    else:
        return (
         start, door, monster)


def get_move(player):
    moves = [
     'S', 'K', 'A', 'B']
    x, y = player
    if x == 0:
        os.system('clear')
        moves.remove('A')
    if x == valx - 1:
        os.system('clear')
        moves.remove('B')
    if y == 0:
        os.system('clear')
        moves.remove('S')
    if y == valy - 1:
        os.system('clear')
        moves.remove('K')
    return moves


def player_move(player, move):
    x, y = player
    if move == 'S':
        y -= 1
    else:
        if move == 'K':
            y += 1
        else:
            if move == 'A':
                x -= 1
            else:
                if move == 'B':
                    x += 1
                return (
                 x, y)


def draw_map(player):
    for x in range(valy):
        if x == valy - 1:
            print(' __')
            break
        else:
            print(' __', end='')

    tile = '|{}'
    rightidx = []
    count, val = (0, 0)
    for x in range(valx):
        if val == 0:
            val += count + valy - 1
            rightidx.append(val)
        else:
            val += count + valy
            rightidx.append(val)

    for idx, cell in enumerate(CELLS):
        if idx not in rightidx:
            if cell == player:
                print((tile.format('👤')), end='')
            else:
                if cell == door:
                    print((tile.format('👾')), end='')
                else:
                    print((tile.format('__')), end='')
        elif cell == player:
            print(tile.format('👤|'))
        elif cell == door:
            print(tile.format('👾|'))
        else:
            print(tile.format('__|'))


player, door, monster = get_location()
os.system('clear')
while 1:
    moves = get_move(player)
    print('                   \x1b[31;1m[ 🎮\x1b[32;1mGame Termux🎮 \x1b[31;1m]')
    print('                   \x1b[39;1m[\x1b[32;1m√\x1b[39;1m]Author\x1b[31;1m:\x1b[34;1mMr.Tr3v!0n')
    print('                   \x1b[39;1m[\x1b[32;1m•\x1b[39;1m]\x1b[31;1mBlack Coder Crush')
    print('           \x1b[39;1m[\x1b[32;1m•\x1b[39;1m]  \x1b[32;1mKita Berada Di Room\x1b[31;1m:\x1b[36;1m{}\x1b[32;1m  \x1b[39;1m[\x1b[32;1m•\x1b[39;1m]\x1b[32;1m'.format(player))
    draw_map(player)
    print(' ')
    print('\x1b[39;1m[\x1b[32;1m√\x1b[39;1m]\x1b[32;1m Perintah Untuk Menjalankan\x1b[31;1m:'.format(moves))
    print('\x1b[39;1m[\x1b[32;1m•\x1b[39;1m]\x1b[32;1m S \x1b[31;1m(\x1b[39;1mKiri\x1b[31;1m) ')
    print('\x1b[39;1m[\x1b[32;1m•\x1b[39;1m]\x1b[32;1m K \x1b[31;1m(\x1b[39;1mKanan\x1b[31;1m) ')
    print('\x1b[39;1m[\x1b[32;1m•\x1b[39;1m]\x1b[32;1m A \x1b[31;1m(\x1b[39;1mAtas\x1b[31;1m) ')
    print('\x1b[39;1m[\x1b[32;1m•\x1b[39;1m]\x1b[32;1m B \x1b[31;1m(\x1b[39;1mBawah\x1b[31;1m)\n ')
    print('\x1b[39;1m[\x1b[32;1m00\x1b[39;1m]\x1b[31;1m Exit\n')
    move = input(' 🎮 ')
    move = move.upper()
    if move == '00':
        break
    if move in moves:
        os.system('clear')
        player = player_move(player, move)
    else:
        print("Don't try to walk in wall")
        continue
    if player == monster:
        print('\x1b[39;1m[\x1b[31;1m!\x1b[39;1m]\x1b[31;1m Kamu di Makan Monster')
        break
    elif player == door:
        print('\x1b[39;1m[\x1b[32;1m√\x1b[39;1m]\x1b[32;1m Selamat Anda Menang')
        break