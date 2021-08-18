# ====== main code ====================================== #
word = input() + ' запретил букву'
b = ['а', 'б', 'в', 'г', 'д', 'е', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
exclu = 0

while word.strip() != '':
    
    if word == word.replace(b[exclu], '') and exclu != 31:
        exclu += 1
        continue
    else:
        print(word, b[exclu])
        word = word.replace(b[exclu], '')
        word = word.replace('  ', ' ').strip()
        exclu += 1
# ====== end of code ==================================== #
