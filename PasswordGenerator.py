import random

PWNAns = []

print("Генератор паролей v. 1.1")
PWNTall = input("Введите нужное количество символов которое нужно в вашем пароле (цифра):")

for PWN in range(int(PWNTall)):
        PWN = random.randint(0,9)
        PWNAns.append(PWN)

PWNANS = ''.join(map(str, PWNAns))


print("Ваш пароль: " + PWNANS)
input()