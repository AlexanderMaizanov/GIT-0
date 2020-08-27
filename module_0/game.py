import numpy as np
import math
Debug = False #Чтобы увидеть дополнительный вывод можно установить в True

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    upper = 100 #Верхний предел
    lower = 0 #Нижний предел
    
    predict = (upper - lower)/2 #Делим наш интервал пополам, чтобы ускорить поиск решения
    while number != predict:
        count += 1
        if Debug: print(f"try: {count}, predict: {predict}")
        if number > predict:
            lower = predict #Задаем новый нижний предел
            predict += int(math.ceil((upper - predict)/2.0)) #вычисляем предсказание
            if Debug: print("more")
        elif number < predict:
            upper = predict #Задаем новый верхний предел
            predict -= int(math.ceil((predict - lower)/2.0))#вычисляем предсказание
            if Debug: print("less")
        
    return(count) # выход из цикла, если угадали

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        if Debug: print(f"number = {number}")
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

score_game(game_core_v3)