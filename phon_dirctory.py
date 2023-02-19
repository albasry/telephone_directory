# Keys are unique in a Dictionary and can not be duplicated inside a Dictionary.
# So I used it to write telephone numbers.
tele_dir = {
    1111111111: "John",
    2222222222: "Sara",
    3333333333: "Amal",
    4444444444: "Ahmed"
}

while True:
    # As we know that Python’s built-in input() function always returns a str(string) class object.
    user_input = input("Please enter the phone number: ")
    # To force user to input numbers only, use .isdigit() method
    # To force user to input characters only, use .isalpha() method
    if user_input.isdigit() and len(user_input) == 10:
        # So for taking integer input we have to type cast those inputs into
        # integers by using Python built-in int() function.
        if int(user_input) in tele_dir:
            print(f"This number belongs to: {tele_dir[int(user_input)]}")
        else:
            print("Sorry, the number is not found")
        break
    else:
        print("Invalid: It must be ten digits!")
