x = [i for i in range(20) if i % 2 == 0]

print(x)

x = []
for i in range(20):
    if i % 2 == 0:
        x += [i]

a = list('Hello World')
print(a)

a.sort(key=str.lower, reverse=True)
print(a)



str1 = 'ERTETER'
str2 = 'gdfgert'

str3 = str1 + str2
lst1 = []

for i in str3:
    if i in lst1:
        continue
    else:
        lst1.append(i)

print(lst1)

print(str3)

y = list(str3)
print(y)

for i in y:
    print(i)

del y[10:13]
print(y)

y.remove('E')
print(y)
y = str(y)
print(type(y))
y1 = ''
x1 = y1.join([str1, str2])
print(x1)
print(type(x1))


str4 = f'{str1}, {str2}, {str3}'
print(str4)
