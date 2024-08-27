import tkinter as tk


class Sensors(tk.LabelFrame):
    # Constructor
    def __init__(self, parent):
        # Set variable
        super().__init__(
            parent,
            text="Sensors",
            background="white",
            borderwidth=2,
            labelanchor="n",
            padx=12,
            pady=12,
        )

        # Insert widget to parent
        self.place(relx=0, rely=0, relheight=0.7, relwidth=0.5)
