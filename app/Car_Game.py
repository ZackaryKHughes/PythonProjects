command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started")
        else:
            started = True
        print("Car Started")
    elif command == "stop":
        if not started:
            print("Car is already off")
        else:
            started = False
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

