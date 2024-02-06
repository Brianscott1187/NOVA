name = input("What is your name?: \n");
print("Your name is:", name)
# Practicing input and breaks
age = int(input("What is your age?: \n"));
# Practicing nesting
# Nesting changes str to int
address = input("What is your street address?: \n")
major = input("What is your major?: \n")
gpa = float(input("What is your GPA?: \n"))

print("You are",age, "years old. \nNext year you will be",age+1, "years old")
# Ask the user a yes/no question
grad_status = input("Have you graduated yet? Enter 'yes' or 'no': ")
grad_status_lower = grad_status.lower()

boolean_var = (grad_status_lower == 'yes')

semesters_needed = 0  # Initialize semesters_needed
if boolean_var == False:
    semesters_needed = int(input(f"How many semesters are needed until graduation, {name}?\n"))
else:
    print(f"Congratulations on your graduation, {name}!")
# Practicing string interpolation

print(f"Your name is: {name},\nyour address is {address},\nyour age is: {age},\nyou have {semesters_needed} semesters left until graduation,\nYour major is {major},\nYour GPA is {gpa}\n")
print("Type of GPA variable:", type(gpa))
print("Type of age variable:", type(age))
print("Type of grad status variable:", type(boolean_var))
print("Type of address variable:", type(address))


