import board
# ------------------------------------------  main -----------------------------------------

game_board = board.Board()
game_board.update_board()
game_board.print_board()
game_board.play_game()
game_board.print_board()

if(game_board.check_win()):
    print("You are too good")
else:
    print("You get an unoptimized solution")


