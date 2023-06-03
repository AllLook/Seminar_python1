number = int(input("Введите целое число:"))
if number <= 0 or number == 0 or number == 1 or number > 100000:
    print("Это число не подходит!")
    exit()
i = 0
for j in range(2, number // 2 + 1):
    if (number % j == 0):
        i += 1
if i == 0:
    print("Число простое!")
else:
    print("Число составное!")
