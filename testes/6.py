primo = int(input('numero: '))

if primo < 2:
    print('nao primo')
else:
    for i in range(2, primo):
        if primo % i == 0:
            print("nao primo")
            break
    else:
        print('primo')

