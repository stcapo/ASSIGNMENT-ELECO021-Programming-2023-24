from NumberList import NumberList
def mean(data):
    # Function to calculate the mean (average) of a dataset.
    # 'data' is a list of numerical values.
    return sum(data) / len(data) if data else 0  # Calculate the mean if 'data' is not empty, otherwise return 0.
    # The 'if data' checks if the list is not empty.
    # 'sum(data)' calculates the sum of all elements in 'data'.
    # 'len(data)' gets the number of elements in 'data'.
    # If 'data' is empty, 'sum(data)' and 'len(data)' would raise an error, so 'else 0' returns 0 in this case.

def variance(data):
    # Function to calculate the variance of a dataset.
    # 'data' is a list of numerical values.
    if not data:
        # Check if the list 'data' is empty.
        return 0  # Return 0 if 'data' is empty as variance is not defined for an empty dataset.
    data_mean = mean(data)  # Calculate the mean of the dataset using the mean function defined above.
    # The variance is calculated as the average of the squared differences from the mean.
    return sum((x - data_mean) ** 2 for x in data) / len(data)
    # Iterate over each element 'x' in 'data', calculate the squared difference from the mean, and sum these values.
    # Finally, divide by the number of elements in 'data' to get the variance.

def main():
    nlist = NumberList()
    # Choose one of the following methods to initialize data
    # nlist.getDataFromKeyboard()
    # nlist.getRandomData(5, 0, 10)  # Example: 5 random values in [0, 10)
    # nlist.getDataFromFile("dataFile.txt")  # Example file name

    nlist.getDataFromKeyboard()  # For example, we use getDataFromKeyboard here

    print("Numbers:", nlist.getData())
    print("Mean:", mean(nlist.getData()))
    print("Variance:", variance(nlist.getData()))

if __name__ == "__main__":
    main()
