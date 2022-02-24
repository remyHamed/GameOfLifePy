import time
import random

def current_milli_time():
    return round(time.time() * 1000)


class Cell:

    # constructeur
    def __init__(self, value):
        self._is_alive = value

    @property
    def is_alive(self):
        return self._is_alive

    @is_alive.setter
    def is_alive(self, value):
        self._is_alive = self.__check_value(value)

    def __check_value(self, value):
        value = isinstance(value, bool)
        if not value:
            raise AttributeError(f"value = {value} is not convertible to integer\n")
        else:
            return value

    def process_state(self, is_alive, nb_neighbour_cells_alive):

        if is_alive and (nb_neighbour_cells_alive == 2 or nb_neighbour_cells_alive == 3):
            return True

        if not is_alive and nb_neighbour_cells_alive == 3:
            return True

        return False

    def to_string(self):
        if self.is_alive:
            return "X"
        else:
            return "."


class Grid:

    # constructeur
    def __init__(self, square_size):
        self._square_size = square_size
        for i in range(0, self.square_size):
            self._cells = [[Cell(False)] * self.square_size for i in range(self.square_size)]
        for i in range(0, self.square_size):
            self._temps_cells = [[Cell(False)] * self.square_size for i in range(self.square_size)]
        self._display = " "

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

    def initial_cells(self):
        # for i in range(0, self.square_size):
        #    self.cells = [[Cell(False)]* self.square_size for i in range( self.square_size)]
        #    self.temps_cells.append([Cell(False) for x in range(0, self.square_size)])

        for i in range(0, self._square_size):
            for j in range(0, self._square_size):
                self.cells[i][j] = Cell(False)

        for i in range(0, self._square_size):
            for j in range(0, self._square_size,2):
                if random.randint(1, 100) % 2 == 0 and current_milli_time() % 2 == 0:
                    self.cells[i][j] = Cell(False)
                    print("mort")
                else:
                    self.cells[i][j] = Cell(True)
                    print("vivant")

    def show(self):
        for m in range(0, len(self.cells)):
            for j in range(0, len(self.cells)):
                print(self.cells[m][j].to_string(), end='')
            print(' \n')

    def generate_next_state(self):
        count = 0
        for m in range(0, len(self.cells)):
            for j in range(0, len(self.cells)):
                for k in range(m - 1, m + 2):
                    for l in range(j - 1, j + 2):
                        if k == m and l == j:
                            continue
                        if k < 0 or l < 0:
                            continue
                        if k >= len(self.cells) or l >= len(self.cells):
                            continue
                        if self.cells[k][l].is_alive:
                            count += 1
                if self.cells[m][j].process_state(self.cells[m][j].is_alive, count):
                    self.temps_cells[m][j].is_alive = True #is_alive(True)
                else:
                    self.temps_cells[m][j].is_alive = False #is_alive(True)
                count = 0

        self.cells = self.temps_cells.copy()

        new_string_display = ""
        for m in range(0, len(self.cells)):
            for j in range(0, len(self.cells)):
                print(self.cells[m][j].to_string(), end='')
            print(' \n', end='')
                #self.display(new_string_display + str(self.cells[m][j].__str__))
                #if j < (len(self.cells) - 1):
                    #new_string_display = new_string_display + " "
                #if j == (len(self.cells) - 1) and m < (len(self.cells) - 1):
                    #new_string_display = new_string_display + "\n"
            #self.display(new_string_display)


    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, string):
        self._cells = string

    # def __check_cells(self, tab):
    #    res = isinstance(tab, list)
    #    if not res:
    #       raise AttributeError(f"tab = {tab} is not a list")
    # else:
    #   for cell in tab:
    #      res = isinstance(cell, Cell)
    #     if not res:
    #        raise AttributeError(f"tab = {tab} need to contain cells only")

    @property
    def temps_cells(self):
        return self._temps_cells

    @temps_cells.setter
    def temps_cells(self, tab):
        self._temps_cells = tab

    @property
    def display(self):
        return self._display

    @display.setter
    def display(self, string):
        self._display = string

   # def __check_display(self, string):
   #     res = isinstance(string, str)
   #     if not res:
   #         raise AttributeError(f"string = {string} is not a string")


g = Grid(20)
print(g.square_size)
print("1\n")
g.initial_cells()
print("2\n")
g.show()
print("3\n\n")
g.generate_next_state()
g.show()

#for i in range(0, 50):
    #g.generate_next_state()
    #print("\n")
