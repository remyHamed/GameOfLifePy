import time
import random
import tkinter
from tkinter import *

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
        self._cells = [[]]
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
                raise AttributeError(f"square_size = {value} is under 18")
            return value
        except Exception:
            raise AttributeError(f"square_size = {value} is not convertible to integer")


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
        nwtab = [[]]
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
                    #print("vrai")
                    #self.temps_cells[m][j].set_alive(True) #is_alive(True)
                    nwtab[m].append(Cell(True))
                    #print(self.temps_cells[m][j].is_alive)
                else:
                    #print("false")
                    #self.temps_cells[m][j].set_alive(False) #is_alive(True)
                    nwtab[m].append(Cell(False))
                    #print(self.temps_cells[m][j].is_alive)
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


g = Grid(25)
print(g.square_size)
'''
print("1\n")
print("2\n")
g.show()

print("3\n\n")
g.generate_next_state()
g.show()
print("4\n\n")
g.generate_next_state()
g.show()

for i in range(0, 50):
    g.generate_next_state()
    g.show()
    print("-------------\n")

'''

# création de la fenetre
window = Tk()
window.title("Game Of Life") # titre
window.geometry("1080x720") # taille
window.minsize(1920, 1080) # taille minimal
window.iconbitmap("logo.ico") #logo (.ico obligatoire)
window.config(background="grey") # couleur de fond

#creation d'un composant
title = Label(window, text="Game Of Life", font=("Arial", 40), bg="white", fg="red")
title.pack() # ajoute le composant a la fenetre

#creation d'un second composant
subtitle = Label(window, text="Sa veut dire jeu de la vie en français !", font=("Arial", 10), bg="white", fg="red")
subtitle.pack()

#creation d'un composant qui va contenir notre grille
grid = Frame(window, bg="grey")
grid.pack()
# affichage de la grille

canvas_list = [[]]

def init_grid():
    canvas_list.clear()
    g.generate_next_state()
    for i in range(0, g.square_size):
        canvas_list.append([])
        for j in range(0, g.square_size):
            if(g.cells[i][j].is_alive):
                chosencolor = "black"
            else:
                chosencolor = "white"
            # canvas qui va nous servire a dessiner notre couleurs
            canvas = Canvas(grid, width=25, height=25, bg=chosencolor, highlightthickness=0)
            canvas.grid(row=i, column=j)
            canvas_list[i].append(canvas)

def refresh_grid():
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
    grid.after(100, refresh_grid)

init_grid()
refresh_grid()
window.mainloop()




