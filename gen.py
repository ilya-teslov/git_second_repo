import random

def generate_and_display_numbers(N):
    # Генерируем список из N случайных чисел от -10 до 10
    numbers = [random.randint(-10, 10) for _ in range(N)]
    
    # Выводим весь список
    print("Весь список:", numbers)
    
    # Выводим все элементы, кроме последних двух
    if N > 2:
        print("Элементы кроме последних двух:", numbers[:-2])
    else:
        print("В списке меньше 3 элементов, невозможно показать элементы кроме последних двух")

# Пример использования
N = int(input("Введите количество чисел N: "))
generate_and_display_numbers(N)