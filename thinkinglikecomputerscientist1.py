#Compounding Interest Assignment

p = 1000
n = 12
r = 0.08
time_lapse = input("please enter the time period you want to use. ")
t = int(time_lapse)
compounded_interest = p * (1 + (r/n)) ** (n*t)

print compounded_interest