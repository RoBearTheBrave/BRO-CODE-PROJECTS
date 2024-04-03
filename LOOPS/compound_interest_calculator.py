#compound interest calculator uses formula A = P(1 + r/n)^(t)

principle = 0
rate = 0
time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle amount must be greater than 0") 

# while rate <= 0:
#     rate = float(input("Enter the interest rate: "))
#     if rate <= 0:
#         print("Interest amount must be greater than 0")  

# while time <= 0:
#     time = int(input("Enter the time in years: "))
#     if time <= 0:
#         print("Years must be greater than 0") 

# total = principle * pow((1 + rate/100), time)
# print(f"The total amount after {time} years is: {total:.2f}")

### allows users to enter 0 values for principle, rate, and time
while True:
    principle = float(input("Enter the principle amount: "))
    if principle <= 0:
        print("Principle amount must be greater than 0") 
    else:
        break

while True:
    rate = float(input("Enter the interest rate: "))
    if rate <= 0:
        print("Interest amount must be greater than 0")  
    else:
        break

while True:
    time = int(input("Enter the time in years: "))
    if time <= 0:
        print("Years must be greater than 0") 
    else:
        break

total = principle * pow((1 + rate/100), time)
print(f"The total amount after {time} years is: {total:.2f}")