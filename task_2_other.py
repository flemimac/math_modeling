a, b, c = map(int, input().split())

if (a + b > c) and (a + c > b) and (b + c > a):
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('Равнобедренный.')
    elif a != b != c:
        print('Разносторонний.')
    else:
        print('Равностронний.')
else:
    print('Треугольника не существует, проверьте данные.')