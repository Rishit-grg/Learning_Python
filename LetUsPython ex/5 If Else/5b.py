a = int(input("Enter a year to check:"))

if a%4==0 :
    if a%100==0:
        if a%400==0:
            print("LEAP YR")
        else:
            print("NON LEAP YR")
    else:
        print ("LEAP YR")
        
else:
    print("NON LEAP YR")


# ...............CHAT GPT BETTTER CODE .........................
# year = int(input("Enter a year to check: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("LEAP YR")
# else:
#     print("NON LEAP YR")
