def begin_menu():
    print('1 - Посмотреть контакты на экране в формате txt')
    print('2 - Сохранить контакты в формате txt')
    print('3 - Сохранить контакты в формате csv')
    print('4 - Посмотреть контакты на экране в формате csv')
    print('5 - Сохранить контакты из формата txt в csv')
    print('6 - Сохранить контакты из формата csv в txt')
    return input('Введите цифру: ')


def show_result(res):
    for i, row in enumerate(res):
        print(i, ' '.join(row))