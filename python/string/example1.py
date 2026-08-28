'''
ip = 'B4A1D3'
op = 'ABD123'
'''

ip = 'B4A1D3'
lst = []
lst_digit = []
lst_new = []
for i in ip:
    if i.isalpha():
        lst.append(i)
    elif i.isdigit():
        lst_digit.append(i)
lst.sort()
lst_digit.sort()
lst_new = lst+lst_digit
print(lst)
print(lst_digit)
print(''.join(lst_new))