number = int(input())
while number > 0:
    last = number % 10
    number //= 10
    print(last, end="")