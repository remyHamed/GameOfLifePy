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

    def generate_next_state(self):
        count = 0
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells)):
                for k in range(i - 1, i + 2):
                    for l in range(j - 1, j + 2):
                        if k == i and l == j:
                            continue
                        if k < 0 or l < 0:
                            continue
                        if k >= len(self.cells) or 1 >= len(self.cells):
                            continue
                        if self.cells[k][l].is_alive:
                            count += 1
                if self.cells[i][j].process_state(self.cells[i][j].is_alive, count):
                    self.temps_cells[i][j].is_alive = True
                else:
                    self.temps_cells[i][j].is_alive = False

                count = 0

        self.cells = self.temps_cell
        for i in range(0, len(self.cells)):
            for j in range(0, len(self.cells)):
                display = display + self.cells[i][j].to_string()
                if j < (len(self.cells) - 1):
                    display = display + " "
                if j == (len(self.cells) - 1) and i < (len(self.cells) - 1):
                    display = display + "\n"


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

