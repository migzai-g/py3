s = int(input("Segundos: "))

h, r = divmod(s, 3600) # primeiro com 3600, que é 1 hora
m, s = divmod(r, 60) # depois com 60, 1 minuto

print(f'A hora é: {h:02d}:{m:02d}:{s:02d}') # :02d completa com 0 à esqueda


