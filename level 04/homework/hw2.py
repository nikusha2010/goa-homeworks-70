#2) მომხმარებელს შემოატანინეთ ორი რიცხვითი მნიშვნელობა (სიგანე და სიმაღლე). ტერმინალში გამოიტანეთ ფართობი/პერიმეტრი. S = ფართობი (S = width*height)/P = პერიმეტრი (P = (width+height)*2

width = int(input("Enter width: "))
height = int(input("Enter height: "))


P = (width + height)*2
S = width * height

print("Perimeter is ", P ,"and area is ", S)