def print_board(board, p1_store, p2_store):
    '''
    Takes 3 inputs (board list, P1 store, and P2 store) and prints out the
    correctly formatted board.
    '''
    print("P1   1 2 3 4 5 6     ")
    print("  -----------------  ")
    print("    |{}|{}|{}|{}|{}|{}|    ".format(*board[0]))
    print(" {}  -------------  {} ".format(p1_store, p2_store))
    print("    |{}|{}|{}|{}|{}|{}|    ".format(*board[1]))
    print("  -----------------  ")
    print("     6 5 4 3 2 1   P2")
    
def get_move(player, board):
    '''
    Asks the player for the space that they want to play.  If the input is 
    invalid or the space is empty, it tries again.
    '''
    space = int(input("Player {} enter a space:  ".format(player)))
    if (space < 1 or space > 6):
        print("Invalid input.  Enter a number between 1 and 6.")
        space = get_move(player, board)
    if player == 1:
        if board[0][space - 1] == 0:
            print("Empty space.  Please try again.")
            space = get_move(player, board)
    else:
        if board[1][6 - space] == 0:
            print("Empty space.  Please try again.")
            space = get_move(player, board)
    return space
    
def make_move(player, space, board, p1_store, p2_store):
    '''
    Takes the space that the user inputed and makes the correct move based on
    the number of stones in that space.  If the last stone lands in the 
    player's store, the player gets another turn.  If the last stone ends in an
    empty space on the player's side, the player gets that stone and any stones 
    in the space across from it.
    '''
    if player == 1:
        current = [0, space - 1]
    else:
        current = [1, 6 - space]
    count = board[current[0]][current[1]]
    board[current[0]][current[1]] = 0
    for i in range(count):
        # update position
        if current[0] == 0:
            current[1] -= 1
        else:
            current[1] += 1
        
        # Add stones to space
        
        # add to store
        if player == 1 and current[1] == -1:
            p1_store += 1
            if i == count - 1:
                print_board(board, p1_store, p2_store)
                print("You get another turn!")
                space = get_move(player, board)
                board, p1_store, p2_store = make_move(player, space, board, p1_store, p2_store)
        elif player == 2 and current[1] == 6:
            p2_store += 1
            if i == count - 1:
                print_board(board, p1_store, p2_store)
                print("You get another turn!")
                space = get_move(player, board)
                board, p1_store, p2_store = make_move(player, space, board, p1_store, p2_store)
        
        else:
            # correct position
            if current[1] < 0:
                current[0] += 1
                current[1] = 0
            elif current[1] > 5:
                current[0] -= 1
                current[1] = 5
            
            # add to space
            if (i == count - 1) and (board[current[0]][current[1]] == 0):
                print(current)
                if player == 1 and current[0] == 0:
                    print("You landed in an empty space!")
                    p1_store += (board[1][current[1]] + 1)
                    board[1][current[1]] = 0
                    return (board, p1_store, p2_store)
                elif player == 2 and current[0] == 1:
                    print("You landed in an empty space!")
                    p2_store += (board[0][current[1]] + 1)
                    board[0][current[1]] = 0
                    return (board, p1_store, p2_store)
            board[current[0]][current[1]] += 1
    return (board, p1_store, p2_store)
            
def play_game(board, p1_store, p2_store):
    '''
    Check if either of the players have no stones left.  Adds any remaining
    stones left on a players side when the game ends.
    '''
    p1_left = 0
    p2_left = 0
    for i in range(6):
        p1_left += board[0][i]
        p2_left += board[1][i]
    if p1_left == 0:
        p2_store += p2_left
        return False
    elif p2_left == 0:
        p1_store += p1_store
        return False
    return True
    
            
def main():
    '''
    Sets up the game and runs the main game loop until the game is over.
    '''
    board = [[4, 4, 4, 4, 4, 4],[4, 4, 4, 4, 4, 4]]
    p1_store = 0
    p2_store = 0
    player = 1
    while play_game(board, p1_store, p2_store):
        print_board(board, p1_store, p2_store)
        space = get_move(player, board)
        board, p1_store, p2_store = make_move(player, space, board, p1_store, p2_store)
        if player == 1:
            player = 2
        else:
            player = 1
    print_board(board, p1_store, p2_store)
    if p1_store > p2_store:
        print("Player 1 wins!")
    elif p2_store > p1_store:
        print("Player 2 wins!")
    else:
        print("Tie!")

if __name__ == "__main__":
    main()
