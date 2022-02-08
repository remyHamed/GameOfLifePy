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

        if value < 18:
            raise AttributeError(f"square_size = {value} is under 18")


    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, tab):
        self._cells = self.__check_cells(tab)

    def __check_cells(self, tab):
        res = isinstance(tab, list)
        if not res:
            raise AttributeError(f"tab = {tab} is not a list")
        else:
            for cell in tab:
                res = isinstance(cell, Cell)
                if not res:
                    raise AttributeError(f"tab = {tab} need to contain cells only")

    @property
    def display(self):
        return self._display

    @cells.setter
    def display(self, tab):
        self._display = self.__check_display(tab)

    def __check_display(self, string):
        res = isinstance(string, str)
        if not res:
            raise AttributeError(f"string = {string} is not a string")
        #else:

   # ". . . .\n . X X .\n . X . . \n. . . .\n"

