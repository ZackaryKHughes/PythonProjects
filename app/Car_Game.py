command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car Started")
    elif command == "stop":
        print("Car Stopped")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - to quit""")
    elif command == "quit":
        break
    else:
        print("I don't understand this.")

