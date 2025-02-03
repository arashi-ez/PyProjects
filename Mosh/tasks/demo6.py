numbers = [5,2,4,2,2]

print("-----------")
print("Nested Loop")
print("-----------")

for item in numbers:
    holder = ''
    for counter in range(item):
        holder += 'x'
    print(holder)
print("---------------")
print("Simple Solution")
print("---------------")


for items in numbers:
    print('x' * items)