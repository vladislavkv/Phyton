file = open('database.txt', 'r', encoding = 'utf-8')

leastProduct = 9999
leastLine = [ ]

for line in file:
    valuesList = line.split(',')

    if int (valuesList[4]) < leastProduct:
        leastProduct = int (valuesList[4])
        leastLine = valuesList
        
print ('Меньше всего товара под названием:', leastLine[1])
print ('Остаток:', leastLine[4])


    



