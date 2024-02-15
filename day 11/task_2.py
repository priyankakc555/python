# print(result)
# Create a new list of repeated items from a provided list:
# nums = [3, 4, 2, 2, 1, 3, 3, 3]
# Output = [3, 2]

nums = [3, 4, 2, 2, 1, 3, 3, 3]
result = []
for i in nums:
    if nums.count(i) > 1 and i not in result:
        result.append(i)  # [3, 2]
print(result) 

# WAP to prompt the user for hours and rate per hour using input to compute gross pay. Pay the hourly rate for the hours up to 40 and 1.5 times the hourly rate for all hours worked above 40 hours. 
#Use 45 hours and a rate of 10.50 per hour to test the program (the pay should be 498.75). You should use input to read a string and float() to convert the string to a number.

hour=float(input("enter the hour of work"))
rate=float(input("enter the hourly rate :"))
if hour <40 :
    print(f"the salary of the worker is {rate *hour}")
else:
    print(f"the salary of the worker is {(rate *40)+(hour-40)(rate *1.5)}")