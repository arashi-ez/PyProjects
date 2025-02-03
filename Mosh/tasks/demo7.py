numbers = [2,2,4,6,3,4,6,1,4]
numbers.sort()

#at this code check and pop copies
#it will not iterate to the next value untill all elmens is existing 
#less efficient
i = 1
while i < len(numbers):
    if numbers[i] == numbers[i-1]:
        numbers.pop(i)
    else:
        i+=1
print(numbers)

#at this ex make a copy of a code after and append of nonexisting ones
#from numbers to holder
holder = []
for number in numbers:
    if number not in holder:
        holder.append(number)
print(holder)