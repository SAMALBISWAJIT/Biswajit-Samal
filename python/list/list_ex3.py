'''
find the 2nd largest number from a given values
ip = [10,11,19,20,1,2,3]
op = [19]
'''

ip = [10, 11, 19, 20, 1, 2, 3]

ip.sort(reverse=True)
j = 0
for i in ip:
    j += 1
    if j == 2:
        print(f'The index value is {j}, actual value is {i}')
        break