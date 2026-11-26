def primo(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0: 
        return False
    for i in range(3, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input('Número: ')) 
print('True: primo; False: não primo')
print(f'{primo(n)}, {n}')    