temp = input("Введите путь к файлу:").split('\\')
print(temp)


def road_split(temp):
    #    for item  in  ['\\', '.']: // почему так нельзя?ошибка что у листа нет split,но я же пытаюсь реребором применить к строке
    #         temp = temp.split(item)
    *a, b = temp
    b = str(b).split('.')
    res = (a, b[0], b[1])
    print(res)


road_split(temp) 
