import tkinter
from src.colorchooser import ColorChooser

class ColorWheel():

        def __init__(
            self,
            params: dict,
            color_table: dict = None,
        ):

            self.params = params

            if color_table is None:
                self.color_table = {
                    "red": "#ff0000",
                    "green": "#00ff00",
                    "blue": "#0000ff",
                    "pink": "#d7449a",
                    "white": "#ffffff",
                    "black": "#000000",
                }
            else:
                self.color_table = color_table

        ####### WINDOW METHODS #######

        def _create_window(self):
            self.root = tkinter.Tk()

            self.W_max = self.root.winfo_screenwidth()
            self.H_max = self.root.winfo_screenheight()

            self.W_button = self.params["W_button"]
            self.H_button = self.params["H_button"]

            self.root.geometry(
                f'{self.W_max}x{self.H_max}'
            )

        ####### MAIN RECT METHODS #######

        def _display_color(self):
            self.root.title("ColorWheel")

            self.canvas = tkinter.Canvas(master=self.root)

            self.display_rect = self.canvas.create_rectangle(
                0, 0, self.W_max - self.W_button, self.H_max,
                outline='#000000',   # only first display color
                fill='#000000',      # only first display color
            )

            self.canvas.pack(fill=tkinter.BOTH, expand=1)

        ####### CUSTOM COLOR ENTRY METHODS #######

        def _create_entry(self):

            entry_label = tkinter.StringVar()
            entry_label.set("Color")
            self.entry_var = tkinter.StringVar()
            self.entry = tkinter.Entry(
                self.root,
                textvariable=self.entry_var,
                font=(
                    self.params["font_name"],
                    self.params["font_size"],
                    self.params["font_type"],
                ),
            )
            self.entry.pack()

            entry_button_label = tkinter.StringVar()
            entry_button_label.set("Change")
            self.entry_button = tkinter.Button(
                self.root,
                textvariable=entry_button_label,
                command=self.__entry_cmd_change_color,
            )
            self.entry_button.pack()

            self.entry.place(
                x=self.W_max - self.params["x_entry_offset"],
                y=self.H_max - self.H_button + self.params["y_entry_offset"],
            )
            self.entry_button.place(
                x=self.W_max - self.params["x_entry_button_offset"],
                y=self.H_max - self.H_button + self.params["y_entry_button_offset"],
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
            except (ValueError, IndexError):
                return False

        def __entry_cmd_change_color(self):
            new_color_str = self.entry_var.get()

            if len(new_color_str) != 0 and new_color_str[0] != '#':
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

        ####### COLOR BUTTONS METHODS #######

        def _create_buttons(self):

            for i, (k, v) in enumerate(self.color_table.items()):
                button_label = tkinter.StringVar()
                button_label.set(k.capitalize())
                button = tkinter.Button(
                    self.root,
                    textvariable=button_label,
                    command=self.__button_cmd_color_change(v),
                )
                button.pack()
                button.place(
                    x=i * self.params["x_button_offset"],
                    y=self.H_max - self.H_button + self.params["y_button_offset"],
                )

            # Creating color chooser
            button_label_chooser = tkinter.StringVar()
            button_label_chooser.set("Choose Color")
            button_chooser = tkinter.Button(
                self.root,
                textvariable=button_label_chooser,
                command=self.__button_cmd_color_chooser,
            )
            button_chooser.pack()
            button_chooser.place(
                x=(i + 1) * self.params["x_button_offset"],
                y=self.H_max - self.H_button + self.params["y_button_offset"],
            )

        def __button_cmd_color_change(self, rgb_str: str):
            canvas = self.canvas
            display_rect = self.display_rect

            def __generic_color_change():
                canvas.itemconfig(
                    display_rect,
                    fill=rgb_str,
                    outline=rgb_str,
                )
            return __generic_color_change

        def __button_cmd_color_chooser(self):
            from tkinter.colorchooser import askcolor

            selected_color = askcolor(title="Choose Color")[-1]
            self.canvas.itemconfig(
                self.display_rect,
                fill=selected_color,
                outline=selected_color,
            )


        ####### MAIN FUNC #######

        def run(self):
            self._create_window()
            self._display_color()
            self._create_entry()
            self._create_buttons()
            self.root.mainloop()
