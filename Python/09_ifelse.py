age = int(input("Enter your age : "))
if(age < 18):
    print("can not drive")
elif(age >= 18 and age <= 60):
    print("can drive")
else:
    print("you are not ligible")