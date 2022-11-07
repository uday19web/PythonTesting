greeting = "Good Morining"

if greeting == "Morning":
    print("Condition Matches")
else:
    print('Condition do not match')
print("if else completed")

print("##################################################################")
print("For loop explanation")
# for loop
obj = [2, 3, 5, 7, 9]

for i in obj:
    print(i)
print("##################################################################")

# print sum of first 5 natural numbers
num = 0
for i in range(1,6):
    num = num + i
print(num)
print("####################### while loop ###########################################")

it = 10
while it > 1:
    it = it - 1
    if it == 9:
        continue
    if it == 3:
        break
    print(it)



