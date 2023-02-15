bill = 1000
indomie = str(input("Do you wish to order for an indomie? (Y/N): "))
if(indomie == 'Y' or indomie == 'y'):
    bill += 200
    print("Okay.... your oder will be available in few seconds.....")
if(indomie == 'N' or indomie == 'n'):
    bill += 10
    print("Thank you for cancelling your request....")

rice = str(input("Do you wish to order for rice? (Y/N): "))
if(rice == 'Y' or rice == 'y'):
    bill =+ 200
    print("Okay.... your oder will be available in few seconds.....")

beans = str(input("Do you wish to order for an Beans? (Y/N): "))
if(beans == 'Y' or beans == 'y'):
    bill += 300
    print("Thank you for cancelling your request....")
if(beans == 'N' or beans == 'n'):
    bill += 000
    print("Thank you for cancelling your request....")

print("THANK YOU FOR PETRONIZING US!!!")