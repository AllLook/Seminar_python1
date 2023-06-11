from random import randint
num = randint(0, 1000)
print(num)
print("Игра начинается!Программа загадала число!")
i = 0
while i < 10:
    number = input("Угадай число от 0 до 1000:")
    if number.isdigit():
        number = int(number)
        if num == number:
            print("Поздравляю!Вы выиграли!")
            break

        elif number > num:
            print("Подсказка: введите число меньше")
        else:
            print("Подсказка: введите число больше")
    else:
        print("Повторите с корректным вводом!")
    i += 1


print("До свидания!")
