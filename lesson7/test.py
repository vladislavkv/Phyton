# a = [int(input('Введите 1е число: ')), int(input('Введите 2е число: ')), int(input('Введите 3е число: '))]
# print('Сумма наибольших чисеел: ', sum(sorted(a)[1:]))

questions = ('Какого цвета кофта Рахата?',
         'Самый лучший певец в мире?',
         'Курица или яйцо?',
         'Кто следующий президент России?',
         'Сколько частей в форсаже?')

rightAnswers = (1,1,2,3,3)
myAnswers = []
rights = 0

answers = (['Серого','Желтого','Прозрачного'],
        ['Кайрат Нуртас','Торегали Тореали','Риана'],
        ['Курица','Яйцо','Хз'],
        ['Путин','Путин','Воспрос не имеет смысла'],
        ['6','7','8'])

for question in questions:
    print(question)
    i = questions.index(question)
    for answer in answers[i]:
        print(answer)
    myAnswers.append(int(input('Ответ: ')))

for i in range(len(rightAnswers)):
    if rightAnswers[i] == myAnswers[i]:
        rights += 1

print('Кол-во правильных ответов: ' + str(rights))
        
