class card():
    def __init__(self, name, intro, effect, skill):
        self.name = name
        self.introduce = intro
        self.effect = effect
        self.skill = skill


class effect():
    def __init__(self, name, intro, level):
        self.name = name
        self.intro = intro
        self.level = level


class skill():
    def __init__(self, name, intro):
        self.name = name
        self.intro = intro


cards = [
    card("math_card", None, effect(None, None, None), skill(
        ['學科技a', '競賽類型技a'], ['在計算時手感變好', '變得稍微擅長數學競賽']))
]
