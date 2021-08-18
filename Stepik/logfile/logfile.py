# ====== main code ====================================== #
with open('logfile.txt', 'r', encoding='utf-8') as f, open('output.txt', 'w') as l:
    text = [line.strip().split() for line in f.readlines()]
    for line in text:
        if int(line[3][:2]) - int(line[2][:2]) >= 2 or int(line[3][:2]) - int(line[2][:2]) == 1 and int(line[3][3:5]) - int(line[2][3:5]) >= 0:
            print(line[0], line[1][:-1], file=l)
# ====== end of code ==================================== #            
