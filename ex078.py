v=list()
maior=0
menor=0
for c in range(0,5):
    v.append(int(input(f'Informe o valor da posição {c}: ')))
    if c==0:
        maior=menor=v[c]
    elif v[c]>maior:
        maior=v[c]
    elif v[c]<menor:
        menor=v[c]
print(f'O maior valor {maior} aparece nas posições: ')
for x,k in enumerate(v):
    if k==maior:
        print(f'{x}...',end='')
print(f'\n O menor valor {menor} aparece nas posições: ')
for t,l in enumerate(v):
    if l==menor:
        print(f'{t}...',end='')



