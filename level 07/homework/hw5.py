# 5)მომხმარებელმა უნდა შეიყვანოს რიცხვი n. პროგრამამ while ციკლით უნდა დაითვალოს 1-დან n-მდე რიცხვების ჯამი.  

n = int(input("Enter number: "))

count = 1

total = 0

while count <= n:
    total += count
    count += 1

print(total)