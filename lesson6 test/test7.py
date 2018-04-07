fio = input('Введите ФИО: ')

fioMas = fio.split(' ')

firstName = fioMas[1].capitalize()
lastName = fioMas[0].capitalize()
middleName = fioMas[2].capitalize()

print(lastName + ' ' + firstName + ' ' + middleName)
