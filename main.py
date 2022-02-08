class Cell:

    #constructeur
    def __init__(self, value):
        self.is_alive = value

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = self.__check_value(value)

    @staticmethod
    def __check_value(value):
        value = isinstance(value, bool)
        if not value:
            raise AttributeError(f"value = {value} is not convertible to integer\n")
        else:
            return value


class Grid:

    #constructeur
    def __init__(self, cells, t_grid, square_size , display):
        self.square_size = square_size
        self.cells = cells

    @property
    def square_size(self):
        return self._square_size

    @square_size.setter
    def square_size(self, value):
        self._square_size = self.__check_square_size(value)

    def __check_square_size(self, value):
        try:
            value = int(value)
        except Exception:
            raise AttributeError(f"square_size = {value} is not convertible to integer")

        try:
            if value < 18:
                raise AttributeError(f"square_size = {value} is under 18")


    @property
        def cells(self):
            return self._cells

        @cells.setter
        def cells(self, value, self.squareSize):
            self._cells = self.__check_value(value, squareSize)

        @staticmethod
        def __check_value(value):
            res = isinstance(value, list)
            if not res:
                raise AttributeError(f"{value} is not a list")
            else:
                for cell in value:
                    res = isinstance(cell, Cell)
                    if not res:
                        raise AttributeError(f"")