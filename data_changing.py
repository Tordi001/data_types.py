height = int(input("Enter your height in feet: "))
age = int(input("Enter your age here: "))

if(height<20):
    print("you are qualified for this job")
    if(height<15):
        print("you are qualified for this job")
    elif(height<10):
        print("you are not welcome in this company")
    else:
        print("You are not qualified for this job")

if(age<50):
    print("you are qualified for this job")
else:
    print("You are not qualified for this job")