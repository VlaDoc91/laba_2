a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = int(input('Введите третье число: '))
if a > b > c:
    print(a)
elif b > a > c:
    print(b)
else:
    print(c)
print('Finish')
