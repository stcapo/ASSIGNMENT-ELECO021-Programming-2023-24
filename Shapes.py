class Shape:
    def __init__(self, name):
        # Constructor for the Shape class.
        # Initializes a Shape instance with a given name.
        self.name = name

    def getName(self):
        # Returns the name of the shape.
        return self.name

    def toString(self):
        # Returns a string representation of the shape.
        # This method can be overridden in derived classes for more specific details.
        return f"Shape(Name: {self.name})"

    def getArea(self):
        # Placeholder method to calculate the area of the shape.
        # This method should be overridden in derived classes with specific area calculations.
        raise NotImplementedError

    def getVolume(self):
        # Placeholder method to calculate the volume of the shape (if applicable).
        # This method should be overridden in derived classes with specific volume calculations.
        raise NotImplementedError
class Circle(Shape):
    def __init__(self, radius):
        # Constructor for the Circle class, which inherits from Shape.
        # Calls the constructor of the Shape class with the name "Circle".
        # Initializes a Circle instance with a given radius.
        super().__init__("Circle")
        self.radius = radius

    def getArea(self):
        # Overrides the getArea method from the Shape class.
        # Calculates and returns the area of the circle.
        return 3.14159 * self.radius * self.radius

    def toString(self):
        # Overrides the toString method from the Shape class.
        # Returns a string representation of the circle with its radius.
        return f"Circle(Radius: {self.radius})"
    

class Square(Shape):
    def __init__(self, side):
        # Constructor for the Square class, which inherits from Shape.
        # Calls the constructor of the Shape class with the name "Square".
        # Initializes a Square instance with a given side length.
        super().__init__("Square")
        self.side = side

    def getArea(self):
        # Overrides the getArea method from the Shape class.
        # Calculates and returns the area of the square.
        return self.side * self.side

    def toString(self):
        # Overrides the toString method from the Shape class.
        # Returns a string representation of the square with its side length.
        return f"Square(Side: {self.side})"

def main():
    # Create a list to store shape instances
    shapes = []

    while True:
        # Display a menu to the user
        print("\nMenu:")
        print("1. Add a new Circle")
        print("2. Add a new Square")
        print("3. Show all Shapes")
        print("4. Exit")
        choice = input("Enter your choice: ")

        # Handle user's choice
        if choice == '1':
            # Add a new Circle
            radius = float(input("Enter the radius of the circle: "))
            shapes.append(Circle(radius))
            print("Circle added.")

        elif choice == '2':
            # Add a new Square
            side = float(input("Enter the side length of the square: "))
            shapes.append(Square(side))
            print("Square added.")

        elif choice == '3':
            # Show all Shapes
            print("\nShapes:")
            for shape in shapes:
                print(shape.toString() + ", Area: " + str(shape.getArea()))

        elif choice == '4':
            # Exit the program
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")

# Run the main function
if __name__ == "__main__":
    main()
