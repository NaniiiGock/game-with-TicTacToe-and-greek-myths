import random
introduction = "Коли Пандора привідкрила гореносну скриньку,\n\
з якої вилетіли всі нещастя, все ж, одне залишилось - ви.\n\
Ваша місія в майбутньому світі дуже важлива, \n\
тож не зволікайте, шукайте вихід! Скоріш, адже ви - інтернет-залежність!"

entrance = "а ось і вхід до лабіринту!\n\
Ой, леле, його охороняють два цербери!\n\
Здається, вони просять код, для того, щоб увійти.....а тут ще й табличка: \n\
    -----------\n\
    | fill in |\n\
    |  month  |\n\
    | number  |\n\
    -----------" 

sample = "ось нумерація полів:\
-------------\n\
| 1 | 2 | 3 |\n\
------------\n\
| 4 | 5 | 6 |\n\
------------\n\
| 7 | 8 | 9 |\n\
------------ \n\
    удачі на цьому етапі!"  

def bin_code():
    """відповідає за виконання завдання про бінарний пінкод"""
    pincode = random.randint(1, 13)
    months = ["січень", "лютий", "березень", "квітень","травень","червень","липень","серпень",\
       "вересень","жовтень","листопад","грудень"]
    month = months[int(pincode)-1]
    print(f'зараз {month},\n\
        введіть код для входу')
       
    for i in range(1, 4):
        input_code = input(">>> ") 
        if input_code != bin(pincode):
            if i == 1:
                print("цербери кажуть, що знають лише бінарну систему лічби ;(")
            elif i == 2:
                print('жах, спробуйте ще')
            print(f'залишилось {3 - i} спроб')
            if i == 3:
                print("спробуйте ще за 100 років......")
                exit
            
        else:
            print("супер, проходьте далі!")
            break    

def last_part_intro():
    print("огоооо, за полем для гри, виявляється, є ще й інша частина лабіринту....\n\
    поглянь, що це за дороговказ?")
    input(">>> ")
    print("--------------------\n\
    |     навпакинія     |\n\
    |      WELLCOME!     |\n\
    ----------------------")
    input(">>> ")
    print("a тут потрібно ще раз зіграти у гру, тільки правила зовсім інші!\n\
        спробуй тепер програти, у тебе 3 спроби!")


def draw_board(board):
    """ (board) -> None
     ігрове поле, побудоване зв допомогою символів
-------------
|   |   |   |
------------
|   |   |   |
------------
|   |   |   |
------------
"""
    print("-------------")
    for i in range(3):
        print("|", board[1 + i * 3], "|", board[2 + i * 3], "|", board[3 + i * 3], "|")
        print("------------")

def choose_symbol():
    """ () -> list[str]
    return: перший символ - вибраний гравцем для гри,
    другий - комп'ютера
    який символ обираєш для гри?
    >>> x
    return ['1', '0']
    """
    symbol = ''
    print('який символ обираєш для гри?(1, 0)')
    symbol = input(">>> ")
    if symbol == '1':
        return ['1', 'О']
    elif symbol == '0':
        return ['О', '1']
    else:
      
def first_player():
    """() -> Literal['комп'ютер', 'граець']
    return: визначає, хто ходить перший(randomly)
    """
    if random.randint(0, 1) == 0:
        return "комп'ютер"
    else:
        return "гравець"

def make_move(board, letter, move):
    """(board, letter, move) -> None
    забезпечення ходу"""
    board[move] = letter

def win_board(b, l):
    """(b, l) -> Any
    board = b, letter = l
    перевіряє можливі випадки виграшу по всіх лініях і діагоналях
    """
    return ((b[7] == l and b[8] == l and b[9] == l) or
    (b[4] == l and b[5] == l and b[6] == l) or 
    (b[1] == l and b[2] == l and b[3] == l) or 
    (b[7] == l and b[4] == l and b[1] == l) or 
    (b[8] == l and b[5] == l and b[2] == l) or 
    (b[9] == l and b[6] == l and b[3] == l) or 
    (b[7] == l and b[5] == l and b[3] == l) or 
    (b[9] == l and b[5] == l and b[1] == l)) 

def copy_board(board):
    """(board) -> list
    return: copy of board"""
    boardcopy = []
    for i in board:
        boardcopy.append(i)
    return boardcopy

def free_space(board, move):
    """(board, move) -> Any
    return True якщо хід можливий"""
    return board[move] == ' '

def getPlayerMove(board):
    """хід гравця, перевірка на можливість ходу
    return: номер поля, в яке вставляємо символ"""
    move = ''
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not free_space(board, int(move)):
        print('куди йдемо? (1-9):')
        move = input()
    return int(move)

def random_move(board, movesList):
    """(board, movesList) -> Any | None
    збирає усі можливі ходи"""
    possibleMoves = []
    for i in movesList:
        if free_space(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
       return random.choice(possibleMoves)
    else:
       return None

def getComputerMove(board, computerLetter):
    """(board, computerLetter) -> int | Any | None
    return: хід комп'ютера, найбільш виграшний в даній ситуації:
    спочатку заповнюються кути, потім середина, тоді вже бокові вільні поля"""
    if computerLetter == '1':
        playerLetter = 'О'
    else:
        playerLetter = '1'
    for i in range(1, 10):
        copy = copy_board(board)
        if free_space(copy, i):
            make_move(copy, computerLetter, i)
            if win_board(copy, computerLetter):
                return i
    for i in range(1, 10):
        copy = copy_board(board)
        if free_space(copy, i):
            make_move(copy, playerLetter, i)
            if win_board(copy, playerLetter):
                return i
    move = random_move(board, [1, 3, 7, 9])
    if move != None:
        return move
    if free_space(board, 5):
        return 5
    return random_move(board, [2, 4, 6, 8])

def getComputerMove2(board, computer_symbol):
    """(board, computerLetter) -> int | Any | None
    return: хід комп'ютера, найбільш програшний в даній ситуації:
    спочатку заповнюються бокові поля, потім середина, тоді вже кути"""
    if computer_symbol == '1':
        player_symbol = 'О'
    else:
        player_symbol = 'O'
    move = random_move(board, [2, 4, 6, 8])
    if move != None:
        return move
    return random_move(board, [1, 3, 5, 7, 9])
    
    
def full_board(board):
    """(board) -> bool
    return: визначає, чи є вільні поля"""
    for i in range(1, 10):
        if free_space(board, i):
            return False
    return True

def part_one():
    print(introduction)
    input(">>> ")
    print(entrance)

def finish():
    year = random.randint(1900, 3000)
    print(f'Втаємо, тепер інтернет-залежність серед людей!\n\
        ваша подорож завершилась у {year} році')
def game2():
    while True:
        Board = [' ']*10
        player_symbol, computer_symbol = choose_symbol()
        turn = first_player()
        print ('першим ходитиме '+turn +'\n')
        current_game = True 
        # exit_from_for = False
        
        while current_game:
            if turn == "гравець":
                draw_board(Board)
                move = getPlayerMove(Board)
                make_move(Board, player_symbol, move)
                if win_board(Board, player_symbol):
                    draw_board(Board)
                    print ("ви програли!")
                    current_game = False 
                    # exit_from_while = True
                else:
                    if full_board(Board):
                        draw_board(Board)
                        print("все б нічого, але нічия не рахується)")
                        break
                    else: 
                        turn = "комп'ютер"
            # elif exit_from_while:
            #     break
            else:   
                move = getComputerMove2(Board, computer_symbol)
                make_move(Board, computer_symbol, move)
                if win_board(Board, computer_symbol):
                    draw_board(Board)
                    print("ви виграли!")
                    finish()
                    exit
                    current_game = False 
                else:
                    if full_board(Board):
                        draw_board(Board)
                        print('Нічия')
                        break
                    else:
                        turn = "гравець" 


def game():
    print(sample)
    while True:
        Board = [' ']*10
        player_symbol, computer_symbol = choose_symbol()
        turn = first_player()
        print ('першим ходитиме '+turn +'\n')
        current_game = True 
        # exit_from_for = False
        
        while current_game:
            if turn == "гравець":
                draw_board(Board)
                move = getPlayerMove(Board)
                make_move(Board, player_symbol, move)
                if win_board(Board, player_symbol):
                    draw_board(Board)
                    print ("вітання! можете проходити далі!")
                    last_part_intro()
                    game2()
                    current_game = False 
                    
                    # exit_from_while = True
                else:
                    if full_board(Board):
                        draw_board(Board)
                        print("все б нічого, але нічия не рахується)")
                        break
                    else: 
                        turn = "комп'ютер"
            # elif exit_from_while:
            #     break
            else:   
                move = getComputerMove(Board, computer_symbol)
                make_move(Board, computer_symbol, move)
                if win_board(Board, computer_symbol):
                    draw_board(Board)
                    print("ви програли!")
                    current_game = False # вийти зі всієї гри
                    exit_from_for = True
                else:
                    if full_board(Board):
                        draw_board(Board)
                        print('Нічия')
                        break
                    else:
                        turn = "гравець" 

def main():
    part_one()            
    bin_code()        
    game()
if __name__ == "__main__":
    main()
