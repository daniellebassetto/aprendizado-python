dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))

if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
    if mes == 2:
        if dia >= 1 and dia <= 29:
            print('Data válida!')
        else:
            print('Dia inválido!')
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print('Data válida!')
        else:
            print('Dia inválido!')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print('Data válida')
        else:
            print('Dia inválido!')
    else:
        print('Mês inválido!')
else:
    if mes == 2:
        if dia >= 1 and dia <= 28:
            print('Data válida!')
        else:
            print('Dia inválido!')
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
        if dia >= 1 and dia <= 31:
            print('Data válida!')
        else:
            print('Dia inválido!')
    elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
        if dia >= 1 and dia <= 30:
            print('Data válida')
        else:
            print('Dia inválido!')
    else:
        print('Mês inválido!')