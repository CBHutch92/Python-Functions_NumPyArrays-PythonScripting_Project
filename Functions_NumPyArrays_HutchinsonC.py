# Casey Hutchinson
# Assignment 3


# Part A
# This function generates and displays the multiplication table (from 0-10) based on the number input from the user that is passed through as a parameter using the "user_number" variable (step 1)
def multiplication_table(user_number):
    for i in range(11):                                 # This creates a loop that stops at 10
        table = (user_number * i)                       # This formula multiplies the users number by the appropriate value i (0-10) based on the current loop iteration
        print(f"{user_number} x {i} = {table}")         # Prints the result of the previous formula after displaying the users number x the value (0-10) based on the current loop iteration so that it can be displayed (via main function below - step 2.b)

# Part B
# This function generates 2 random integers and places them in a tuple by importing the random module (step 1)
def random_integers():
    import random
    randnum1 = random.randint(0, 9)
    randnum2 = random.randint(0, 9)
    return (randnum1, randnum2)


# Part C
# This function asks the user for numbers via input and puts them in an array. It also allows them to do various things with the new array once the user has finished entering numbers for their array
def NumPy_Array():
    while True:
        import numpy as np                                                                                                                                          # Imports NumPy (step 1)
        user_numbers = []
        print("\n")
        print("Now we are going to create a set of numbers in an 'array'")
        print("To do this, please enter a number between 1 and 100 (inclusive) - no decimals! When you are done entering numbers, you can enter 0.")                # Rules for the following loop
        while True:
            try:
                input_number = int(input("Please enter your number here (Remember, enter a 0 to stop): "))                                                          # Asks the user to input numbers between 1-100 using a loop until they enter a 0 (step 2)
                if input_number == 0:
                    break                                                                                                                                           # Ends the loop when the user enters a 0 (step 2)
                if input_number >= 1 and input_number <= 100:
                    user_numbers.append(input_number)                                                                                                               # Appends numbers entered b/w 1-100 to the user_numbers list
                else:
                    print("Invalid input. Please enter a whole number between 1 and 100.")
            except ValueError:
                print("Invalid input. Please enter whole number values only - no decimals!")
        
        if user_numbers:
            user_array = np.array(user_numbers)                                                                                                                     # Using NumPy, we use the numbers stored in the list to create a one-dimensional array (step 3)
        else:
            print("You did not enter any valid numbers. Please try again.")
            continue

        while True:
            print("\n")
            print("What would you like to do with the array you've created?")                                                                                       # Asks the user what they want to do with their newly created array (step 4)
            print("You can make your choice by entering the appropriate number below.")
            print("1. Print the array.")                                                                                                                            # Prints the array (step 4)
            print("2. Print the array's data type.")                                                                                                                # Prints the array's data type (step 4)
            print("3. Print the array's number of dimensions.")                                                                                                     # Prints the number of dimensions of the array (step 4)
            print("4. Print the array's shape.")                                                                                                                    # Prints the array's shape (step 4)
            print("5. Print the array's number of elements.")                                                                                                       # Prints the number of elements in the array (step 4)
            print("6. Reshape the array (You will provide the new shape).")                                                                                         # Reshapes the array (step 4)
            print("7. Slice the array (You will provide the indices).")                                                                                             # Slices the array (step 4)
            print("8. Exit the program.")                                                                                                                           # Quite (step 4)
            print("\n")

            user_choice = input("Please enter your what you would like to do by entering the appropriate number choice: ")
            print("\n")

            # Using an if, elif, else statement the user can call the corresponding block of code based on the choice input they entered above (step 4)
            if user_choice == '1':                                                                                                                                  
                print("Your Array:", user_array)                                                                                                                    # Displays result from choice 1 (step 5)
            elif user_choice == '2':                                                                                                                                
                print("The data type of your array:", user_array.dtype)                                                                                             # Displays result from choice 2 (step 5)
            elif user_choice == '3':                                                                                                                                
                print("The number of dimensions of your array:", user_array.ndim)                                                                                   # Displays result from choice 3 (step 5)
            elif user_choice == '4':                                                                                                                                
                print("The shape of your array:", user_array.shape)                                                                                                 # Displays result from choice 4 (step 5)
            elif user_choice == '5':                                                                                                                                
                print("The number of elements in your array:", user_array.size)                                                                                     # Displays result from choice 5 (step 5)
            elif user_choice == '6':                                                                                                                                
                new_array = input("Please enter the new shape for the array (Example: '3,2'): ")
                try:
                    # I had a lot of trouble with this one and eventually read about 'map' on Web3 and GeeksForGeeks, and read ahead a bit to Ch. 13 in our book
                    reshape_tuple = tuple(map(int, new_array.split(',')))
                    reshape_array = user_array.reshape(reshape_tuple)
                    user_array = reshape_array
                    print(f"Your reshaped array:", user_array)                                                                                                      # Displays result from choice 6 (step 5)
                except ValueError:
                    print("Invalid input. Please enter whole number values only - no decimals! If you did and still get this error, your new array shape is not compatible with the elements in the array (Example: 6 elements but you entered '2,4')")
            elif user_choice == '7':                                                                                                                                
                print(f"The current array: {user_array}")
                current_shape = user_array.shape
                print(f"The current shape of the array: {current_shape}")
                print("\n")
                slice_start = input(f"Please enter a whole number to start your slice (0 to {current_shape[0]-1}): ")
                slice_end = input(f"Please enter a whole number to end your slice (1 to {current_shape[0]}): ")
                try:
                    slice_start = int(slice_start)
                    slice_end = int(slice_end)
                    if slice_start >= 0 and slice_end <= current_shape[0]:
                        array_slice = user_array[slice_start:slice_end]
                        print("The sliced array:", array_slice)                                                                                                     # Displays result from choice 7 (step 5)
                    else:
                        print("Invalid input. The indices you entered are outside of the bounds of the current array.")
                except ValueError:
                    ("Invalid input. Please enter number values only.")
            elif user_choice == '8':                                                                                                                                
                print("Thank you for using my program! Have a great day.")                                                                                          # Displays quitting message (step 5)
                exit()
            else:
                print("Invalid input. Please enter a 1-8 to select from the menu above.")
    
def main():
    while True:
        # Asking the user for a number and storing it in a variable (Part A, step 2.a)
        try:
            user_number = int(input("Please enter a number from 0-10 (inclusive) to view it's multiplication table up to 10: "))
            if user_number < 0 or user_number > 10:
                print("Please enter a whole number value from 0-10 only. Thank you.")
                continue
        except ValueError:
            print("Invalid input. Please enter whole number values only. Thank you.")
            continue
        
        # Calls the function from step 2.a and displays the results (Part A, step 2.b)
        multiplication_table(user_number)

        while True:
            # Here we call the function from Part B above and store the randomly generate tuple in a variable called numbers_tuple
            numbers_tuple = random_integers()
            while True:
                try:
                    # Here we ask the user for the answer of the two randomly generated numbers in the tuple multiplied together, and we specify that we want whole number values only and no decimals (Part B, step2.1)
                    answer = int(input(f"What is {numbers_tuple[0]} x {numbers_tuple[1]}? Please enter whole number values only - no decimals! "))

                    if answer == (numbers_tuple[0]) * (numbers_tuple[1]):
                        # This congratulates the user if they got the answer correct, and then shows them a list where they can choose either 1. Try another question or 2. Close the program (Part B, step2.2)
                        print(f"That's correct! {numbers_tuple[0]} x {numbers_tuple[1]} = {answer}!")
                        print("\n")
                        while True:
                            print("Would you like to try another question?")
                            print("Please select from the list below.")
                            print("1. Yes, I'd like to answer another question.")
                            print("2. No, I'd like to close this part of the program.")
                            choice = input("Please enter your choice here by entering the appropriate number: ")

                            # If the user chooses option 1 (Yes), the loop asks them another question (Part B, step2.3)
                            if choice == "1":
                                break
                            # If the user chooses option 2 (No), we thank the user for using the program and close the program (Part B, step2.4)
                            # I chose to nest my NumPy_Array() into this part of the main() because I could not get this block of code to move on to the next block of code, and it would instead close the whole program.
                            # This way the NumPy_Array() does not start until the user chooses to exit the multiplication part of the program
                            elif choice == "2":
                                print("\n")
                                print("Thanks for using the multiplication part of the program!")
                                NumPy_Array()

                            # Makes sure the user chooses either option 1 or 2.
                            else:
                                print("\n")
                                print("Invalid choice. Please select either 1 for another question or 2 to exit the program.")
                                print("\n")
                        break
                    # This lets the user know that their answer input is incorrect and to try again. The program will ask them the same question until they get it correct (Part B, step 2.5)
                    else:
                        print("Incorrect. Please try again.")
                        print("\n")
                except ValueError:
                    print("\n")
                    print("Invalid input. Please enter a whole number only - no decimals!")
                    print("\n")
    
if __name__ == "__main__":
    main()