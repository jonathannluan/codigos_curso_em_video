frase=input('Qual o seu nome?')

print('Seu nome maiúsculo é:{} '.format(frase.upper()))
print('Seu nome minúsculo é:{} '.format(frase.lower()))
print('Seu nome tem {} caracteres'.format(len(frase)-frase.count(' ')))
frase=frase.split()
print('Seu primeiro nome tem {} letras'.format(len(frase[0])))




