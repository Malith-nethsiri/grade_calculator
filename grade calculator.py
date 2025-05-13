# grde calculaator

score= float(input("what is your score? "))

if score > 100 or score < 0 :
    print("your score is not valid, check it again ?? ")


elif score == 100:
    print("** you got the perfect score **")

elif score >= 90:
    print("** you got a A+ score **")

elif score >= 75:
    print("** you got a A pass **")

elif score >= 65:
    print("** you got a B pass **")

elif score >= 55:
    print("** you got a C pass **")

elif score >= 35:
    print("** you got a S pass **")

else :
    print("""unfortunately you have failed the exam 
work hard next time 
never give up               """)
