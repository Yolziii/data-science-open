"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0

    while True:
        count += 1
        predict_number = np.random.randint(1, 101)  # предполагаемое число
        if number == predict_number:
            break  # выход из цикла если угадали
    return count


def smart_predict(number: int = 1) -> int:
    """Trying to find the number by dividing search space by two

    Args:
        number (int, optional): Number to guess. Defaults to 1.

    Returns:
        int: Total attempts count
    """
    count = 0
    last_guess = 0
    search_direction = 1
    step = 50  
      
    while True:
        count += 1

        last_guess += step * search_direction
        if number == last_guess:
            break
        
        search_direction = 1 if number > last_guess else -1
        step = step//2 if step!=0 else np.random.randint(1, 3)
        
    return count
        

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    total_attempts = 1000
    random_array = np.random.randint(1, 101, size=(total_attempts))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Этот алгоритм за {total_attempts} запусков угадал число в среднем за {score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(smart_predict)
