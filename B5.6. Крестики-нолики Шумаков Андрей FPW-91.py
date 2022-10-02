def start():  # приветствие и правила игры
    print('-----------------------------------\n'
          'Приветствую в игре крестики-нолики!\n'
    '-----------------------------------\n'
    '-----------Правила игры------------\n'
    '----Для того, чтобы сделать ход----\n'
          '--необходимо ввести 2 координаты:--\n'
    '         х - номер строки\n'
    '         у - номер столбца\n'
    '     первым ходит - крестик(X)\n'
    '       затем ходит - нолик(O)')



def show_field():  # функция отрисовки игрового поля
    print('  0 1 2 ')
    for i in range(len(field)):  # отрисовка строк игрового поля
        print(str(i), *field[i])



def users_input():  # функция опроса игроков
    while True:
        coordinates = input('Введите координаты :').split()
        x, y = map(int, coordinates)

        if len(coordinates) != 2:
            print('Введите две координаты!')
            continue

        if not(coordinates[0].isdigit() and coordinates[1].isdigit()):
            print('Необходимо ввести цифры!')
            continue


        if not(x >= 0 and x < 3 and y >= 0 and y < 3):
            print('Необходимо ввести координаты от 0 до 2!')
            continue

        if field[x][y] != '-':
            print('Клетка занята!')
            continue

        break
    return x, y


def check_winner():  # функция определения выигрышных комбинаций
    winner_comb = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    
    for coord in winner_comb:
    symbols = []
        for c in coord:
            symbols.append(field[c[0]][c[1]])
        if symbols == ['X', 'X', 'X']:
            print('Выиграл крестик!')
            return True
        if symbols == ['0', '0', '0']:
            print('Выиграл нолик!')
            return True
    return False


start()
field = [['-'] * 3 for i in range(3)]  # строка игрового поля
count = 0  # подсчет ходов
while True:
    count += 1
    show_field()  # объявление функции отрисовки игрового поля
    if count % 2 == 1:
        print('Ходит крестик!')
    else:
        print('Ходит нолик!')

    x, y = users_input()

    if count % 2 == 1:
        field[x][y] = 'X'
    else:
        field[x][y] = 'O'

    if check_winner():  # проверка выигрышных комбинаций
        break

    if count==9:
        print('Ничья!')
        break
