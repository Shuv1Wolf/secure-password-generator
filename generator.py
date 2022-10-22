from random import choice

def count():
    n = input("Сколько вам нужно паролей? Укажите цифру >>> ")
    print()
    while n.isdigit() == False:
        print('Попросили же вроде по русски, что нужна цифра. Исправься.')
        n = input("Сколько вам нужно паролей? Укажите цифру >>> ")
        print()
    return int(n)

def long():
    l = input("Введите длину пароля. Укажите цифру >>> ")
    print()
    while l.isdigit() == False:
        print('Попросили же вроде по русски, что нужна цифра. Исправься.')
        l = input("Введите длину пароля. Укажите цифру >>> ")
        print()
    return int(l)

def is_number():
    print('Нужны ли в пароле цифры 0123456789?')
    is_n = input('Напишите "да" или "нет" >>> ')
    print()
    while is_n.lower().strip() not in ['да', 'нет']:
        print("Нужно ввести 'да' или 'нет'")
        print('Нужны ли в пароле цифры 0123456789?')
        is_n = input('Напишите "да" или "нет" >>> ')
        print()
    return is_n

def is_upper():
    print('Нужны ли в пароле заглавные буквы?')
    is_up = input('Напишите "да" или "нет" >>> ')
    print()
    while is_up.lower().strip() not in ['да', 'нет']:
        print("Нужно ввести 'да' или 'нет'")
        print('Нужны ли в пароле заглавные буквы?')
        is_up = input('Напишите "да" или "нет" >>> ')
        print()
    return is_up

def is_lower():
    print('Нужны ли в пароле строчный буквы?')
    is_lw = input('Напишите "да" или "нет" >>> ')
    print()
    while is_lw.lower().strip() not in ['да', 'нет']:
        print("Нужно ввести 'да' или 'нет'")
        print('Нужны ли в пароле строчные буквы?')
        is_lw = input('Напишите "да" или "нет" >>> ')
        print()
    return is_lw

def is_symbol():
    print('Нужны ли в пароле символы "!#$%&*+-=?@^_?"?')
    is_smb = input('Напишите "да" или "нет" >>> ')
    print()
    while is_smb.lower().strip() not in ['да', 'нет']:
        print("Нужно ввести 'да' или 'нет'")
        print('Нужны ли в пароле символы "!#$%&*+-=?@^_?"?')
        is_smb = input('Напишите "да" или "нет" >>> ')
        print()
    return is_smb

def is_ambiguous():
    print('Будут ли в пароле неоднозначные символы "il1Lo0O"?')
    amb = input('Напишите "да" или "нет" >>> ')
    print()
    while amb.lower().strip() not in ['да', 'нет']:
        print("Нужно ввести 'да' или 'нет'")
        print('Будут ли в пароле неоднозначные символы "il1Lo0O"?')
        amb = input('Напишите "да" или "нет" >>> ')
        print()
    return amb

def gen_chairs():
    chars = ''
    if is_n == 'да':
        chars += '0123456789'
    if is_up == 'да':
        chars += 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    if is_lw == 'да':
        chars += 'abcdefghijklmnopqrstuvwxyz'
    if is_smb == 'да':
        chars += '!#$%&*+-=?@^_'
    if amb == 'нет':
        for c in 'il1Lo0O':
            chars.replace(c, '')  # заменить символ на пустой текст
    return chars

def build_password():
    for i in range(n):
        password = []
        for i in range(l):
            password.append(choice(chars))
        print(''.join(password))

n = count()
l = long()
is_n = is_number()
is_up = is_upper()
is_lw = is_lower()
is_smb = is_symbol()
amb = is_ambiguous()
chars = gen_chairs()
build_password()

