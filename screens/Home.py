import tkinter as tk
from constants import colors


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background = colors.BACKGROUND)
        self.controller = controller
        self.gameMode = tk.StringVar(self, value="Normal")
        #   Última función a llamar
        self.init_widgets()
        
    def move_to_game(self):
        self.controller.mode = self.gameMode.get()
        self.controller.show_frame(self.controller.game)

    def init_widgets(self):
        tk.Label(
            self,
            text = "Yo Nunca: THE GAME",
            justify = tk.CENTER,
            **colors.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
        optionsFrame = tk.Frame(self)
        optionsFrame.configure(background = colors.COMPONENT)
        optionsFrame.pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 22,
            pady = 11
        )
        tk.Label(
            optionsFrame,
            text = "Elige tu modo de Juego 🍉",
            justify = tk.CENTER,
            **colors.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )
        for (key, value) in colors.MODES.items():
            tk.Radiobutton(
                optionsFrame, 
                text = key + ("🔥" if key == "ATREVIDO" else ""), 
                variable = self.gameMode,
                value = value,
                activebackground = colors.BACKGROUND,
                activeforeground = colors.TEXT,
                **colors.STYLE).pack(
                    side = tk.LEFT,
                    fill = tk.BOTH,
                    expand = True,
                    padx = 5,
                    pady = 5
                )
        tk.Button(
            self, 
            text = "EMPEZAR!",
            command = self.move_to_game,
            **colors.STYLE,
            relief = tk.FLAT,
            activebackground = colors.BACKGROUND,
            activeforeground = colors.TEXT,
            ).pack(
            side = tk.TOP,
            fill = tk.X,
            padx = 22,
            pady = 11
        )