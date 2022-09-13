# Задание 1
# a, b, c = int(input()), int(input()), int(input())
# print(a * b**(c-1))


# Задание 2
# a = int(input())
# if (0 < a // 1000 <= 9) and (a % 7 == 0 or a % 17 == 0):
#     print('YES')
# else:
#     print('NO')


# Задание 3
# lst = [int(el) for el in input().split(' ')]
# for el in lst:
# 	if el % 2 != 0:
# 		print('No')
# 		break
# else:
# 	print('Yes')


# Задание 4
# a, b = int(input()), int(input())
# for i in range(a, b + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(j)


# Задание 5
# s = str(input())
# if s == s[::-1]:
#     print('YES')
# else:
#     print('NO')


# Задание 6

# strr = str(input()).split()
# lst = []
# for el in strr:
#     lst.append(int(el))
# lst.sort()
# print(*lst)
# lst.sort(reverse=True)
# print(*lst)


# Задание 7
# def get_factors(num):
#     lst = []
#     for el in range(1, num + 1):
#         if num % el == 0:
#             lst.append(el)
#     return lst
#     pass
#
#
# n = int(input())
#
# print(get_factors(n))
