def contagem_caracteres(s):
    resultado={}
    for caracteres in s:
        cont=resultado.get(caracteres,0)
        cont+=1
        resultado[caracteres]=cont
    return resultado


print(contagem_caracteres('jonathan'))
print()
print(contagem_caracteres('banana'))