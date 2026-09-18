degree=int(input("Enter the Degree"))
if degree <=20:
    print("cold Weather")
elif degree>20 and degree<=38:
    print("Normal weather")
else:
    print("Hot! weather")
    fahrenheit=((degree*1.8)+32)
    print("The Fahrenheit value is ",fahrenheit,"F")