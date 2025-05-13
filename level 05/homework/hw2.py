# 2)მომხმარებელს შემოატანინეთ ორი რიცხვი გააკეთეთ მათზე მათემატიკური ოპერაციები  ("+, -, *, /, %, <, >, <=, >=, ==, !=. **) 

first_num = int(input("Enter first number :"))
second_num = int(input("Enter second number :"))

plus = first_num + second_num
minus = first_num - second_num
multipy = first_num * second_num
divide = first_num / second_num
percent = first_num % second_num
square = first_num ** second_num

print(plus)
print(minus)
print(multipy)
print(divide)
print(percent)
print(square)

if first_num > second_num :
    print(True)
if first_num < second_num:
    print(False)

if first_num <= second_num:
    print(True)
if first_num >= second_num:
    print(False)

if first_num == second_num:
    print(True)
if first_num != second_num:
    print(False)