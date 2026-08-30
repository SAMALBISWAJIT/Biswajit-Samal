'''
flattening the list values
ip = [[1,2],[3,4],[3,5]]
op = [1, 2, 3, 4, 5]
'''

ip = [[1,2],[3,4],[3,5]]
flat = []
print(f'input is : {ip}')
for i in ip:
    #print(i)
    #print(type(i))
    if isinstance(i, list):
        #print("inside another list")
        for j in i:
            if j not in flat:
                flat.append(j)
    else:
        if i not in flat:
            flat.append(i)

print(f'output is : {flat}')