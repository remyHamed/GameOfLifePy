import ast
from tkinter import filedialog as fd
import random
import tkinter
from tkinter import *

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
            raise AttributeError(f"value = {value} is not convertible to bool\n")
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
            return " X"
        else:
            return " ."


class Grid:
    # constructeur
    def __init__(self, square_size):
        self._square_size = square_size
        if is_file_needed:
            temp_grid = list(file_grid)
            self._cells = []
            self._cells.clear()
            for i in range(self._square_size):
                self._cells.append([])
                for j in range(self._square_size):
                    if temp_grid[i][j] == 'X':
                        self._cells[i].append(Cell(True))
                    if temp_grid[i][j] == 'O':
                        self._cells[i].append(Cell(False))
        else:
            self._cells = []
            self._cells.clear()
            for i in range(0, self._square_size):
                self._cells.append([])
                for j in range(0, self._square_size):
                    if random.randint(1, 10000) < 5000:
                        self._cells[i].append(Cell(False))
                    else:
                        self._cells[i].append((Cell(True)))
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
            if value < 18:
                raise ValueError()
            return value
        except AttributeError:
            raise AttributeError(f"square_size = {value} is not convertible to integer")
        except ValueError:
            raise ValueError(f"square_size = {value} is under 18")
    #def initial_cells(self):
        # for i in range(0, self.square_size):
        #    self.cells = [[Cell(False)]* self.square_size for i in range( self.square_size)]
        #    self.temps_cells.append([Cell(False) for x in range(0, self.square_size)])

    @property
    def cells(self):
        return self._cells

    @cells.setter
    def cells(self, tab):
        self._cells = tab

    def show(self):
        for m in range(0, self.square_size):
            for j in range(0, self.square_size):
                print(self.cells[m][j].to_string(), end='')
            print(' \n')

    def generate_next_state(self):
        count = 0
        nwtab = []
        nwtab.clear()
        for m in range(0, self.square_size): # 0
            nwtab.append([])
            for j in range(0, self.square_size): # 0
                for k in range(m - 1, m + 2): # 0
                    for l in range(j - 1, j + 2): # 1
                        if k == m and l == j:
                            continue
                        if k < 0 or l < 0:
                            continue
                        if k >= self.square_size or l >= self.square_size:
                            continue
                        if self.cells[k][l].is_alive:
                            count += 1
                if self.cells[m][j].process_state(self.cells[m][j].is_alive, count):
                    nwtab[m].append(Cell(True))
                else:
                    nwtab[m].append(Cell(False))
                count = 0
        
        self.cells = nwtab

                #self.display(new_string_display + str(self.cells[m][j].__str__))
                #if j < (len(self.cells) - 1):
                    #new_string_display = new_string_display + " "
                #if j == (len(self.cells) - 1) and m < (len(self.cells) - 1):
                    #new_string_display = new_string_display + "\n"
            #self.display(new_string_display)




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
    def display(self):
        return self._display

    @display.setter
    def display(self, string):
        self._display = string

   # def __check_display(self, string):
   #     res = isinstance(string, str)
   #     if not res:
   #         raise AttributeError(f"string = {string} is not a string")


is_file_needed = False
file_grid = []
g = Grid(20)
canvas_list = [[]]

class Window(tkinter.Tk):
    def __init__(self, *args, **kwargs):
        tkinter.Tk.__init__(self, *args, **kwargs)
        self.title("Game Of Life")  # titre
        self.geometry("1080x720")  # taille
        self.minsize(500, 300)  # taille minimal
        self.iconbitmap("logo.ico")  # logo (.ico obligatoire)
        self.config(background="grey")  # couleur de fond
        title = Label(self, text="Game Of Life", font=("Arial", 40), bg="grey", fg="white")
        title.pack()  # ajoute le composant a la fenetre
        self.container = tkinter.Frame(self)
        self.container.pack()
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)
        self.show_main_frame()

    def load_file(self):
        global file_grid
        global is_file_needed
        global g
        is_file_needed = True
        filename = fd.askopenfilename()
        filin = open(filename, "r")
        file_grid = (ast.literal_eval(s) for s in filin)
        file_grid = list(file_grid)
        cpt = 0
        for l in file_grid:
            cpt = cpt + 1
        g = Grid(cpt)
        self.show_grid_frame()


    def show_main_frame(self):
        frame = Main_frame(parent=self.container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

    def show_grid_frame(self):
        frame = Grid_frame(parent=self.container, controller=self)
        frame.grid(row=0, column=0, sticky="nsew")
        frame.tkraise()

class Main_frame(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        btn_load = tkinter.Button(self, text="Charger", command=lambda: controller.load_file())
        btn_load.pack()
        btn_generate = tkinter.Button(self, text="Générer", command=lambda: controller.show_grid_frame())
        btn_generate.pack()


class Grid_frame(tkinter.Frame):
    def __init__(self, parent, controller):
        tkinter.Frame.__init__(self, parent)
        self.controller = controller
        self.create_grid()
        self.refresh_grid()

    def create_grid(self):
        canvas_list.clear()
        g.generate_next_state()
        for i in range(0, g.square_size):
            canvas_list.append([])
            for j in range(0, g.square_size):
                if (g.cells[i][j].is_alive):
                    chosencolor = "black"
                else:
                    chosencolor = "white"
                # canvas qui va nous servire a dessiner notre couleurs
                canvas = Canvas(self, width=25, height=25, bg=chosencolor, highlightthickness=0)
                canvas.grid(row=i, column=j)
                canvas_list[i].append(canvas)

    def refresh_grid(self):
        g.generate_next_state()
        for k in range(g.square_size):
            for i in range(g.square_size):
                if (g.cells[k][i].is_alive):
                    chosencolor = "black"
                else:
                    chosencolor = "white"
                canvas = canvas_list[k][i]
                canvas.configure(bg=chosencolor)
                canvas_list[k][i] = canvas
        self.after(100, self.refresh_grid)

app = Window()
app.mainloop()