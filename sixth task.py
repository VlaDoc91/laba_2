a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if (a <= b and a <= c):
    if (b <= c):
        print(f'{a} {b} {c}')
else:
    print(f'{a}{b}{c}')
elif (b <= c and b <= a):
    if (a <= c):
        print(f'{b}{c}{a}')
else:
    print(f'{b}{c}{a}')
