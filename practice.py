# print 1 to 10
for i in range(10):
    print(i)
print("********************")
count = 0
while count < 5:
    print(count)
    count += 1

print("******** 5 to 10 ********")
for i in range(5, 11):
    print(i)

print("******** pyramid 1 *******")
for i in range(3):
    for j in range(2):
        print(i, j)


print("******** Area of circle ********")
import math
radius = float(input("Enter area : "))
area = math.pi * (radius ** 2)
print(area)