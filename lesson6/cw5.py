myStr = input ('Введите число: ')

myLen = len(myStr)

if myStr[0] == '-':
    print('Отрицательное')
    myLen -= 1
else:
    print('Положительное')

if myLen == 1:
    print('Однозначное число')
elif len(myStr) == 2:
    print('Двузначное число')
elif myLen == 3:
    print('Трехзначное число')
elif myLen:
    print('Многозначное число')
    
