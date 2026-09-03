'''
WAP to enter name & % in a dictionary and display the info on the Screen
'''

num = int(input("Enter total number of Students : "))
dic = {}
for i in range(num):
    name = str(input("Enter the Student Name : "))
    perct = float(input("Enter the STudent Percentage : "))
    dic[name] = perct

print(dic)