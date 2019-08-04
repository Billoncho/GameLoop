# GameLoop.py
# Billy Ridgeway
# Loops the game as long as the user presses "ENTER".
# Practice program.

keep_going = True   # Set the variable to true.

# Creates a while loop to check to see if the user pressed "ENTER"
# to keep playing or any other key to exit.
while keep_going:
    answer = input("Hit [Enter] to keep going, any key to exit: ")
    keep_going = (answer == "")
