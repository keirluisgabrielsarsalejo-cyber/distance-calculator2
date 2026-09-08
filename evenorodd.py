while True:
    try:
        whole_number=int(input("Enter a whole number: "))
        break
    except:
        print("Please enter a WHOLE number.")
    # This makes it so that the user can **ONLY** input a whole number.

if whole_number % 2 ==0:
    print("The number is Even.") # Output: Even
else:
    print("The number is Odd") # Output: Odd
