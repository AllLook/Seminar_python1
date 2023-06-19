def fun_key(**kwargs):
    temp_dict = {}
    temp_dict = kwargs
    print(temp_dict)
    res = {}
    for i in range(len(temp_dict)):
        for item,value in temp_dict.items():
            #print(value)
            if value.__hash__ is not None:
                value#то что будет ключем
            else:
               value =  tuple(value)#ошибка TypeError: unhashable type: 'list'   и ",".join(value) и str(*value) и str(value) как тогда приводить к строке?
               #удалось только к кортежу он не изменяем
            res[value] = item
    print(res)
            
 
    
print(fun_key(arg1="Hello",arg2=2,arg3="123",arg4=[1,2,3]))