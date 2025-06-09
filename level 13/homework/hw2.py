# დავალება 2: წონის შეფასება ასაკის მიხედვით (უბრალოდ და ლოგიკურად),
# აღწერა: მომხმარებელი შეიყვანს საკუთარ ასაკს და წონას. პროგრამამ უნდა შეაფასოს წონა ასაკის მიხედვით მარტივი ლოგიკით:

age = int(input("Enter your age: "))
weight = int(input("Enter your weight: "))

if age < 10:
    if weight < 20:
        print("low weight! ")
    if weight > 20 and weight <= 40:
        print("normal weight! ")
    if weight > 40:
        print("high weight! ")

if age > 10 and age <= 17:
    if weight < 40:
        print("low weight")
    if weight > 40 and weight <= 65:
        print("normal weight! ")
    if weight > 65:
        print("high weight! ")

if age >= 18:
    if weight < 50:
        print("low weight! ")
    if weight > 50 and weight <= 90:
        print("normal weight! ")
    if weight > 90:
        print("high weight! ")
