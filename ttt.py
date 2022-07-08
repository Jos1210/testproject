def movement(board, n):
    inf = True  # Conditioner
    print(n)
    while inf:
        # Coordinates
        coor = input('Type the coordinates to use: ')
        coor = coor.strip()
        coor = coor.split()
        # Exceptions
        try:
            row = int(coor[0]) - 1
            column = int(coor[1]) - 1
        except ValueError:
            print("You should enter numbers!")

        else:
            if (row or column) > 2 or (row or column) < 0:
                print('Coordinates should be from 1 to 3!')

            elif board[row][column] == 'X' or board[row][column] == 'O':
                print('This cell is occupied! Choose another one!')

            else:
                if n % 2 == 0 or n == 0:
                    board[row][column] = 'X'
                else:
                    board[row][column] = 'O'
                return board


def table(game_table):
    print("----------")
    print("|" + ' ' + game_table[0][0] + ' ' + game_table[0][1] + ' ' + game_table[0][2] + ' ' + "|")
    print("|" + ' ' + game_table[1][0] + ' ' + game_table[1][1] + ' ' + game_table[1][2] + ' ' + "|")
    print("|" + ' ' + game_table[2][0] + ' ' + game_table[2][1] + ' ' + game_table[2][2] + ' ' + "|")
    print("----------")
    pass


def main():
    # Printing the board
    game = "_________"
    game = game.upper()
    game = [[game[0], game[1], game[2]], [game[3], game[4], game[5]], [game[6], game[7], game[8]]]
    table(game)
    # User input
    n_turns = 0  # It should be up to 8
    win = 0  # Win counter
    while n_turns < 9:
        game = movement(game, n_turns)
        table(game)
        n_turns += 1
        for i in range(3):
            if game[i][0] == game[i][1] and game[i][1] == game[i][2] and game[i][0] == game[i][2] and \
                    game[i][0] != "_":
                win += 1
                winner = str(game[i][0])
                n_turns = 9
            elif game[0][i] == game[1][i] and game[1][i] == game[2][i] and game[0][i] == game[2][i] and \
                    game[0][i] != "_":
                win += 1
                winner = str(game[0][i])
                n_turns = 9

        if game[0][0] == game[1][1] and game[1][1] == game[2][2] and game[0][0] == game[2][2] and \
                game[1][1] != "_":
            win += 1
            winner = str(game[0][0])
            n_turns = 9

        elif game[0][2] == game[1][1] and game[1][1] == game[2][0] and game[0][2] == game[2][0] and \
                game[1][1] != "_":
            win += 1
            winner = str(game[0][2])
            n_turns = 9
        else:
            continue

    # Conditions for winner display
    if win == 0:
        winner = 'Draw'
        print(winner)
    elif win == 1:
        print(winner, 'wins')


if __name__ == '__main__':
    main()