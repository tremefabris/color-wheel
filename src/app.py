import tkinter

class ColorWheel():
        def __init__(self):
            super().__init__()

        def _create_window(self):
            self.root = tkinter.Tk()

            self.W_max = self.root.winfo_screenwidth()
            self.H_max = self.root.winfo_screenheight()

            self.W_button = 0
            self.H_button = 125

            self.root.geometry(
                f'{self.W_max}x{self.H_max}'
            )

        def initUI(self):
            self.root.title("Coloured Rects")

            self.canvas = tkinter.Canvas(master=self.root)
            
            self.display_rect = self.canvas.create_rectangle(
                0, 0, self.W_max - self.W_button, self.H_max - 0,
                outline='#ff1493',   # only first display color
                fill='#ff1493',      # only first display color
            )

            self.canvas.pack(fill=tkinter.BOTH, expand=1)

        def _create_buttons(self):
            
            red_button_label = tkinter.StringVar()
            red_button_label.set("Red")
            self.red_button = tkinter.Button(
                self.root,
                textvariable=red_button_label,
                command=self.__button_cmd_change_color_red,
            )
            self.red_button.pack()
            self.red_button.place(
                x=0,
                y=self.H_max - self.H_button + 22,
            )

            green_button_label = tkinter.StringVar()
            green_button_label.set("Green")
            self.green_button = tkinter.Button(
                self.root,
                textvariable=green_button_label,
                command=self.__button_cmd_change_color_green,
            )
            self.green_button.pack()
            self.green_button.place(
                x=60,
                y=self.H_max - self.H_button + 22,
            )

        def __button_cmd_change_color_red(self):
            self.canvas.itemconfig(
                self.display_rect,
                fill='#cc0000',
                outline='#cc0000',
            )
        def __button_cmd_change_color_green(self):
            self.canvas.itemconfig(
                self.display_rect,
                fill='#6aa84f',
                outline='#6aa84f',
            )

        def run(self):
            self._create_window()
            self.initUI()
            self._create_buttons()
            self.root.mainloop()