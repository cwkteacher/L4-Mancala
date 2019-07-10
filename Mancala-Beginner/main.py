board = []
p1_store = 0
p2_store = 0

def print_board():
    '''
    Takes 3 inputs (board list, P1 store, and P2 store) and prints out the
    correctly formatted board.
    '''
    global board, p1_store, p2_store
    
    print("P1   1 2 3 4 5 6     ")
    print("  -----------------  ")
    print("    |{}|{}|{}|{}|{}|{}|    ".format(board[0], board[1], board[2], board[3], board[4], board[5]))
    print(" {}  -------------  {} ".format(p1_store, p2_store))
    print("    |{}|{}|{}|{}|{}|{}|    ".format(board[11], board[10], board[9], board[8], board[7], board[6]))
    print("  -----------------  ")
    print("     6 5 4 3 2 1   P2")
    
def get_move(player):
    '''
    Asks the player for the space that they want to play.  If the input is 
    invalid or the space is empty, it tries again.
    '''
    global board
    
    space = int(input("Player {} enter a space:  ".format(player)))
    if (space < 1 or space > 6):
        print("Invalid input.  Enter a number between 1 and 6.")
        space = get_move(player)
    elif player == 1:
        if board[space - 1] == 0:
            print("Empty space.  Please try again.")
            space = get_move(player)
    else:
        if board[space + 5] == 0:
            print("Empty space.  Please try again.")
            space = get_move(player)
    return space
    
def make_move(player, space):
    '''
    Takes the space that the user inputed and makes the correct move based on
    the number of stones in that space.  If the last stone lands in the 
    player's store, the player gets another turn.  If the last stone ends in an
    empty space on the player's side, the player gets that stone and any stones 
    in the space across from it.
    '''
    global board, p1_store, p2_store
    
    if player == 1:
        current = space - 1
    else:
        current = space + 5
    count = board[current]
    board[current] = 0
    for i in range(count):
        # update position
        if player == 1 and current == 0:
            current = -1
        elif player == 1 and current == -1:
            current = 11
        elif player == 2 and current == 6:
            current = -1
        elif player == 2 and current == -1:
            current = 5
        elif current == 0:
            current = 11
        else:
            current -= 1
        
        # add stone to space
        if current == -1:
            if player == 1:
                p1_store += 1
            else:
                p2_store += 1
        
        else:
            board[current] += 1
            
def play_game():
    '''
    Check if either of the players have no stones left.  Adds any remaining
    stones left on a players side when the game ends.
    '''
    global board, p1_store, p2_store
    
    p1_left = 0
    p2_left = 0
    for i in range(6):
        p1_left += board[i]
        p2_left += board[i + 6]
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
    global board, p1_store, p2_store
    
    board = [4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4]
    p1_store = 0
    p2_store = 0
    player = 1
    while play_game():
        print_board()
        space = get_move(player)
        make_move(player, space)
        if player == 1:
            player = 2
        else:
            player = 1
    print_board()
    if p1_store > p2_store:
        print("Player 1 wins!")
    elif p2_store > p1_store:
        print("Player 2 wins!")
    else:
        print("Tie!")

if __name__ == "__main__":
    main()
