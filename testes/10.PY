
def estatiscas(num):
    menor = min(num)
    maior = max(num)
    media = sum(num) / len(num)
    return menor, maior, media

entrada = input("Digite 3 ou mais números, separados por espaço: ")

n = [float(i) for i in entrada.split()]

print(f'Menor, maior e média: {estatiscas(n)}')
