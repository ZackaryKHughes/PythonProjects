high_income = False
good_credit = True
criminal_record = True

if good_credit and not criminal_record:
    print("Is eligible for loan")
else:
    print("I am sorry, not eligible for loan")

# And : both
# Or: at least one
# Not: True will change to a False on a variable.

temperature = 70

if temperature >= 70:
    print("It's a hot day")
else:
    print("It's not a hot day")


