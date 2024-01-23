import random

'''
In this class, various methods are provided for initializing the dataset: 
setData for setting data directly, getDataFromKeyboard for reading data from keyboard input, 
getRandomData for generating random data, and getDataFromFile for reading data from a file. 
The class uses private and public methods, static methods, exception handling, and file I/O operations, 
'''

class NumberList:
    def __init__(self):
        # Constructor of the NumberList class.
        # Initializes a private variable '__data' as an empty list to store the dataset.
        self.__data = []

    def getData(self):
        # Public method to access the data.
        # Returns the data stored in the private variable '__data'.
        return self.__data

    def setData(self, data):
        # Public method to set the data.
        # Takes an external list 'data' and sets it as the value of the private variable '__data'.
        self.__data = data

    @staticmethod
    def _getNDataFromKeyboard():
        # Static method (doesn't require class instance) to get the number of data elements from the user.
        # This is a "private" method as indicated by the underscore at the beginning.
        print("Enter the number of data set elements: ")
        while True:
            try:
                ndata = int(input())  # Attempt to read an integer from user input.
                if ndata >= 2:
                    return ndata  # Return the value if it's an integer and greater than or equal to 2.
                else:
                    print("ndata should be >= 2")  # Print error message if ndata is less than 2.
            except ValueError:
                # Handle the case where the input is not an integer.
                print("ndata should be an integer!")

    def getDataFromKeyboard(self):
        # Public method to allow the user to input a list of data elements from the keyboard.
        ndata = self._getNDataFromKeyboard()  # Get the number of data elements.
        print("Enter {} data elements:".format(ndata))
        for _ in range(ndata):  # Loop through the number of elements.
            while True:
                try:
                    data_value = float(input())  # Attempt to read a float value from user input.
                    self.__data.append(data_value)  # Add the value to the '__data' list.
                    break  # Break the loop after successfully adding the value.
                except ValueError:
                    # Handle the case where the input is not a valid number.
                    print("Please enter a valid number.")

    def getRandomData(self, ndata, range1, range2=0):
        # Public method to generate random data.
        # 'ndata' is the number of data elements, 'range1' and 'range2' define the range of random values.
        # 'range2' is optional and defaults to 0. If 'range2' is 0, it's set to 'range1' and 'range1' is set to 0.
        if range2 == 0:
            range2, range1 = range1, 0
        if range1 >= range2:
            # Check if 'range1' is less than 'range2'.
            print("Error: range1 should be less than range2")
            return
        # Generate 'ndata' random numbers within the specified range and store them in '__data'.
        self.__data = [random.uniform(range1, range2) for _ in range(ndata)]

    def getDataFromFile(self, fileName):
        # Public method to read data from a file.
        # 'fileName' is the path to the file containing the data.
        try:
            with open(fileName, 'r') as file:  # Open the file in read mode.
                for line in file:
                    # Strip each line to remove whitespace and newline characters, then convert to float and append to '__data'.
                    self.__data.append(float(line.strip()))
        except Exception as e:
            # Handle exceptions such as file not found, unable to convert to float, etc.
            print("Error reading file:", e)
