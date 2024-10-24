Chisla = input("Введите целое десятичное число: ")

if Chisla.lstrip('-').isdigit():
    Chisla = int(Chisla)
    if Chisla >= 0:
        bin = bin(Chisla)[2:]
        oct = oct(Chisla)[2:]
    else:
        bin = '-' + bin(abs(Chisla))[2:]
        oct = '-' + oct(abs(Chisla))[2:]
    print(f"Двоичное представление: {bin}")
    print(f"Восьмеричное представление: {oct}")
else:
    print("Ошибка: введите корректное целое число.")