my_dict = {'Nikolai':'13.10.2000','Anna':'10.04.2002'}
print(my_dict)
print(my_dict["Nikolai"])
print(my_dict.get("Olga"))
my_dict.update({'a':'1',
               'b':'2'})
print(my_dict)
x = my_dict.pop('a')
print(x)
print(my_dict)
my_set = {1,2,3,1,2,3}
print(my_set)
my_set.add(4)
my_set.add(5)
my_set.remove(1)
print(my_set)