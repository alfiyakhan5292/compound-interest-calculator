# Python compound interest calculator

# formula of compound interest : A = P(1 + r / n)^t

principle = 0
rate = 0
time = 0 

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle can't be less than zero")
    else:
        break    


while True:
    rate = float(input("Enter the interest rate: "))
    if rate < 0:
        print("interest rate can't be less than zero")
    else:
        break 

while True:
    time = int(input("Enter the time of the years: "))
    if rate < 0:
        print("Time can't be less than zero")
    else:
        break 
    
total = principle * pow((1 + rate / 100), time)
print(f"Balance after {time} year/s: ₹{total:.2f}")