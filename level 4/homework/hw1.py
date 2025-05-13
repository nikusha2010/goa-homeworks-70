#1) მომხარებელს შემოატანინეთ სახელი და ასაკი და დაპრინტეთ შემდეგ ფორმატში: "Name: სახელი, Age: ასაკი"

name = input("Enter your name: ")
age = input("Enter yout age: ")

print("name :"+ name)
print("age :"+ age)

#2) მომხმარებელს შემოატანინეთ ორი რიცხვითი მნიშვნელობა (სიგანე და სიმაღლე). ტერმინალში გამოიტანეთ ფართობი/პერიმეტრი. S = ფართობი (S = width*height)/P = პერიმეტრი (P = (width+height)*2

width = int(input("Enter width: "))
height = int(input("Enter height: "))


P = (width + height)*2
S = width * height

print("Perimeter is ", P ,"and area is ", S)

#3) კომენტარების სახით ახსენი რა არის input და output

#input ის საშვალებით ხდება მონაცემის შეტანა პროგრამაში

#output ის საშუალებით ხდება შეტანილი ინფორმაციის გამოტანა ეკრანზე



#4) შემოატანინეთ მომხმარებელს ორი რიცხვი და დაპრინტეთ მათი ჯამი, სხვაობა, ნამრავლი და განაყოფი.

first_num = int(input("enter your first num: "))
second_num = int(input("enter your second num: "))

plus = first_num + second_num
print(plus)

minus = first_num - second_num
print(minus)

multipy = first_num * second_num
print(multipy)

divide = first_num / second_num
print(divide)



