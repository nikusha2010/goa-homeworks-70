# 1) შექმენი for loop- რომელიც გამოიტანს 1-100 ჩატვლით რიცხვებს და ასევე კენტია თუ ლუწი ეს რიცხვი.

for i in range(1, 100 + 1, 1):
    print(i)
    if i % 2 == 0:
        print("luwi ", i)
    else:
        print("kenti ", i)