ips = ('192.168.0.1', '10.0.0.2', '172.16.0.3')
IP = input('Введите IP адресс: ')
for i in ips:
    if IP == i:
        print('Найдено')
        break
else:
    print('Нет в списке.')