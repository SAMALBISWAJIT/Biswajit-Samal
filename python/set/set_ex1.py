'''
find out the vowels present in a string
'''

s = input("enter any string : ")
vw = {'a','e','i','o','u'}
sv = set()
for i in s:
    sv.add(i)
print(sv.intersection(vw))