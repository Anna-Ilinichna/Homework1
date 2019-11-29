def comparison(text1, text2):
    if type(text1) != str:
        return 0
    elif type(text2) != str:
        return 0
    elif text1 == text2:
        return 1
    elif text1 != text2 and len(text1)>len(text2):
        return 2
    elif text1 != text2 and text2 == 'learn':
        return 3       
    else:
        return f'{text1} {text2}'
print(comparison(text1=input("Введите текст1:"), text2=input("Введите текст2:")))