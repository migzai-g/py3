nome = (input("Nome: "))
palavras = nome.split()

for i in palavras:
    print(i[0].upper(), end="") # Printa a primeira letra de cada nome em maiúsculo
                                # Tentei usar replace(' ', '') primeiramente. Porém, o split já tira os espaços.

