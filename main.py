from role_init import roles
from card_info import *
from card_calcu import *
import keyboard


def init():
    isFirst = True
    global skill_point, pressure
    skill_point, pressure = 0, 0
    print(" -----------------------------------")
    print(" |~~~ welcome to GSAT cultivate ~~~| ")
    print(" -----------------------------------")
    isFirst = False
    print("please choose mod")
    mode = input("(1)cultivate (2)display role : ")
    if mode == "1":
        cultivate()
    elif mode == "2":
        print()
        role_display(len(roles), True)
        print()
        print('Press any key to go back : ')
        while True:
            if bool(keyboard.read_key()):
                homePage()


def homePage():
    print()
    print("please choose mode")
    mode = input("(1)cultivate (2)display role\nSelect mode : ")
    if mode == "1":
        cultivate()
    elif mode == "2":
        print()
        role_display(len(roles), True)
        print()
        print('Press any key to go back : ')
        while True:
            if bool(keyboard.read_key()):
                homePage()


def cultivate():  # 培育
    role = choose_role()
    print()
    card = choose_card()
    # root attributes changes
    card_effect(roles[role - 1], cards[card[0] - 1][card[1] - 1].effect)


def choose_role():  # 選擇角色
    for i in range(len(roles)):
        print(f'({i+1}) {roles[i].name}')
    name_sel = int(input('enter num to select role : '))
    if name_sel > len(roles):
        print()
        print('! input number out of range !')
        print('Please enter an available number!!!')
        print()
        choose_role()
    else:
        print()
        mode = int(
            input(f'Current role : {roles[name_sel].name}\n(1) to show role detail\n(2) to comfirm selecte\n(3) to reselect role\nEnter to select mode : '))
        if mode == 1:
            role_display(name_sel, False)
            print()
            temp = int(
                input("(1) to comfirm select\n(2) to reselect role\nEnter number to select : "))
            if temp == 1:
                print()
                return name_sel
            elif temp == 2:
                print()
                print('RESELECTE ROLE')
                print()
                choose_role()
            else:
                print()
                print('! input number out of range !')
                print('Please enter an available number!!!')
                pass

        elif mode == 2:
            return name_sel

        elif mode == 3:
            print()
            print('RESELECTE ROLE')
            print()
            choose_role()
        else:
            print()
            print('! input number out of range !')
            print('Please enter an available number!!!')
            print()
            choose_role()


def role_display(n, all=False):  # 觀看擁有角色
    if all:
        for i in range(len(roles)):
            print(f'({i+1}) {roles[i].name}')
            print('introduce  :')
            print(roles[i].introduce)
            print(f'science    : {roles[i].science}')
            print(f'society    : {roles[i].society}')
            print(f'math       : {roles[i].math}')
            print(f'chinese    : {roles[i].chinese}')
            print(f'english    : {roles[i].english}')
            print(f'pressure   : {roles[i].pressure}')
            print(f'dePressure : {roles[i].dePressure}')
            print(f'group      : {roles[i].group}')
            print(f'subject    : {roles[i].subject}')
            print()
    else:
        print(f'name       : {roles[n - 1].name}')
        print('introduce  :')
        print(roles[n - 1].introduce)
        print(f'science    : {roles[n - 1].science}')
        print(f'society    : {roles[n - 1].society}')
        print(f'math       : {roles[n - 1].math}')
        print(f'chinese    : {roles[n - 1].chinese}')
        print(f'english    : {roles[n - 1].english}')
        print(f'pressure   : {roles[n - 1].pressure}')
        print(f'dePressure : {roles[n - 1].dePressure}')
        print(f'group      : {roles[n - 1].group}')
        print(f'subject    : {roles[n - 1].subject}')


def choose_card():  # 選擇卡片
    category = int(input(
        '(1) Depressure Card\n(2) Science Card\n(3) Society Card\n(4) Math Card\n(5) Chinese Card(6) English Card\nEnter number to list corresponding category : '))
    if 1 <= category <= len(cards):
        card_display(category, None)  # display category cards
        card_sel = int(input('enter number to select card : '))
        if 0 <= card_sel > len[cards[category - 1]]:
            print()
            print('! input number out of range !')
            print('Please enter an available number!!!')
            print()
            choose_card()
        else:
            mode = int(
                input(f'Current role : {cards[category - 1][card_sel - 1].name}\n(1) to show role detail\n(2) to comfirm selecte\n(3) to reselect role\nEnter to select mode : '))
        if mode == 1:
            card_display(category, card_sel)
            print()
            temp = int(
                input("(1) to comfirm select\n(2) to reselect role\nEnter number to select : "))
            if temp == 1:
                print()
                return category, card_sel
            elif temp == 2:
                print()
                print('RESELECTE CARD')
                print()
                choose_card()
            else:
                print()
                print('! input number out of range !')
                print('Please enter an available number!!!')
                pass
        elif mode == 2:
            return category, card_sel
        elif mode == 3:
            print()
            print('RESELECTE CARD')
            print()
            choose_role()
        else:
            print()
            print('! input number out of range !')
            print('Please enter an available number!!!')
            print()
            choose_role()


def card_display(category, n):  # 觀看擁有卡片
    if n:
        temp = cards[category - 1][n - 1]
        print(f'name      : {temp.name}')
        print(f'introduce : {temp.intro}')
        for i in range(len(temp.effect)):
            print(f'effect {i+1} name : {temp.effect[i].name}')
    else:
        for i in range(len(cards[category - 1])):
            print(f'({i+1}) {cards[category - 1][i].name}')


def cultivated_display():  # 觀看歷史培育角色
    pass


init()
