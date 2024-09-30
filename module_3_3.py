def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
#print_params(a, b)
#print_params(a)
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
values_list = [1, 1.0,'one']
values_dict = {'a':1, 'b':1.0, 'c':'one'}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [1, 1.0]
print_params(*values_list_2, 42)