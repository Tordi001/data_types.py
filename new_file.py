rice = input("Choose within your orders using (Y/N): ")
if(rice == 'Y' or rice == 'y'):
    print("your rice will be available shortly.....")
elif(rice == 'N' or rice == 'n'):
    print("Your have successfully cancceled your order for rice.....")
else:
    print("there are no more packages for rice for this service....")

beans = input("Choose within your orders using (Y/N): ")
if(beans == 'Y' or beans == 'y'):
    print("your rice will be available shortly.....")
elif(beans == 'N' or beans == 'n'):
    print("Your have successfully cancceled your order for beans.....")
else:
    print("there are no more packages for beans in this service......")

indomie = input("Choose within your orders using (Y/N):")
if(indomie == 'Y' or indomie == 'y'):
    print("your indomie will be available shortly.....")
elif(indomie == 'N' or indomie == 'n'):
    print("Your have successfully cancceled your order for indomie.......")
else:
    print("there are no more packages for beans in this service......")

supergatti = input("Choose within your orders using (Y/N): ")
if(supergatti == 'Y' or supergatti == 'y'):
    print("your supergatti will be available shortly.....")
elif(supergatti == 'N' or supergatti == 'n'):
    print("Your have successfully cancceled your order for supergatti.....")
else:
    print("there are no more packages for supergatti in this service......")

print("Thank you for you services.....")
print("We really you services with us....")

if(supergatti == indomie):
    print("You will be offerred both supergatti and indomie")
elif(supergatti == rice):
    print("this service is for supergatti and rice only")