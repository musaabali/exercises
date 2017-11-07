def main():
    valid_number = False
    while not valid_number:
        uinput = ""
        uinput = input("Enter a number between 0 and 100: ")
        try:
             uinput = float(uinput)
        except ValueError:
            print ("Letters are not allowed")
            continue
            
        if uinput > 0 and uinput < 100:
            print ("Good job")
            valid_number = True
        else:
            print ("Number out of bounds, try again")
main()