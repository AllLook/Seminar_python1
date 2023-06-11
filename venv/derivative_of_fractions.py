#СЛОЖНОЕ И БЕСПОЛЕЗНОЕ ЗАДАНИЕ.ЕСТЬ ВТРОЕННЫЙ МЕТОД.НО ВСЕ РАБОТАЕТ АНАЛОГИЧНО FRACTIONS

import math
frac_tion1 = input("Введите первую дробь:").split("/")
numerator1 = int(frac_tion1[0])#первую часть дроби приводим к числу как первый числитель
denominator1 = int(frac_tion1[1])#вторую часть дроби приводим к числу как первый знаменатель
frac_tion2 = input("Введите вторую дробь:").split("/")
numerator2 = int(frac_tion2[0])#первую часть дроби приводим к числу как второй числитель
denominator2 = int(frac_tion2[1])#вторую часть дроби приводим к числу как второй знаменатель
#print(denominator2)
def sum_fractions(denominator1, denominator2, numerator1, numerator2): #передаем введенные данные для вычисления суммы если знаменатель разный
    if denominator1 < denominator2 or denominator2 < denominator1: #если знаменатели разные
        def res_denominator(denominator1, denominator2): #вычисляем общий знаменатель
            num = denominator1 * denominator2
            while denominator1 !=0 and denominator2 != 0:
                if denominator1 > denominator2:
                    denominator1 %= denominator2
                else:
                    denominator2 %= denominator1
            return num // (denominator1 + denominator2)
        #print(denominator2)
        #print(res_denominator(denominator1, denominator2))
        if denominator1 < res_denominator(denominator1, denominator2) or denominator1 < res_denominator(denominator1, denominator2):#если начальные знаменатели не равны общему
            num2 = res_denominator(denominator1, denominator2) // denominator1 #вычисляем число с помощью которого привести первый числитель
            numerator1 = numerator1 * num2 #приводим первый числитель
            #print(numerator1)
            num3 = res_denominator(denominator1, denominator2) // denominator2 #вычисляем число с помощью которого привести второй числитель
            numerator2 = numerator2 * num3 #приводим второй числитель
            #print(numerator2)
        print(f"Сумма дробей с разным знаменателем равна {numerator1 + numerator2}/{res_denominator(denominator1, denominator2)}")
    else:
        print(f"Сумма дробей с одинаковым знаменателем равна {numerator1 + numerator2}/{denominator1}")
sum_fractions(denominator1, denominator2, numerator1, numerator2)

work_numerator = numerator1 * numerator2 #числитель перемноженной дроби
work_denominator = denominator1 * denominator2 #числитель перемноженной дроби
result_devider = math.gcd(work_numerator, work_denominator) # общий делитель для сокращения дроби
print(f"Произведение дробей {numerator1 * numerator2 / result_devider}/{denominator1 * denominator2 / result_devider}")