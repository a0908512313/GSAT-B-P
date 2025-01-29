import json

class Role:
    def __init__(self, name, sc, so, ma, cs, en, dp, group, subject, introduce):
        self.name = name
        self.science = sc
        self.society = so
        self.math = ma
        self.chinese = cs
        self.english = en
        self.dePressure = dp
        self.introduce = introduce
        self.pressure = 0
        self.group = group  # group= science / social
        self.subject = subject  # subject = science/social/ch/en/math

    def __str__(self):
       return (f'Name: {self.name}, Science: {self.science}, Society: {self.society}, '
               f'Math: {self.math}, Chinese: {
                   self.chinese}, English: {self.english}, '
               f'Pressure: {self.pressure}, DePressure: {self.dePressure}, '
               f'Group: {self.group}, Subject: {self.subject}')

# Load role info from JSON file
roles = []
with open("role_info.json", "r", encoding="utf-8") as file:
    data = json.load(file)

for role_data in data:
    role = Role(
        role_data["name"],
        role_data["subject value"]["sc"],
        role_data["subject value"]["so"],
        role_data["subject value"]["ma"],
        role_data["subject value"]["cs"],
        role_data["subject value"]["en"],
        role_data["subject value"]["dp"],
        role_data["group"],
        role_data["subject"],
        role_data["history"]["introduce"]
    )
    roles.append(role)

# Print all roles
for role in roles:
    print(role)
