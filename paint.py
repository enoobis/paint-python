from tkinter import *
from tkinter import filedialog
from PIL import ImageGrab

class PaintApp:
    def __init__(self, master):
        self.master = master
        master.title("Paint App")
        self.color = "white"
        self.create_widgets()
        self.create_menubar()

    def create_widgets(self):
        self.color_frame = Frame(self.master)
        self.color_frame.pack(side=LEFT)
        color_options = ["razer", "red", "green", "blue"]
        for color in color_options:
            btn = Button(self.color_frame, text=color.capitalize(), command=lambda c=color: self.change_color(c))
            btn.pack()

        self.canvas = Canvas(self.master, bg="black")
        self.canvas.pack(fill=BOTH, expand=True)
        self.canvas.bind("<B1-Motion>", self.paint)

    def change_color(self, new_color):
        self.color = new_color

    def paint(self, event):
        x1, y1 = (event.x - 2), (event.y - 2)
        x2, y2 = (event.x + 2), (event.y + 2)
        self.canvas.create_oval(x1, y1, x2, y2, fill=self.color, width=1)

    def create_menubar(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_canvas)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)

        edit_menu = Menu(menubar)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Undo", command=self.undo_action)
        edit_menu.add_command(label="Clear All", command=self.clear_canvas)

    def new_canvas(self):
        self.canvas.delete("all")

    def open_file(self):
        filename = filedialog.askopenfilename(defaultextension=".png", filetypes=[("All Files", "*.*"), ("PNG", "*.png"), ("JPEG", "*.jpg")])
        if filename:
            self.new_canvas()
            self.canvas.background = PhotoImage(file=filename)
            self.canvas.create_image(0, 0, image=self.canvas.background, anchor=NW)

    def save_file(self):
        filename = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("All Files", "*.*"), ("PNG", "*.png"), ("JPEG", "*.jpg")])
        if filename:
            x = self.master.winfo_rootx() + self.canvas.winfo_x()
            y = self.master.winfo_rooty() + self.canvas.winfo_y()
            x1 = x + self.canvas.winfo_width()
            y1 = y + self.canvas.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(filename)

    def undo_action(self):
        self.canvas.undo()

    def clear_canvas(self):
        self.canvas.delete("all")
root = Tk()
my_paint_app = PaintApp(root)
root.mainloop()

