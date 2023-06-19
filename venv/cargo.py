things = {"вода" : 3, "еда" : 2, "спальный мешок" : 1, "Аптечка"  : 0.5, "одежда" : 3, "средства гигиены" : 0.5, "посуда" : 2, "топливо" : 2} #Значения указаны в кг или литрах.
res_things = {}
cargo_max = 10
temp = 0
for item, value in things.items():
    if temp < cargo_max:
        #print(temp)
        temp = temp + value
        #print(temp)
        res_things[item] = value
for res_item, res_value in res_things.items():
    print(f"Рюкзак укомплектован {res_item} с массой {res_value} ")


    
