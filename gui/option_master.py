import tkinter as tk


class Options(tk.LabelFrame):
    # Constructor
    def __init__(self, parent):
        # Set variable
        super().__init__(
            parent,
            text="Options",
            background="white",
            borderwidth=2,
            labelanchor="n",
            padx=12,
            pady=12,
        )

        # Insert widget to parent
        self.place(relx=0.5, rely=0.7, relheight=0.3, relwidth=0.5)
