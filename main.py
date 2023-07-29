from tkinter import *
from unit import Cell
import configure
import new




root = Tk()
# Override the configure of the window
root.configure(bg="grey")
root.geometry(f'{configure.WIDTH}x{configure.HEIGHT}')
root.title("Minesweeper Game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='#5D6D7E',
    width=configure.WIDTH,
    height=new.height_prct(25)
)
top_frame.place(x=0, y=0)

game_title = Label(
    top_frame,
    bg='#5D6D7E',
    fg='white',
    text='Minesweeper Game',
    font=('', 48)
)

game_title.place(
    x=new.width_prct(30), y=0
)

center_frame = Frame(
    root,
    bg='black',
    width=new.width_prct(75),
    height=new.height_prct(75)
)
center_frame.place(
    x=new.width_prct(30),
    y=new.height_prct(30),
)

for x in range(configure.GRID_SIZE):
    for y in range(configure.GRID_SIZE):
        c = Cell(x, y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid(
            column=x, row=y
        )
# Call the label from the Cell class
Cell.create_cell_count_label(top_frame)
Cell.cell_count_label_object.place(
    x=new.width_prct(42), y=new.height_prct(15)
)

Cell.randomize_mines()


# Run the window
root.mainloop()