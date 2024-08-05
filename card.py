class card():
    def __init__(self, name, type, effect, skill, introduce):
        self.name = name
        self.type = type
        self.effect = effect
        self.skill = skill
        self.introduce = introduce


class effect():
    def __init__(self, name, dp, art, lan, mem):
        self.name = name
        self.dp = dp
        self.art = art
        self.lan = lan
        self.mem = mem


class skill():
    def __init__(self, name, sc, so, ma, cs, en, dp):
        self.name = name
        self.sc = sc
        self.so = so
        self.ma = ma
        self.cs = cs
        self.en = en
        self.dp = dp


effects = []
skills = []

cards = []  # [0] -> depressure [1] -> science [2] -> society  [3] -> math  [4] -> chinese  [5] -> language

# effect(name, decrease_pressure, logc, art, lan, mem)
# skill(name, science, society, math, chinese, english, depressure)
