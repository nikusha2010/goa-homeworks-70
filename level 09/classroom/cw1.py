# 1. მომხმარებელს შემოატანინეთ სამი რიცხვი, start/end/step და ჩასვით for loop-ში სათანადო ადგილას.

start = int(input("start: "))
end = int(input("end: "))
step = int(input("step: "))

for i in range(start, end, step):
    print(i)
