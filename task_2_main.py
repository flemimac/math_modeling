b1, q, n = int(input()), int(input()), int(input())
b = b1

for i in range(1, n):
    b_cur = b * q
    print(b_cur)
    b = b_cur