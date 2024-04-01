from copy import deepcopy


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
        if 0 <= x < self.width and 0 <= y < self.height:
            return True
        else:
            pass
            #raise IndexError()

    def get(self, x, y):
        """
        Gets the value stored at (x, y).
        (x, y) should be in bounds.
        """
        if self.in_bounds(x, y):
            return self.array[y][x]
        else:
            pass
            #raise IndexError()

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
        str_lst = repr(self.array)
        return f"Grid.build({str_lst})"

    def __eq__(self, other):
        if isinstance(other, Grid):
            return self.array == other.array
        elif isinstance(other, list):
            return self.array == other

    def copy(self):
        return deepcopy(self)

    @staticmethod
    def check_list_malformed(lst):
        if not isinstance(lst, list):
            raise ValueError("You sucked")
        if len(lst) == 0:
            raise ValueError("You sucked")
        for item in lst:
            if not isinstance(item, list):
                raise ValueError("You sucked again")
            if len(item) != len(lst[0]):
                raise ValueError("You sucked again")

    @staticmethod
    def build(lst):
        Grid.check_list_malformed(lst)
        width = len(lst[0])
        height = len(lst)
        new_grid = Grid(width, height)
        new_grid.array = deepcopy(lst)
        # the .array thing doesn't overwrite
        # that variable, it is just mutating
        # the original one
        return new_grid


if __name__ == "__main__":
    pass
