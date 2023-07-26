# x = [i for i in range(20) if i % 2 == 0]
# print(x)
#
# x = []
# for i in range(20):
#     if i % 2 == 0:
#         x += [i]

a = 'H HHAAello ERBWorld'
print(a)
b = a.replace(" ", "")
print(b)

b.upper()
c = list(b)
c.sort(reverse=False)
print(c)

converted_list = [str(elem) for elem in c]
listToStr = ''.join(converted_list)

print(listToStr)
print(type(listToStr))
#
# str1 = 'ERTETER'
# str2 = 'gdfgert'
#
# str3 = str1 + str2
# lst1 = []
#
# for i in str3:
#     if i in lst1:
#         continue
#     else:
#         lst1.append(i)
#
# print(lst1)
#
# print(str3)
#
# y = list(str3)
# print(y)
#
# for i in y:
#     print(i)
#
# del y[10:13]
# print(y)
#
# y.remove('E')
# print(y)
# y = str(y)
# print(type(y))
# y1 = ''
# x1 = y1.join([str1, str2])
# print(x1)
# print(type(x1))
#
#
# str4 = f'{str1}, {str2}, {str3}'
# print(str4)
#
# # для примера мастер ветка
# # commit


a = 'RRTTYUJN'
b = set(a)

d = ''
for i in b:
    d = d + i

print(d)
