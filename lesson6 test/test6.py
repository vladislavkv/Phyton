password = input('Введите пароль: ')

digit = ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0')
letters = ('q', 'w', 'e', 't', 'y', 'i', 'u', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'z', 'x', 'c', 'v', 'b', 'n', 'm')
symbols = ('@', '!', '#', '$', '%', '^', '&', '*')

hasDigit = False
hasLetter = False
hasSymbol = False

for sym in password:
    if sym in digit:
        hasDigit = True
    if sym in letters:
        hasLetter = True
    if sym in symbols:
        hasSymbol = True

if hasDigit == False:
    print('Пароль должен содержать цифры!')
    
if hasLetter == False:
    print('Пароль должен содержать буквы!')
    
if hasSymbol == False:
    print('Пароль должен содержать символы!')

if len(password) < 8:
    print('В пароле должно быть более 8 символов!')

if len(password) >= 8 and hasDigit == True and hasLetter == True and hasSymbol == True:
    print('Пароль хороший')
else:
    print('Пароль плохой')
