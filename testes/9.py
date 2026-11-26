txt = str(input("Texto: "))

def contar_vogais(txt):
    vogais = 'a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú'
    contador = 0

    for i in txt.lower():
        if i in vogais:
            contador += 1
    return contador

print(f'Vogais no texto: {contar_vogais(txt)}')