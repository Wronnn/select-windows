# -*- coding: utf-8 -*-

# Подбор стабильной Windows для ПК
# Copyright © 2023 Alexey Polyakov. All rights reserved.

# Импорты
import sys

# Главная
print("Подбор стабильной Windows для ПК\nCopyright © 2023 Alexey Polyakov. All rights reserved.\n")
input_ram = input("Сколько у вас оперативной памяти?\n1) 1 ГБ и меньше\n2) 2 ГБ\n3) 3 ГБ и больше\nВведите ваш ответ: ")
print()
cpu_cores = input("Сколько ядер в вашем процессоре?\n1) 1 ядро\n2) 2 ядра и больше\nВведите ваш ответ: ")


# Память
if input_ram == "1": ram = "1 ГБ и меньше"
elif input_ram == "2": ram = "2 ГБ"
elif input_ram == "3": ram = "3 ГБ и больше"
else:
    print("\n\nВы ввели неправильную цифру оперативной памяти!")
    input("\n\nНажмите Enter, чтобы выйти.")
    sys.exit(0)
    
# Кол-во ядер процессора
if cpu_cores == "1": core = "1 ядро"
elif cpu_cores == "2": core = "2 ядра и больше"
else:
    print("\n\nВы ввели неправильную цифру ядер процессора!")
    input("\n\nНажмите Enter, чтобы выйти.")
    sys.exit(0)
    
# Сбор данных
sur = [ram, core]

# Результаты
if sur == ["1 ГБ и меньше", "1 ядро"]: print("\n\nВам стоит установить на ваш ПК: Windows XP Professional / Home Edition x32")
elif sur == ["2 ГБ", "1 ядро"]: print("\n\nВам стоит установить на ваш ПК: Windows XP Professional / Home Edition x32")
elif sur == ["3 ГБ и больше", "1 ядро"]: print("\n\nВам стоит установить на ваш ПК: Windows XP Professional / Home Edition x32 или Windows 7 Максимальная / Профессиональная x32")

elif sur == ["1 ГБ и меньше", "2 ядра и больше"]: print("\n\nВам стоит установить на ваш ПК: Windows XP Professional / Home Edition x32")
elif sur == ["2 ГБ", "2 ядра и больше"]: print("\n\nВам стоит установить на ваш ПК: Windows 7 Максимальная / Профессиональная или Windows 10 Pro / Home x32")
elif sur == ["3 ГБ и больше", "2 ядра и больше"]: print("\n\nВам стоит установить на ваш ПК: Windows 7 Максимальная / Профессиональная или Windows 10 Pro / Home x64")

# Конец
input("\n\nНажмите Enter, чтобы выйти.")
