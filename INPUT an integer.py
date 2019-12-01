#input an integer x

while True:
    try:
        x = int(input("Please enter an integer: "))
        break
    except ValueError:
         print("Error.  Enter an INTEGER.  Try again.")
         winsound.Beep(370,630)
