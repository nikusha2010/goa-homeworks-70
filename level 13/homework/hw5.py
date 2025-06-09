# დავალება 5: ასაკი და კვება
# მომხმარებელი შეიყვანს ასაკს. პროგრამა გასცემს კვების რეკომენდაციას:

age = int(input("Enter your age: "))

if age > 0 and age <= 12:
    print("You need vitamin-rich foods! ")
if age > 13 and age <= 25:
    print("You need energy-giving food! ")
if age > 26 and age <= 59:
    print("You need a balanced diet! ")
if age > 60:
    print("You need low-calorie and light food! ")