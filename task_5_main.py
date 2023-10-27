first = int(input())
second = int(input())

remains = first % second

if first / second:
    print('Первое число делиться на второе.')
if remains != 0:
    print(f'Остаток равен {remains}.')
print(f'Целое равен {first / second}.')
