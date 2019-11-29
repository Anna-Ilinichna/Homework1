# while True:
#     user_say = input('Как дела?: ')
#     if user_say == 'Хорошо':
#         print('Отлично')
#         break
#     else:   
#         print('Пока!')
user_say=input('Как дела?:')
user_ask=input('Что делашь?:')
try:
    while True:
        if user_say == 'Хорошо' and user_ask == 'Программирую':
            print('Отлично')     
        else: 
            try:
            except(KeyboardInterrupt):
                print('Пока!')
                break