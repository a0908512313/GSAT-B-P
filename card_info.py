class card():
    def __init__(self, name, intro, effect, skill):
        self.name = name
        self.introduce = intro
        self.effect = effect
        self.skill = skill


class effect():
    def __init__(self, name, level):
        # logic -> sc art -> cn lan -> en mem -> so
        c1 = ['logic', 'art', 'lan', 'mem']
        e1 = [0.01, 0.03, 0.05]
        e2 = [-1, -3, -5]
        self.name = name
        for i in c1:
            if name == i:
                self.intro = e1[level - 1]
                self.eff = i
            else:
                self.intro = e2[level - 1]
        self.level = level


class skill():
    def __init__(self, name, intro):
        self.name = name
        self.intro = intro


cards = [
    card("math_card", None, [effect('邏輯I', 1), effect('減壓II', 2)], skill(
        ['學科技a', '競賽類型技a'], ['在計算時手感變好', '變得稍微擅長數學競賽']))
]
