# from random import randint

# def game_play() -> None:
#     """basic logic"""
#     person = randint(0, 1)
#     flag = 1
#     while flag:
#         print(f'Конфет на столе: {candies}')
#         if mode == '1':
#             if person:
#                 num_take = human(person)
#                 if num_take > 28 or num_take < 0:
#                     num_take = AMT_MAX 
#             else:
#                 num_take = ai_player(candies)
#         else:
#             num_take = human(person)
#             if num_take > 28 or num_take < 0:
#                 num_take = AMT_MAX

#         if candies <= 28:
#             print(f'{names[person]} забирает {candies} конфет.')
#         else:
#             print(f'{names[person]} берёт {num_take} конфет.')
#         candies -= num_take
#         if candies <= 0:
#             print(f'{names[person]} победил')
#             flag = 0
#         person = (person + 1) % 2


# def ai_player(candies: int) -> int:
#     """primitive AI"""
#     if candies < 28:
#         return candies
#     elif candies - 28 > 1 and candies < 28 * 2:
#         return candies - 27
#     else:
#         return 28


# def human(pers: int) -> int:
#     """human capture"""
#     global names
#     return int(input(f'Сколько конфет берёте (0 min, 28 max), {names[pers]}? '))


# # def intro():
# #     print(
# #         '''
# #         Играем в конфеты. 
# #         Полиси: можно взять от 0 до 28 штук.
# #         Если взять меньше 0 (интересный вариант...) или больше 28,
# #         считается что взял 28. Поехали.    
# #     '''
#         # )

#     # flag_0 = 1
#     # global mode
#     # global names
#     #      #= input('Играем с компьютером или на двоих? (1/2/exit): ')
#     #     if mode == 'exit':
#     #         print('Выход')
#     #         raise SystemExit
#     #     elif mode not in ('1', '2'):
#     #         print('Ошибка ввода.')
#     #     else:
#     #         flag_0 = 0

#     # if mode == '1':
#     #     names = ('An artificial one', input('Введите имя: '))
#     # else:
#     #     names = (input('Введите имя 1-го игрока: '), input('Введите имя 2-го игрока: '))

#     game_play()


# intro()
