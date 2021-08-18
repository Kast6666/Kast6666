# ====== imports block ================================== #
import re
# ====== main code ====================================== #
num = int(input())
for i in range(num):
    if re.search(r'.*a.*n.*t.*o.*n', input()):
        print(i + 1, end=' ')
# ====== end of code ==================================== #
