#Task 1) Ask for the user to input number of years and print out how many days, 
#weeks, and hours are present in the number of years provided.
num_years=int(input("Enter number of years: "))

print(num_years*365, "days")
print(num_years*52, "weeks")
print(num_years*365*24, "hours")