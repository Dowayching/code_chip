import os

# %%
def clear_screen():
    '''Clear the screen by os
    '''
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')
    # for linux & mac (os.name is 'posix')
    else:
        _ = os.system('clear')


# %%
def display_board(user_inputs):
    '''
    '''
    v = '   |   |   '       # vertical
    vi = ' {} | {} | {} '   # vertical with input
    h = '--- --- ---'       # horizental
    draw_figure = [v, vi, v, h, v, vi, v, h, v, vi, v]

    clear_screen()
    print('Current board:  ')
    for idx, draw_line in enumerate(draw_figure):
        if idx == 1 or idx == 5 or idx == 9:
            # change index from board index to user_input index
            # board   user_input
            #   1          6
            #   5          3
            #   9          0
            i = int((2 - (idx - 1) / 4) * 3)
            print(draw_line.format(user_inputs[i], user_inputs[i + 1], 
                                   user_inputs[i + 2])) 
        else:
            print(draw_line)

#user_input = ['O', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
#display_board(user_input)


# %%
def get_user_choice(player):
    '''
    '''
    user_choice = 0
    while True:
        choice = input('Player {}, input your choice(1~9):'.format(player)) 

        # check if input is digit and in the range of 1~9 
        if choice.isdigit() == False:
            print('Your input is not digit!')
            continue
        user_choice = int(choice)
        if user_choice not in range(1, 10):
            print('Your input {} is not in 1~9'.format(choice))
        else:
            break

    return user_choice
#get_user_choice(1)


# %%
def update_user_inputs(user_inputs, player, user_choice):
    '''
    '''
    user_inputs[user_choice - 1] = 'O' if player == 1 else 'X'
    return user_inputs

# %%
def get_user_gameon():
    '''
    '''
    is_gameon = False
    while True:
        gameon = input('Do you wa`nt to play again (Y or N):')

        # check if input is correct 
        gameon.lower()
        if gameon not in ['y', 'n']:
            print('Your input is not correct (only Y, y, N, n)!')
            continue
        else:
            is_gameon = (gameon == 'y')
            break

    return is_gameon 
#get_user_gameon()


# %%
def check_if_game_end(inputs):
    '''
    '''
    # check if somebody win
    chk_list = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
    for group in chk_list:
        if inputs[group[0]] != ' ' and \
           inputs[group[0]] == inputs[group[1]] == inputs[group[2]]:
            return True, True

    # check if the game is end but nobody win
    if ' ' not in inputs:
        return True, False

    return False, False


# %%
def main():
    
    #user_input = ['O', 'X', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    player = 1
    user_inputs = [' '] * 9

    while True:
        # display current board information 
        display_board(user_inputs)

        # print prompt, get input, & check input
        user_choice = get_user_choice(player)

        # update input & update display
        user_inputs = update_user_inputs(user_inputs, player, user_choice)
        display_board(user_inputs)

        # check if somebody is win
        is_game_end, is_win = check_if_game_end(user_inputs)
        if is_game_end:
            if is_win:
                print('Player {} is WIN !!'.format(player))
            else:
                print('No one has win !')

            # start
            if get_user_gameon() == True:
                print('New Game')
            else:
                print('Bye Bye ! See you next time')
                break

        # update Player
        player = 2 if player == 1 else 1


if __name__ == "__main__":
    main()    






# %%
