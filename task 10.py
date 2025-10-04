while True:
    user_input = input()
    if user_input == "стоп":
        break
    try:
        number = float(user_input)
        print(number)
    except ValueError:
        print("Ошибка: введите число или 'стоп'.")