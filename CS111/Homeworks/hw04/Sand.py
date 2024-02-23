from Grid import Grid


class Sand:
    def __init__(self, grid, x=0, y=0):
        # initialize sand object
        self.grid = grid
        self.x = x
        self.y = y

    def __str__(self):
        # String rep of sand object
        return f"Sand({self.x},{self.y})"

    def is_move_ok(self, x_to, y_to):
        # Check to move sand
        if not self.grid.in_bounds(x_to, y_to):
            return False
        if self.grid.get(x_to, y_to) is not None:
            return False
        if self.x != x_to:
            return self.grid.get(x_to, self.y) is None
        return True

    def gravity(self):
        # where it will move based off the rules
        if self.is_move_ok(self.x, self.y + 1):  # Move down
            return self.x, self.y + 1
        elif self.is_move_ok(self.x - 1, self.y + 1):  # Move down-left
            return self.x - 1, self.y + 1
        elif self.is_move_ok(self.x + 1, self.y + 1):  # Move down-right
            return self.x + 1, self.y + 1
        else:
            return None

    def move(self, physics):
        # actually move the sand
        new_position = physics()
        if new_position is None:
            return

        # Clear the current position in the grid
        self.grid.set(self.x, self.y, None)

        # Update the Sand object's position
        self.x, self.y = new_position

        # Set the new position in the grid to a reference to the Sand object
        self.grid.set(self.x, self.y, self)


if __name__ == "__main__":
    pass
