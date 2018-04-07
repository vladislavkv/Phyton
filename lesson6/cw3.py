def summa(a):
    a = a.split()
    b = []
    
    for i in a:
        b.append(int(i))
    return sum(b)
 
s = 0

while 1:
    a = input()
    if a == ' ': break
    s += summa(a)
    print('Сумма строк равна:', s)
