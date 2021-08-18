# ====== imports block ================================== #
import random
import string
# ====== defining functions ============================= #
def is_int(num):  # контроль числового ввода
    if not num.isdigit():
        return False
    return True

def is_correct_answer(answer):
    if answer.lower() in ('y','n'):
        return True
    return False

def on_off(answer):
    if answer.lower() == 'y':
        return True
    else:
        return False

def generate_pwd(lenght, chars):
    pwd = ''
    for _ in range(lenght):
        pwd += random.choice(chars)

    return pwd

# ====== main code ====================================== #
digits = string.digits
lowercases = string.ascii_lowercase
uppercases = string.ascii_uppercase
punctuations = '!#$%&*+-=?@^_'  #string.punctuation
doubts = 'il1Lo0O'
chars = ''
pwd_list =[]

pwd_quant = input('сколько паролей надо сгененрировать? ')
while not is_int(pwd_quant):
    pwd_quant = input('это не число. Еще раз: ')
pwd_quant = int(pwd_quant)

pwd_len = input('длина пароля: ')
while not is_int(pwd_len):
    pwd_len = input('это не число. Еще раз: ')
pwd_len = int(pwd_len)

upper_on_quest = input('использовать ПРОПИСНЫЕ буквы? Y / N: ')
while not is_correct_answer(upper_on_quest):
    upper_on_quest = input('Y or N: ')

lower_on_quest = input('использовать строчные буквы? Y / N: ')
while not is_correct_answer(lower_on_quest):
    lower_on_quest = input('Y or N: ')

digit_on_quest = input('использовать цифры? Y / N: ')
while not is_correct_answer(digit_on_quest):
    digit_on_quest = input('Y or N: ')

punctuation_on_quest = input('использовать спецсимволы? Y / N: ')
while not is_correct_answer(punctuation_on_quest):
    punctuation_on_quest = input('Y or N: ')

doubt_on_quest = input('Исключить неоднозначные символы? Y / N: ')
while not is_correct_answer(doubt_on_quest):
    doubt_on_quest = input('Y or N: ')

upper_on = on_off(upper_on_quest)
lower_on = on_off(lower_on_quest)
digit_on = on_off(digit_on_quest)
punctuation_on = on_off(punctuation_on_quest)
doubt_on = on_off(digit_on_quest)

if upper_on:
    chars += uppercases
if lower_on:
    chars += lowercases
if digit_on:
    chars += digits
if punctuation_on:
    chars += punctuations
if  doubt_on: # нужно убрать из строки сомнительные символы
    chars = ''.join(i for i in chars if i not in doubts)

for _ in range(pwd_quant):
    pwd_list.append(generate_pwd(pwd_len, chars))

print(*pwd_list, sep='\n')
# ====== end of code ==================================== #
