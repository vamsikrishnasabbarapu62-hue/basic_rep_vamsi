his_name=input("enter your name: ")
her_name=input("enter your name: ")
combined_name=his_name+her_name
lower_case=combined_name.lower()

t=lower_case.count("t")
r=lower_case.count("r")
u=lower_case.count("u")
e=lower_case.count("e")

count_1=t+r+u+e

l=lower_case.count("l")
o=lower_case.count("o")
v=lower_case.count("v")
e=lower_case.count("e")

count_2=l+o+v+e

total_count=int(str(count_1)+str(count_2))

if total_count<10 and total_count>90:
    print("you will be like coke and mentos like a blast")
elif total_count<=50 and total_count>=40:
    print("you will end in breakup")
else:
    print(f"your lovescore is",{total_count} )

    