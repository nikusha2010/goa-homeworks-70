# დავალება 4: ფიზიკური აქტივობის რეკომენდაცია,
# მომხმარებელი შეიყვანს თავის ასაკს და გულის ცემას.
# პროგრამამ უნდა დაარიგოს ასეთი რჩევები:

age = int(input("Enter your age: "))
heartbeat = int(input("Enter your heartbeat: "))


if age < 30 and heartbeat < 140:
    print("You can practice more! ")
if age >= 30 and heartbeat > 170:
    print("You need relax! ")
else:
    print("Activity level is normal! ")