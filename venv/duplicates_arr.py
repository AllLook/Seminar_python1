my_list = [2, 4, 6, 8, 13, 16, 2, 6, 2, 'w', 's', 'w', 16]
res_list = []
for item in my_list:
    res = my_list.count(item)
    if res == 2:
        res_list.append(item)
res_list = set(res_list)  # .list(res_list) так почему нельзя?
res_list = list(res_list)
print(res_list)
