a, b, c = map(int, input().split())

D = b**2 - 4 * a * c
d = D**0.5
if D == 0:
    print(-b / 2 * a)
elif D > 0:
    print((-b + d) / (2 * a),
          (-b - d) / (2 * a), sep='\n')
else:
    print('Нет корней.')