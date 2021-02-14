first_list = ['python','ruby','go','c++','c#','powershell']
second_list = []

while first_list:
    hold = first_list.pop()
    print("now moving items: " + hold.title())
    second_list.append(hold)

print(second_list)

second_list.append('python')
print(second_list)

while 'python' in second_list:
    second_list.remove('python')

print(second_list)

