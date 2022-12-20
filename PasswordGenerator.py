import random

PWNAns = []
PWCS = random.randint(0,3)

print("Генератор паролей v. 1.1")
PWNTall = input("Введите нужное количество символов которое нужно в вашем пароле (цифра):")

for PWN in range(int(PWNTall)):
        PWN = random.randint(0,9)
        PWNAns.append(PWN)

if PWCS == 0:
    PWCS = "-"
elif PWCS == 1:
    PWCS = "_"
elif PWCS == 2:
    PWCS = "!"
elif PWCS == 3:
    PWCS = "@"

PWNAns.insert(random.randint(1, int(PWNTall) - 2), PWCS)
PWNANS = ''.join(map(str, PWNAns))

print("Ваш пароль: " + PWNANS)
input()