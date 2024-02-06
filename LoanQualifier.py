years_active=int(input("Enter the number of years you have worked: "))
salary=float(input("Enter you yearly salary: "))

if years_active>=2 and \
   salary>=30000:
    print("YOU QUALIFY! Welcome to the team!")
else:
    print("Sorry, you didn't make the cut.\
 We require a yearly salary of at least $30,000\
 and minimum of 2 years of experience")
