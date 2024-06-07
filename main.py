
from myfuncfile import *
if __name__ == "__main__":

    print('Welcome to Tic Tac Toe!')
    #initiate the game
    while True:
        player1_mark, player2_mark = player_input()
        initboard = [' '] * 10
        display_board(initboard)
        turn = choose_first()
        print(turn + " will play first.")

        play_game='string'
        while play_game not in ['y','Y','n','N']:
            play_game = input('Are you ready to play? Enter Y/N.\n')
        if play_game.lower() == 'y':
            game_on = True
        else:
            game_on = False

    # game on
        while game_on:
            # Player 1 turn
            if turn == 'PLAYER 1':
                display_board(initboard)
                position = player_choice(initboard, turn)
                place_marker(initboard, player1_mark, position)

                if win_check(initboard, player1_mark):
                    display_board(initboard)
                    print('~~~~~Congratulations! PLAYER 1 have won the game!~~~~~')
                    game_on = 0
                else:
                    if full_board_check(initboard):
                        display_board(initboard)
                        print('---The game is a draw!---')
                        break
                    else:
                        turn = 'PLAYER 2'
            # Player 2 turn
            else:
                display_board(initboard)
                position = player_choice(initboard, turn)
                place_marker(initboard, player2_mark, position)

                if win_check(initboard, player2_mark):
                    display_board(initboard)
                    print('~~~~Congratulations! PLAYER 2 have won the game!~~~~')
                    game_on = 0
                else:
                    if full_board_check(initboard):
                        display_board(initboard)
                        print('---The game is a draw!---')
                        break
                    else:
                        turn = 'PLAYER 1'
        # keep playing or not
        if not replay():
            break

