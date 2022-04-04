def ano(x):
    from datetime import date
    idade=date.today().year - x
    if 15<idade<18 or idade >70:
        return f'Você tem {idade} anos. O voto é OPCIONAL'
    elif idade <16:
        return f'Votê tem {idade} anos. Não pode votar.'
    else:
        return f'Você tem {idade} anos. O voto é OBRIGATÓRIO.'



print(ano(2008))
