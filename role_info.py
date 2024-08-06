# 擷取history
from role_plot import role_introduce
# 定義角色數值<class>


class Role:
    def __init__(self, name, sc, so, ma, cs, en, dp, group, subject, introduce):
        # role name 角色名稱
        self.name = name
        # role information 角色基本數值
        self.science = sc
        self.society = so
        self.math = ma
        self.chinese = cs
        self.english = en
        self.dePressure = dp
        self.introduce = introduce
        self.pressure = 0
        # 角色資質
        self.group = group  # group= science / social
        self.subject = subject  # subject = science/social/ch/en/math

    # def __str__(self):
    #    return (f'Name: {self.name}, Science: {self.science}, Society: {self.society}, '
    #            f'Math: {self.math}, Chinese: {
    #                self.chinese}, English: {self.english}, '
    #            f'Pressure: {self.pressure}, DePressure: {self.dePressure}, '
    #            f'Group: {self.group}, Subject: {self.subject}')


# 輸出值,各角色初始的數值
roles = [
    Role("如月 花子", 60, 50, 130, 75, 72, 83,
         "science", "math", role_introduce['如月 花子']),
    Role("蘇我 美月", 54, 125, 45, 80, 76, 90,
         "social", "social", role_introduce['蘇我 美月']),
    Role("廖 優柰", 57, 65, 61, 75, 62, 150,
         "science", "cs", role_introduce['廖 優奈']),
    Role("住野 由美子", 45, 87, 38, 160, 69, 80,
         "social", "cs", role_introduce['住野 由美子']),
    Role("真鍋 香繪", 130, 57, 70, 71, 66, 0,
         "science", "sc", role_introduce['真鍋 香繪']),
    Role("小柳 詩", 45, 80, 55, 70, 71, 120,
         "social", "en", role_introduce['小柳 詩'])
]
