# 3) მომხმარებელს სთხოვე შეიყვანოს ორი რიცხვი. შემდეგ:
# თუ ორივე რიცხვი დადებითია → დაბეჭდე "ორივე დადებითია"
# თუ მხოლოდ ერთი დადებითია → "მხოლოდ ერთი დადებითი რიცხვია"
# თუ არცერთი არ არის დადებითი → "არცერთი არ არის დადებითი"


first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

if first_number > 0 and second_number > 0:
    print("ორივე დადებითია")

if first_number > 0 and second_number < 0:
    print("მხოლოდ ერთი დადებითი რიცხვია")
if second_number > 0 and first_number < 0:
    print("მხოლოდ ერთი დადებითი რიცხვია")

if first_number < 0 and second_number < 0:
    print("არცერთი არ არის დადებითი")