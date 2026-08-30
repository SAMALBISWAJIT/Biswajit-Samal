vow = ['a','e','i','o','u']
ip = input("enter any string : ")
vow_ip = []
for i in ip:
    if i.lower() in vow:
        if i.lower() not in vow_ip:
            vow_ip.append(i.lower())
vow_ip.sort()
print(vow_ip)