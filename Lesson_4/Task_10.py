# Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
# Дополнительно сохраняйте все операции поступления и снятия средств в список.

s = 10000
count = 0
RICHLIMIT = 5_000_000
RICHTAX = 0.9
THREEOPERATIONS = 3
BONUSTHREE = 1.03
FREENDERING = 50
COMMISSIONOUTDROW = 0.015
MINLIMIT = 30
MAXLIMIT = 600
operations = []


''' функция пополнения '''
def deposit_account(acc_balance, operation_count, operation_list):
    withdrow = int(input('введиет сумму: '))
    if withdrow % FREENDERING == 0:
        acc_balance += withdrow
        operation_list.append(withdrow)
    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


''' функция снятия '''
def withdraw_account(acc_balance, operation_count, operation_list):
    withdrow = int(input('введиет сумму: '))
    if withdrow % FREENDERING == 0:
        comission = withdrow * COMMISSIONOUTDROW
        if comission < MINLIMIT:
            comission = MINLIMIT
        elif comission > MAXLIMIT:
            comission = MAXLIMIT
        if (comission + withdrow) > acc_balance:
            print('Недостаточно средств на счете')
        else:
            acc_balance -= (comission + withdrow)
            operation_list.append(int(-comission - withdrow))
    print(f'Баланс вашего счета: {acc_balance:.0f}')
    operation_count += 1
    return acc_balance, operation_count, operation_list


''' Цикл банкомат '''
while True:
    if s >= RICHLIMIT:
        s *= RICHTAX
    if count % THREEOPERATIONS == 0 and count != 0:
        s *= BONUSTHREE
        count = 0
    operation = input(f'Для работы с банкоматом выберите действие:\n1 - пополнить\n'
                      f'2 - снять\n3 - выйти\n')
    match operation:
        case '1':
            s, count, operations = deposit_account(s, count, operations)
        case '2':
            s, count, operations = withdraw_account(s, count, operations)
        case '3':
            print(f'Баланс вашего счета: {s:.0f}')
            break
        case _:
            break

print(operations)