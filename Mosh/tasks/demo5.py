command = ""
is_driving = False
help = """start - to start
stop  - to stop
quit  - to stop"""
while True:
    command = input('> ').lower()
    if is_driving == False:
        if command == "start":
            print("Car is Starting")        
            is_driving = True    
        elif command == "stop":
            print("Already")
        elif command == "help":
            print(help)
        elif command == "quit":
            print("Game Over")
            break
        else:
            print("Wrong Input.")
    elif is_driving == True:
        if command == "start":
            print("Already Started")
        elif command == "stop":
            print("Stopped")            
            is_driving == False
        elif command == "help":
            print(help)
        elif command == "quit":
            print("Game Over")
            break
        else:
            print("Wrong Input.")

