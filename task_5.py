print('Шляпка гриба, покрытая (1) кожиц(2)й, держится на (3) ножк(4). Снизу шляпка затянута (5) плёнкой. Когда её уберёшь, откроется нижняя (6) сторона шляпк(7).')
n = 1
s = []

while n != 8:
    print(f'Недостающая буква или слово для {n}')
    a = input()
    s.append(a)
    n += 1

print(f"Шляпка гриба, покрытая {s[0]} кожиц{s[1]}й, держится на {s[2]} ножк{s[3]}. Снизу шляпка затянута {s[4]} плёнкой. Когда её уберёшь, откроется нижняя {s[5]} сторона шляпк{s[6]}.")