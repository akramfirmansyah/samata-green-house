# Import library
import tkinter as tk
from sensor_master import Sensors
from graph_master import Graph
from actuator_master import Actuator
from option_master import Options


class Window(tk.Tk):
    # Constructor
    def __init__(self, title: str, sizes: tuple | list, isFullscreen: bool):
        # Set variable
        super().__init__()
        self.width = sizes[0]
        self.height = sizes[1]
        self.isFullscreen = isFullscreen

        # Config window
        self.title(title)
        self.geometry(f"{self.width}x{self.height}+0+0")
        self.wm_minsize(self.width, self.height)
        self.wm_attributes("-zoomed", self.isFullscreen)
        self.config(bg="white", padx=12, pady=4)

        # Widgets
        self.sensors = Sensors(self)
        self.graph = Graph(self)
        self.actuator = Actuator(self)
        self.option = Options(self)

        # Set keybind for window
        self.bind("<F11>", self.toggle_fullscreen)
        self.bind("<Escape>", self.close_application)

        # Run window
        self.mainloop()

    def toggle_fullscreen(self, event=None):
        """
        Function for handle toggle fullscreen mode
        """

        self.isFullscreen = not self.isFullscreen

        if self.isFullscreen:
            self.wm_attributes("-zoomed", self.isFullscreen)
        else:
            self.wm_attributes("-zoomed", self.isFullscreen)

    def close_application(self, event=None):
        """
        Function for close GUI
        """
        self.destroy()


# Run app
if __name__ == "__main__":
    Window("Skypian Gamma", (800, 480), False)
