# 擷取history
import role_story  # temp

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

# 各角色自我介紹


# 如月 花子
introduce_1 = ""
# 蘇我 美月
introduce_2 = ""
# 廖 優奈
introduce_3 = ""
# 住野 由美子
introduce_4 = ""
# 真鍋 香繪
introduce_5 = "金髮辣妹,對理科,特別是化學,抱有強烈興致,個性十分外向,社交牛逼,喜歡傳XX決,與廖 優奈經常熬夜爬牌位。好甜食,螞蟻人；對社會科毫無關心,本人說「社會科不都是常識嗎?」,但其實只是對於背東西很不在行。"
# 小柳 詩
introduce_6 = "身高159.6的銀白長髮的日本女孩,個性活潑、溫柔,是個十足的戲精,有不把苦說出口的壞毛病。喜歡吃甜食,特別是抹茶厥餅,喜歡音樂,幾乎什麼都聽,甚至是如月花子愛聽的至鬱戲音樂。有極高的音樂、演藝天賦,但本人似乎沒意識到這點。"

# 輸出值,各角色初始的數值
roles = [
    Role("如月 花子", 0, 0, 0, 0, 0, 0, "none", "none", introduce_1),
    Role("蘇我 美月", 0, 0, 0, 0, 0, 0, "none", "none", introduce_2),
    Role("廖 優柰", 0, 0, 0, 0, 0, 0, "none", "none", introduce_3),
    Role("住野 由美子", 0, 0, 0, 0, 0, 0, "none", "none", introduce_4),
    Role("真鍋 香繪", 130, 57, 70, 71, 66, 0, "science", "sc", introduce_5),
    Role("小柳 詩", 45, 80, 55, 70, 71, 120, "social", "en", introduce_6)
]
