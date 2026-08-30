'''
count the frequency of any element within a given string
'''
ip = input("enter any string : ")
sub_ip = input("which element need to check the frequency : ")
j = 0
for i in ip:
    if sub_ip.lower() in i.lower():
        j = j+1
        continue
print(f'the sub_ip {sub_ip} found in input {ip} is {j}')