import numpy as np
number = np.random.randint(1, 101)#загадываем число
count = 0

while True:
    count += 1
    predict_number = int(input('Угадай число от одного до ста: '))
    if predict_number < number:
        print('Введённое число меньше!')
    elif predict_number > number:
        print('Введённое число больше!')
    else:
        print(f'Вы угадали число! Это число {number}, за {count} попыток')
        break
    