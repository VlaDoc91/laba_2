n = int(input())
break_1 = n//2 * 5
break_2 = (n - 1)//2 * 15
minutes = 9 * 60 + n * 45 + break_1 + break_2
print(f'{minutes//60} {minutes%60}')
