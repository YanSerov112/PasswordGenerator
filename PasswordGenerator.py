import random

PWNAns = []
PWCS = random.randint(0,3)


print("Генератор паролей v. 1.2")
PWNTall = input("Введите нужное количество символов которое нужно в вашем пароле (цифра):")
PWLTall = input("Введите нужное количество букв которое нужно в вашем пароле (цифра):")

for PWN in range(int(PWNTall)):
    PWN = random.randint(0,9)
    PWNAns.append(PWN)

PWL = random.randint(0,9)
if PWCS == 0:
    PWCS = "-"
elif PWCS == 1:
    PWCS = "_"
elif PWCS == 2:
    PWCS = "!"
elif PWCS == 3:
    PWCS = "@"

for PWN in range(int(PWLTall)):
    PWN = random.randint(0,9)
    if PWL == 0:
        PWL = "F"
    elif PWL == 1:
        PWL = "I"
    elif PWL == 2:
        PWL = "p"
    elif PWL == 3:
        PWL = "J"
    elif PWL == 4:
        PWL = "Q"
    elif PWL == 5:
        PWL = "u"
    elif PWL == 6:
        PWL = "W"
    elif PWL == 7:
        PWL = "x"
    elif PWL == 8:
        PWL = "Y"
    elif PWL == 9:
        PWL = "z"
    PWNAns.insert(random.randint(0, int(PWNTall)), PWL)





PWNAns.insert(random.randint(1, int(PWNTall) - 2), PWCS)
PWNANS = ''.join(map(str, PWNAns))

print("Ваш пароль: " + PWNANS)
input()