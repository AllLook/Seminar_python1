# Вроде все условия задачи))
import sys
from datetime import datetime
SUM_ACTION = 50
res_amount = 0
operation_sheet = []


def withdrawal(SUM_ACTION):
    global res_amount 
    if res_amount < SUM_ACTION:
        print("Недостаточно средств!")
        sys.exit()

    else: 
        res_amount = res_amount - SUM_ACTION
        percent = SUM_ACTION // 100 * 1.5
        if percent < 30:
            percent = 30
        elif percent > 600:
            percent = 600
        res_amount = res_amount - percent
    print(f"остаток по счету: {res_amount}")

    operation_sheet.append(
        f"{datetime.now()} Текущая операция сняти на сумму {SUM_ACTION} со снятием процента {percent}, остаток по счету {res_amount} ")
    return res_amount


def top_up(SUM_ACTION):
    global res_amount
    res_amount = res_amount + SUM_ACTION
    percent = SUM_ACTION // 100 * 1.5
    if percent < 30:
        percent = 30
    elif percent > 600:
        percent = 600
    res_amount = res_amount - percent
    print(res_amount)
    print(f"остаток по счету: {res_amount}")
    operation_sheet.append(
        f"{datetime.now()} Текущая операция снятия на сумму {SUM_ACTION} со снятием процента {percent}, остаток по счету {res_amount} ")
    return res_amount


run = True
while run:
    if res_amount > 5000000:
        percent = res_amount // 100 * 10
        res_amount -= percent
        print(
            f"Вычтен налог на богатство в размере 10% ваш остаток {res_amount}")
    action = input(
        "Введите действие: пополнить,снять,выйти,стоп\nчтобы вывести список операций:список \n").lower()
    if action == "снять":
        withdrawal(SUM_ACTION)
    elif action == "пополнить":
        top_up(SUM_ACTION)
    elif action == "список":
        print(operation_sheet)
    else:
        action == "стоп"
        run = False 
        print("До свидания!")
