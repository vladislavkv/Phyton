#Shop database
#file = open ('database.txt', 'r', encoding = 'utf-8')

#leastProduct = 9999
#leastLine = [ ]

#for line in file:
#    valuesList = line.split (',')

#    if int (valuesList[4]) < leastProduct:
#        leastProduct = int (valuesList[4])
#        leastLine = valuesList
        
#print ('Меньше всего товара под названием:', leastLine[1])
#print ('Остаток:', leastLine[4])

#
personInfo ={
              'виктор':'+7(***)***9052',
              'рахат':'+7(***)****1265',
              'максим':'+7(***)***7542',
              'олег':'+7(***)***2374'
            }

personName = input ('Введите имя: ')
personName = personName.lower()

if personName in personInfo:
    print (personInfo[personName])
else:
    print ('Ошибка! (Такого имени нет)')



    



