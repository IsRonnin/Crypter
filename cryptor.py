CHANGE = 0 # сдвиг

str_to_char = lambda string: [ord(i)+CHANGE for i in string] # функция перевода в список 
char_to_str = lambda char_list, string='': string.join([chr(i-CHANGE) for i in char_list]) # функция перевода из списка в строку
s_msg = 'код для проверки'


print((str_to_char(s_msg)))

msg = [1082, 1086, 1076, 32, 1076, 1083, 1103, 32, 1087, 1088, 1086, 1074, 1077, 1088, 1082, 1080]
print(char_to_str(msg))

