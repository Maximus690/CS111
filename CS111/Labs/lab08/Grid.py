class Grid:
    def __init__(self, width, height):
        """
        Create grid `array` width by height. Create a Grid object with
        a width, height, and array. Initially all locations hold None.
        """
        self.width = width
        self.height = height
        self.array = [[None] * width for _ in range(height)]

    def in_bounds(self, x, y):
        """Check if (x, y) is within bounds."""
        return 0 <= x < self.width and 0 <= y < self.height

    def get(self, x, y):
        """
        Gets the value stored at (x, y).
        (x, y) should be in bounds.
        """
        if not self.in_bounds(x, y):
            print("Error: Coordinates out of bounds.")
            return None
        return self.array[y][x]

    def set(self, x, y, val):
        """
        Sets a new value into the grid at (x, y).
        (x, y) should be in bounds.
        """
        if not self.in_bounds(x, y):
            print("Error: Coordinates out of bounds.")
            return
        self.array[y][x] = val

    def __str__(self):
        first_element = self.get(0, 0)
        return f"Grid({self.height}, {self.width}, first = {first_element})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if not isinstance(other, Grid):
            return False
        return self.array == other.array
# Testing the Grid class


if __name__ == "__main__":
    pass
