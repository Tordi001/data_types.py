name1 = input("Enter your first name heree: ")
name2 = input("Enter your second name here: ")

combined_name = name1 + name2
lower_case_name = combined_name.lower()
t = lower_case_name.count('t')
o = lower_case_name.count('o')
r = lower_case_name.count('r')
d = lower_case_name.count('d')
i = lower_case_name.count('i')
tordi = t + o + r + d + i

f = lower_case_name.count('f')
r = lower_case_name.count('r')
i = lower_case_name.count('i')
d = lower_case_name.count('d')
a = lower_case_name.count('a')
y = lower_case_name.count('y')
friday = f + r + i + d + a + y
sum = int(str(tordi) + str(friday))
if(sum < 40 or sum > 90):
    print(f"Your love score is {sum} ")
else:
    print(f"Your score is {sum}")
print("BYE......")
