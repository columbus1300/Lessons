calls = 0


def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    count_calls()
    return {len(string), string.upper(), string.lower()}


def is_contains(string, list_to_search):
    count_calls()
    x = 0
    for i in list_to_search:
        string_1 = string.lower()
        i = i.lower()
        if i == string_1:
            x = x + 1
    if x >= 1:
        return True
    else:
        return False


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
