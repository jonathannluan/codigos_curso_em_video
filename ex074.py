from random import randint
num=(randint(1,10),randint(1,10),randint(1,10),randint(1,10),randint(1,10))
print('Os valores foram: ', end=' ')
for c in num:
    print(f'{c} ' , end='')
print(f'\n O maior valor foi o {max(num)} e o menor foi {min(num)}')
