i = 1

while i <= 5:
    print("*" * i)
    i = i + 1
print("Done")

# Create a guessing game that take a number between 1-9 as a target and use the while loop until you get the right number but you only get 3 chances

total_number = 9
winning_number = 5
guess_count = 0
guess_limit = 3


while guess_count < guess_limit:
    guess = int(input("Guess a number between 1-9 "))
    guess_count += 1
    if guess == winning_number:
        print("Congrats you guessed the correct number!")
        break
else:
    print("Sorry wrong number")



