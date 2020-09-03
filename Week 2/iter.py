print("Please think of a number between 0 and 100!:")
low = 0
hi = 100
while True:
    print ("Is your secret number", (low + hi)//2,"?")
    ans = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if ans == "h":
        hi = (low + hi)//2
    elif ans == "l":
        low = (low + hi)//2
    elif ans == "c":
        print ("Game over. Your secret number was:", ans)
        break
    else:
        print ("Sorry, I did not understand your input.")
