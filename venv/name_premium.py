name_ = ["Иван", "Петр", "Михаил", "Виктор"]
bid = [10000, 15000, 20000, 30000]
premium = ['10.25%', '10.25%', '10.25%', '10.25%']
if len(name_) == len(bid) == len(premium):
    def name_prem(name_, bid, premium):
        for i in range(len(premium)):
            for item in premium:
                item = str(item).replace('%', '')
                premium[i] = float(item)
        # print(premium)
        # res_premium = set([it / 100 * it2  for it in bid for it2 in premium ])
        # res_premium = list(premium)
        # генератор множества
        res_set = {it / 100 * it2 for it in bid for it2 in premium}
        # генератор словаря
        res_dict = {
            res_key: res_value for res_key in name_ for res_value in res_set}
        # print(res_set)
        print(res_dict)
        # print(res_premium)
else:
    print("Не корректный ввод!")


name_prem(name_, bid, premium) 
