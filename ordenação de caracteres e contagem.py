def contagem_caracteres(s):
    ordenados=sorted(s)
    anterior=ordenados[0]
    cont=1
    resultado={}
    for atual in ordenados[1:]:
        if atual == anterior:
            cont+=1
        else:
            resultado[anterior]=cont
            anterior=atual
            cont=1
    resultado[anterior]=cont
    return resultado

print(contagem_caracteres('jonathan'))