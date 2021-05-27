
METER = 100


height = float(input("Enter your height in Centimeters: "))
weight = float(input("Enter your weight in Kg: "))

temp = height / METER

bmi = weight / (temp * temp)


print("Your Body Mass Index is: ", "%d" % (bmi))