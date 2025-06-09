# 1)  მომხმარებელს შემოატანინეთ თავისი გულის ცემა გააკეთეთ პატარა გულის ცემის სისტემა რომელიც ითვლის რა თქმა უნდა გულის ცემას  თუ 180 ზე მეტია ამ შემთხვევაში მაღალია თუ 160-დან 170 მდე არის ამ შემთვევაში არის ნორმალური თუ 160-ზე ნაკლებია ამ შემთხვევაში დაბალია 


Heartbeat = int(input("Enter Your Heartbeat: "))

if Heartbeat > 180:
    print("its high! ")
if Heartbeat > 160 and Heartbeat < 170:
    print("its normal! ")
if Heartbeat < 160:
    print("its low! ")