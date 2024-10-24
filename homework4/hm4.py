def valid(value):
    try:
        float(value.replace(',', '.')) 
        return True
    except ValueError:
        return False

def number(prompt):
    value = input(prompt)
    if valid(value):
        return float(value.replace(',', '.'))
    else:
        print("Ошибка: введите корректное число.")
        return number(prompt) 

a = number("Введите значение a: ")
b = number("Введите значение b: ")
c = number("Введите значение c: ")

x = 7 * b + 2 * c - a

print(f"Результат: x = {x}")