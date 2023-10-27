number = int(input())
count = 2
while count * count <= number:
    if number % count != 0:
        count += 1
    else:
        number //= count
        print(count, end=" ")
if number != 1:
    print(number)