import tkinter

class ColorWheel():
        # TODO: Create params passing to eliminate all hardcoded values
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

        def _display_color(self):
            self.root.title("Coloured Rects")

            self.canvas = tkinter.Canvas(master=self.root)
            
            self.display_rect = self.canvas.create_rectangle(
                0, 0, self.W_max - self.W_button, self.H_max - 0,
                outline='#90527a',   # only first display color
                fill='#90527a',      # only first display color
            )

            self.canvas.pack(fill=tkinter.BOTH, expand=1)

        def _create_entry(self):

            entry_label = tkinter.StringVar()
            entry_label.set("Color")
            self.entry_var = tkinter.StringVar()
            self.entry = tkinter.Entry(
                self.root,
                textvariable=self.entry_var,
                font=("calibre", 10, "normal"),
            )
            self.entry.pack()

            entry_button_label = tkinter.StringVar()
            entry_button_label.set("Change")
            self.entry_button = tkinter.Button(
                self.root,
                textvariable=entry_button_label,
                command=self.__entry_cmd_print_color,
            )
            self.entry_button.pack()

            self.entry.place(
                x=self.W_max - 230,
                y=self.H_max - self.H_button + 25,
            )
            self.entry_button.place(
                x=self.W_max - 80,
                y=self.H_max - self.H_button + 22,
            )

        @classmethod
        def __is_valid_rgb(cls, rgb_str: str):
            if len(rgb_str) != 7:
                return False

            try:
                return (  # this first check isn't needed
                    (rgb_str[0] == '#') and \
                    (int(rgb_str[1:3], 16) >= 0 and int(rgb_str[1:3], 16) < 256) and \
                    (int(rgb_str[3:5], 16) >= 0 and int(rgb_str[3:5], 16) < 256) and \
                    (int(rgb_str[5:], 16) >= 0 and int(rgb_str[5:], 16) < 256)
                )
            except ValueError:
                return False

        def __entry_cmd_print_color(self):
            new_color_str = self.entry_var.get()

            if new_color_str[0] != '#':
                new_color_str = f'#{new_color_str}'

            if not ColorWheel.__is_valid_rgb(new_color_str):
                print("Invalid RGB color; please, try again")
            else:
                self.canvas.itemconfig(
                    self.display_rect,
                    fill=new_color_str,
                    outline=new_color_str,
                )

            self.entry_var.set('')

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
            self._display_color()
            self._create_entry()
            self._create_buttons()
            self.root.mainloop()
