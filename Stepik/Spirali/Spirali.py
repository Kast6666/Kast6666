# ====== main code ====================================== #
n, m = map(int, input().split())
a = [[0] * m for _ in range(n)]
dr, dc, r, c = 0, 1, 0, 0

for cnt in range(1, n * m + 1):
    a[r][c] = cnt
    
    if a[(r + dr) % n][(c + dc) % m]:
        dr, dc = dc, -dr

    r += dr
    c += dc    
    
for row in a:
    print(*(f'{e:<3}' for e in row), sep='')
# ====== end of code ==================================== #
