# стратегия печатать на экран
def console_writer(info):
    print(info)

# стратегия выводить в файл
def file_writer(info):
    with open('log.txt', 'a') as file:
        file.write(info + '\n')

def client(writer):
    writer('Hello world!')

# пользователь выбирает стратегию
if input('Write to file? [Y/N]') == 'Y':
    client(writer=file_writer)
else:
    client(writer=console_writer)
