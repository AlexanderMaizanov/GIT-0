import numpy as np
import math
Debug = False

def game_core_v3(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    upper = 100
    lower = 0
    
    predict = (upper - lower)/2
    while number != predict:
        count += 1
        if Debug: print(f"try: {count}, predict: {predict}")
        if number > predict: #more
            lower = predict
            predict += int(math.ceil((upper - predict)/2.0))
            if Debug: print("more")
        elif number < predict: #less
            upper = predict
            predict -= int(math.ceil((predict - lower)/2.0))
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