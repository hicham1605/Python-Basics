
n = int(input("how many times you want to check the years: "))

for y in range (1, n + 1):
    year = int(input("Enter The years: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print (f"{year} is a leap year")
    else:
        print (f"{year} is not a leap year")