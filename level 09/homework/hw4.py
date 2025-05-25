# 4.შექმენით პროგრამა რომელიც მიიღებს მომხარებლისგან input-ს რიხვის სახით და დაბეჭდეთ ამ რიცხვამდე ყველა რიცხვი თანმიმდევრობით. (For loop)

number = int(input("Enter number: "))

i = 1

for i in range(1, number + 1, 1):
    print(i)


