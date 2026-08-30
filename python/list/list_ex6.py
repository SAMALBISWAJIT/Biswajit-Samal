'''
Merge 2 List into 1
'''
ip1 = [1,2]
ip2 = [3,4]

op = ip1+ip2
print(op)

ip1.extend(ip2)
print(ip1)