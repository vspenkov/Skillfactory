#Приветствие
super_game = input("""Введите Y, если хотите начать игру или N,
             если хотите сыграть позже: """)

game = super_game == "Y"

def is_game(func):
    def wrapper():
        if game:
            print("Приятной игры :)")
            print("Первые ходят 'X'")
            func()
        else:
            print("Будем ждать Вас позже :(")
    return wrapper

@is_game
def new_game():
    print("Начало новой игры")

#создаем поле
    board = [[" "," "," "] for i in range(3)]

    def drow_board(board):
        print("  | 0 | 1 | 2 |")
        print("---------------------")
        for i in range(3):
            print(f"{i} | {board [i][0]} | {board [i][1]} | {board [i][2]}  |")
        print("---------------------")


#Проверка на победу

    def detect_win():
        prov_win = [((0 , 0), (0, 1), (0, 2)), ((0, 0), (1, 0), (2, 0)), ((1, 0), (1 , 1), (1, 2)),
                    ((2, 0), (2, 1), (2, 2)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 1), (2, 0)),
                    ((0,0), (1, 1), (2, 2)), ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2))]
        for win in prov_win:
            a = win[0]
            b = win[1]
            c = win[2]

            if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] != " ":
                print(f"Выиграл {board[a[0]][a[1]]}")
                return True
        return False




    #Ввод данных и проверка на занятость ячейки
    def inp():
        while True:
            x,y = list(map(int, input("Введите параметры Вашего хода:").split()))
            if 0 <= x <= 2 and 0 <= y <= 2 :
                if board [x][y] == " ":
                    return x,y
                else:
                    print ("Ячейка занята, выберите другую")

            else:
                print("Промахнулся мимо поля, внимательней :)")


    cord = 0
    while True:
        cord +=1

        drow_board(board)

        if cord % 2 == 1:
            print ("Ходит крестик")
        else:
            print ("Ходит нолик")

        x, y = inp()

        if cord % 2 == 1:
            board[x][y] = "X"
        else:
            board[x][y] = "0"
        if detect_win():
            again = input('Сыграть еще раз?(N/Y)')
            if again == "Y":
                continue
            else:
                break
            break

        if cord == 9:
            print("Ничья")
            break




new_game()