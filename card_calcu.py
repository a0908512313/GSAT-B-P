from card_info import *


def card_effect(role, card):
    c1 = ['logic', 'art', 'lan', 'mem']
    for i in c1:
        if card.effect.name == i:
            if i == c1[0]:
                role.sc = role.sc * (1 + card.e1[card.effect.level - 1])
            elif i == c1[1]:
                role.cn = role.cn * (1 + card.e1[card.effect.level - 1])
            elif i == c1[2]:
                role.en = role.en * (1 + card.e1[card.effect.level - 1])
            elif i == c1[3]:
                role.so = role.so * (1 + card.e1[card.effect.level - 1])
        else:
            role.dp += card.e2[card.effect.level - 1]
