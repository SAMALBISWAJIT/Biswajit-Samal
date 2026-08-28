'''
WAP to remove the duplicate char from the given input
ip = 'abcdabbcdabbbcccddeeeef'
op = 'abcdef'
'''

ip = 'abcdabbcdabbbcccddeeeef'
lst = []

for i in ip:
    if i not in lst:
        lst.append(i)

print(lst)