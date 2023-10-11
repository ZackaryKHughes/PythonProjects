# Question 1 We Check in a patient named John Smith. He's 20 years old and is a new patient.
# Fill out variables for patient name, age, and if he is a new or old patient.

# name = "John Smith"
# age = 20
# new_patient = True

# Question 2 Ask two questions: person's name and favorite color
# Then, print a message like "Name likes blue"

# name = input("What is your name? ")
# color = input("What is your favorite color? ")
#
# print(name + " likes " + color)

# Question 3 Ask a user their weight (in pounds), convert it to kilograms and print on the terminal

weight = input("What is your weight in pounds? ")
kilo = int(weight) / 2.20462262
print(kilo)


# Question 4 Using Arithmetic Operations, solve the following problem

x = (2 + 3) * 10 - 3
# First the 2 + 3 = 5. Then Multiplication so 5 * 3 = 50. Then subtraction 50 - 3 = 47.
print(x)

# Question 5 A price of a house is $1M. If the buyer has good credit they need to put down 10%. Otherwise they need to put down 20%. Print the down payment for a buyer with good credit.

house = 1000000
good_credit = False
bad_credit = True

if good_credit:
    down_payment = house * .10
    print(f"You have really good credit and you down payment is only 10%. That will come out to be ${down_payment}")
elif bad_credit:
    down_payment = house * .20
    print(f"Your credit isn't the best but we can still make the deal. We just need a higher down payment of 20%, which will be ${down_payment}")
else:
    print("I am sorry but you do not qualify for this house.")


# Question 6 If name is less than 3 characters long name must be at least 3 characters otherwise if it more than 50 characters long name can be a mximum of 50 character otherwise name looks good!


name = input("What is your name? ")


if len(name) < 3 or len(name) > 50:
    print("Please enter a name the is more than 3 or less than 50 characters long")
else:
    print("Name looks good, have a great day!")





