# დავალება 1: წნევის ანალიზი
# მომხმარებელი შეიყვანს ორ მაჩვენებელს: სისტოლური და დიასტოლური წნევა.
# პროგრამამ უნდა განსაზღვროს წნევის კატეგორია:

Systolic_pressure = int(input("Enter your Systolic pressure: "))
Diastolic_pressure = int(input("Enter your Diastolic pressure: "))

if Systolic_pressure > 140 or Diastolic_pressure > 90:
    print("high pressure! ")
if Systolic_pressure < 90 or Diastolic_pressure < 60:
    print("low pressure! ")
else:
    print("normal pressure")

