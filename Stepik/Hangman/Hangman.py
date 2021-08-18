# ====== imports block ================================== #
from random import *
# ====== defining functions ============================= #
def get_word_rus(): # Возвращает случайное слово из функции набора слов для игры
    return word_rus[randint(0, len(word_rus) - 1)]

def correct_answer(answer): # Проверят корректность ответа на альтернативный вопрос о продолжении игры
    if answer.lower() == 'y' or answer.lower() == 'да' or answer.lower() == 'n' or answer.lower() == 'нет':
        return True
    return False



#графическое изображение висилицы
def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        ''',
        # голова, торс, обе руки, одна нога
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        ''',
        # голова, торс, обе руки
        '''
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        ''',
        # голова, торс и одна рука
        '''
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        ''',
        # голова и торс
        '''
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        ''',
        # голова
        '''
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        ''',
        # начальное состояние
        '''
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        '''
    ]
    return stages[tries]

def play(word): #Основная функция для запуска игры
    word_completion = list(len(word) * '_') # список из угаданных букв(изначально из прочерков)
    guessed = False  # сигнальная метка
    guessed_letters = []  # список уже названных букв
    guessed_words = []  # список уже названных слов
    tries = 6  # количество попыток

    print('Давайте играть в угадайку слов!')




    while True:
        print(display_hangman(tries))
        if tries == 0: #
            break
        print(f'Допустимых промахов: {tries}')
        print(*word_completion, sep = '') #Распаковка объектов в списке из угаданных букв(сепаратор без пробела)
        print('Введите букву или слово')
        word_player = input().lower()
        while True:
            if word_player.lower() in guessed_letters or  word_player.lower() in guessed_words : #Вводились ли раньше
                print('Буква или слово уже вводились')
                print('Введите букву или слово')
                word_player = input().lower()

                continue
            flag_letters = True
            for i in word_player: #Итерация всех введёных символов для проверки наличия в алфавите
                if i not in alpha_rus:
                    flag_letters = False #Если хоть 1 буква не подходит, то попытка считается некорректной
            if flag_letters:
                break
            print('Неверный формат')
            print('Введите букву или слово')
            word_player = input().lower()

        if len(word_player) >= 2: # Если больше 1 буквы, то инпут отправляется в список уже введёных слов
            guessed_letters.append(word_player)
        elif len(word_player) == 1: # Если меньше 1 буквы, то инпут отправляется в список уже введёных букв
            guessed_words.append(word_player)

        if word_player in word: # Если указанная буква или слово есть в загаданном слове
            for i in range(len(word) - len(word_player) + 1): #Замена буквы\части слово в списке из прочерков на угаданное значение
                if word[i:i + len(word_player)] == word_player:
                    word_completion[i:i + len(word_player)] = word_player
            print(*word_completion, sep = '')
            word_completion_string = ''.join(word_completion) # Преобразование списка угаданных букв в строку
            if  word_completion_string == word: # Сравнение строки указанных букв с загаданным словом
                guessed = True
                break
            continue
        else:
            tries -= 1  # Уменьшение доступных попыток на одну
    if guessed == True:
        print('Вы выиграли!')
    else:
        print('Вы проиграли')
    print()
    print('Продолжить выполнение программы? y/ДА n/НЕТ')
    answer_exit = input()
    while True:
        if correct_answer(answer_exit) == True:
            break
        print('Введите корректный ответ')
        print('Продолжить выполнение программы? y/ДА n/НЕТ')
        answer_exit = input()
    if answer_exit.lower() == 'y' or answer_exit.lower() == 'да':
        play(get_word_rus())


# ====== main code ====================================== #
word_rus = ['список_слов'] #Набор слов для игры
z = ord('а')
alpha_rus = ''.join([chr(i) for i in range(z,z+32)]) #Формирование букв из русского алфавита(прописного формата)
play(get_word_rus())  #Запуск игры
# ====== end of code ==================================== #
