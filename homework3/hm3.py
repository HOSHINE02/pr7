# Функция для перевода числа в тринадцатеричную систему с использованием рекурсии
def sist13(number):
    if number == 0:
        return ''
    symbols = '0123456789ABC'  # Символы тринадцатеричной системы
    return sist13(number // 13) + symbols[number % 13]

# Основная программа
def main():
    user_input = input("Введите десятичное целое число (от 0 до 10000): ")

    if user_input.lstrip('-').isdigit():  # Проверяем, что введено целое число
        decimal_number = int(user_input)

        if 0 <= decimal_number <= 10000:  # Ограничение диапазона чисел
            sist13_number = sist13(decimal_number)
            sist13_number = sist13_number if sist13_number else '0'  # Если 0, то выводим '0'
            print(f"Тринадцатеричное представление: {sist13_number}")
        else:
            print("Ошибка! Введите число в диапазоне от 0 до 10000.")
    else:
        print("Ошибка! Введите целое число.")

# Вызов основной программы
main()