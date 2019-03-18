#Tic tac toe game
#Sinh Bui
#Oct 22 - 2018
board = "|_|_|_|\n|_|_|_|\n|_|_|_|\n"
print(board)
p1_name = input("Player 1's name: ")
p2_name = input("Player 2's name: ")
print(f"Welcome to the game, {p1_name} and {p2_name}")
p_flag = 'x'
#p_name = [p1_name,p2_name]
tic_his = []
end_game = False

def update_board(board, tic, p_flag):
    if tic == 1:
        board = board[:17]+p_flag+board[18:]
    elif tic == 2:
        board = board[:19]+p_flag+board[20:]
    elif tic == 3:
        board = board[:21]+p_flag+board[22:]
    elif tic == 4:
        board = board[:9]+p_flag+board[10:]
    elif tic == 5:
        board = board[:11]+p_flag+board[12:]
    elif tic == 6:
        board = board[:13]+p_flag+board[14:]
    elif tic == 7:
        board = board[:1]+p_flag+board[2:]
    elif tic == 8:
        board = board[:3]+p_flag+board[4:]
    elif tic == 9:
        board = board[:5]+p_flag+board[6:]
    return board

def board_full_check(board):
    #b = list(board)
    if '_' in [board[1],board[3],board[5],board[9],board[11],board[13],board[17],board[19],board[21]]:
        return False
    else:
        return True

def result_check(board):
    straight = [[board[1],board[3],board[5]],[board[9],board[11],board[13]],[board[17],board[19],board[21]],
                [board[1],board[9],board[17]],[board[3],board[11],board[19]],[board[5],board[13],board[21]],
                [board[1],board[11],board[21]],[board[5],board[11],board[17]]]
    #print(straight)
    for s in straight:
        if s == ['x','x','x']:
            return [True,p1_name]
            print(s)
        if s == ['o','o','o']:
            return [True,p2_name]
    return [False,'No one']

while (end_game!=True):
    if p_flag=='x':
        print(f"{p1_name}'s turn, please enter a number from 1 to 9: ")
        try:
            tic = int(input())
        except ValueError:
            print('Please enter a number from 1 to 9.')
            continue
        if tic in tic_his:
            print('This place has been occupied, please choose another place.')
            continue
        if tic < 1 or tic > 9:
            print('Please enter a number from 1 to 9.')
            continue
        board = update_board(board, tic, p_flag)
        print(board)
        p_flag = 'o'
    elif p_flag=='o':
        print(f"{p2_name}'s turn, please enter a number from 1 to 9: ")
        try:
            tic = int(input())
        except ValueError:
            print('Please enter a number from 1 to 9.')
            continue
        if tic in tic_his:
            print('This place has been occupied, please choose another place.')
            continue
        if tic < 1 or tic > 9:
            print('Please enter a number from 1 to 9.')
            continue
        board = update_board(board, tic, p_flag)
        print(board)
        p_flag = 'x'
    tic_his.append(tic)
    
    [win, winner] = result_check(board)
    
    if win == True or board_full_check(board)==True:
        end_game = True
    
    if end_game==True:
        if win == True:
            print(f"{winner} win! \*/ \*/ \*/")
        else:
            print(f"Draw!")
        ans = input(f"The game is end, do you want to restart? (Y/N) ")
        if ans.lower() in ["y","yes"]:
            board = "|_|_|_|\n|_|_|_|\n|_|_|_|\n"
            print(board)
            p1_name = input("Player 1's name: ")
            p2_name = input("Player 2's name: ")
            print(f"Welcome to the game, {p1_name} and {p2_name}")
            p_flag = 'x'
            #p_name = [p1_name,p2_name]
            tic_his = []
            end_game = False
    
