from datetime import date
ano = date.today().year
nasc = int(input('Em que ano você nasceu: '))
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Você está na categoria mirim.')
elif idade <= 14:
    print('Você está na categoria infantil.')
elif idade <= 19:
    print('Você está na categoria Júnior.')
elif idade <= 25:
    print('Você está na categoria Sênior.')
else:
    print('Você está na categoria Master!')