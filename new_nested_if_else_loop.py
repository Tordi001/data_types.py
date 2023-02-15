weight = int(input("Enter the value of weight here: "))
height = int(input("Enter the value of height here: "))

bmi = (weight)/(height) ** 2
if(bmi<500):
    print("I am coming by 05:00pm")
elif(bmi<400):
    print("I am coming by 04:00pm")
elif(bmi<300):
    print("I am coming by 03:00pm")
elif(bmi<200):
    print("Am not coming by 02:00pm")
elif(bmi<100):
    print("Am not coming by 01:00pm")
else:
    print("i am not coming at all")
print(int(bmi))