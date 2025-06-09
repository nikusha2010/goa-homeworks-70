# დავალება 3: ასაკის შეჯერება დღის მონაკვეთთან
# შეიყვანოს მომხმარებელმა ასაკი და საათი (0-დან 23-მდე). პროგრამამ განსაზღვროს:

age = int(input("Enter your age: "))
time = int(input("Enter time: "))

if age < 18 and time >= 22:
    print("It's time for bed! ")
if age >= 60 and time >= 21:
    print("It is recommended to relax! ")
else:
    print("You can continue the activity! ")