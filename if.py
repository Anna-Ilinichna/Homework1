def profession(age):
    if age < 7:
        return 'Иди в детский сад'
    elif 7 <= age <=18:
        return 'Иди в школу'
    elif 18 < age <=23:
        return 'Иди в институт'
    else: 
        return 'Иди работай'
print(profession(age=int(input("Введите свой возраст:"))))