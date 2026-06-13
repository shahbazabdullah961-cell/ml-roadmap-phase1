Weight = int(input("Enter your Weight:"))
Height = int(input("Enter your Height(m^2):"))
if(Height==0):
    print("Height cannot be 0")
    Height=int(input("New Height!"))
BMI = Weight/Height ** 2
if(BMI < 18.5):
    print("You are under weight")
elif(BMI >= 18.5 and BMI < 25 ):
    print("You have normal weight")
elif (BMI >=25 and BMI<30):
    print("You are Overweight")
else:
    print("You are Obese")