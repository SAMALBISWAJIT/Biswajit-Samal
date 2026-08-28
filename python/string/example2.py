'''
ip = 'a4b3c2'
op = 'aaaabbbcc'
'''
ip = 'a4b3c2'
lst = []
lst_new = []

for i in ip:
    if i.isalpha():
        lst.append(i)
    if i.isdigit():
        lst_new.append(int(i))

print(lst)
print(lst_new)
lst_final = []
j = 0
for i in lst:
    val = i*lst_new[j]
    lst_final.append(val)
    j = j+1
    print(val)

print(''.join(lst_final))
    