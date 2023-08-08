from random import randint
# def print_operation_table(operation, num):
#     for row in range(1, num+1):
#         for colm in range(1, num+1):
#             print(operation(row, colm), end='\t')
#         print()
#
#
# print_operation_table(lambda x, y: x**y, 6)

# simpl_list = ['кот', 'ток', 'ом', 'от', 'кто', 'мат', 'хор', 'там', 'атм', 'кор', 'ор', 'рок', 'пот']
# shake_list = []
# for i in range(0, len(simpl_list)):
#     j = randint(0, len(simpl_list)-1)
#     el = simpl_list[j]
#     simpl_list.pop(j)
#     simpl_list.append(el)
# shake_list = simpl_list
# temp_list = []
# res_list = []
# for i in range(0, len(shake_list)):
#     for j in range(0, len(shake_list)):
#         if len(shake_list[i]) == len(shake_list[j]):
#             count = 0
#             for k in shake_list[i]:
#                 if k in shake_list[j]:
#                     count +=1
#                     if count == len(shake_list[i]):
#                        temp_list.append(shake_list[j])
#                 else:
#                     break
#         else:
#             j+=1
#     if temp_list not in res_list:
#         res_list.append(temp_list)
#     temp_list = []
# print(res_list)

with open('numbers.txt', 'r') as file:
    some_list = []
    while True:
        line = file.readline()
        if line == '':
            break
        some_list.append(line)
print(some_list)
symbol = '!@#$%^&*()_+-=/?><.:;\ n,'
number = ''
numbers = []
for i in range(0, len(some_list)):
    for num in some_list[i]:
        if num not in symbol:
            number +=num
        else:
            numbers.append(number)
            number = ''
print(numbers)