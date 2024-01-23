import random  # Import the random module for generating random numbers

# Function to simulate dice throws
def throw_dice(sides, throws):
    # Initialize a dictionary to count occurrences of each side
    results = {side: 0 for side in range(1, sides + 1)}

    # Loop for the number of throws
    for _ in range(throws):
        # Generate a random number between 1 and the number of sides
        result = random.randint(1, sides)
        # Increment the count for the side that came up
        results[result] += 1

    # Return the final counts of each side
    return results

# Main function to handle user input and display results
def main():
    try:
        # Get user input for the number of sides and the number of throws
        sides = int(input("Enter the number of sides of the dice: "))
        throws = int(input("Enter the number of times to throw the dice: "))

        # Check if the input values are positive integers
        if sides <= 0 or throws <= 0:
            raise ValueError("The number of sides and throws must be positive integers.")

        # Ensure the number of throws is a multiple of the number of sides
        if throws % sides != 0:
            raise ValueError("The number of throws should be a multiple of the number of sides.")

        # Call the function to throw the dice
        results = throw_dice(sides, throws)

        # Print the results
        print("Results of throwing a {}-sided dice {} times:".format(sides, throws))
        for side, count in results.items():
            print("Side {}: {}".format(side, count))

    # Catch and display any ValueError
    except ValueError as e:
        print("Error:", e)
    # Catch any other unexpected errors
    except Exception as e:
        print("An unexpected error occurred:", e)

# Ensure the main function is called when the script is executed
if __name__ == "__main__":
    main()
