class card():
    def __init__(self, name, type, effect, skill, introduce):
        self.name = name
        self.type = type
        self.effect = effect
        self.skill = skill
        self.introduce = introduce


class effect():
    def __init__(self, name):
        self.name = name


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

# sample:
# 【test1】

# 類型:數學卡【情誼條滿時，當次培育回合的數學增加值boost 1.3倍】

# 技能: 抗壓技-在數學考試中，當回合的考試失敗率降低65%

# 介紹: 測試…測試….test1
