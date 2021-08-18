import random

def is_int(num):  # проверка правой границы
    if not num.isdigit():
        return False
    elif int(num) <= 3:
        return False
    return True

def is_valid(num):  # проверка введенноего числа
    if not num.isdigit():
        return False
    if not 1 <= int(num) <= max_num:
        return False
    return True

def compare(user_num):  # сравнение с загаданным
    if user_num == quest:
        print('Вы угадали, поздравляем!')
        print(f'Количество сделанных попыток {try_count}')
        return True             
    elif user_num > quest:
        print('Ваше число больше загаданного, попробуйте еще разок')
        return False
    else:
        print('Ваше число меньше загаданного, попробуйте еще разок')
        return False

def user_input(max_num):  # ввод пользователя
    user_num = input()
    if user_num == stop_word:
        return 'stop'        
    while not is_valid(user_num):
        print(f'А может быть все-таки введем целое число от 1 до {max_num}?')
        user_num = input()
    else:
        user_num = int(user_num)
    return user_num

print('Добро пожаловать в числовую угадайку')
while True:    
    max_num = input('Из скольких чисел будем угадывать? (Введите число больше 3): ')
    while not is_int(max_num):
        print('Ну надо же число больше трех! А то не интересно...')
        max_num = input('Давайте еще раз: ')
    max_num = int(max_num)        
    quest = random.randint(1, max_num)
    stop_word = 'хватит'
    print('Итак, число загадано. Давайте угадывать')
    print(f'Вы может прервать игру введя слово "{stop_word}"')
    print(f'Введите число от 1 до {max_num}')
    try_count = 0
    is_solved = False

    while not is_solved:
        try_count += 1
        user_answer = user_input(max_num)
        if user_answer == 'stop':            
            break
        is_solved = compare(user_answer)
        
    if user_answer == 'stop':
        print('Очень жаль, что вы устали... до новых встреч')
        break
    else:
        is_more = input('Сыграем еще? (Y/N): ')
        if is_more.lower() != 'y':
            print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
            break
