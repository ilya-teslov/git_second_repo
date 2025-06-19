def is_digits_increasing_reverse(N):
    # Преобразуем число в строку для обработки цифр
    digits = str(N)
    
    # Проверяем, что каждая следующая цифра (справа налево) не меньше предыдущей
    for i in range(len(digits)-1, 0, -1):
        if digits[i] < digits[i-1]:
            return False
    return True

# Ввод числа от пользователя
N = int(input("Введите число N: "))

# Проверка и вывод результата
if is_digits_increasing_reverse(N):
    print(f"Цифры числа {N} при просмотре справа налево упорядочены по возрастанию")
else:
    print(f"Цифры числа {N} при просмотре справа налево НЕ упорядочены по возрастанию")