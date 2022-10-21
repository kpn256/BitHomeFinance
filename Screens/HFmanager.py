import tkinter as tk
from constants import style
from Screens.HomeFinanceScreen import HomeFinance
from Screens.dcaScreen import Dca
import Manager




class Hfinance(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.InitWidget()

    def dcaFrame(self):
        self.controller.showFrame(Dca)
    def homefinanceFrame(self):
        self.controller.showFrame(HomeFinance)
    def back_home(self):
        self.controller.showFrame(Manager.Home)    
    

    def InitWidget(self):
        
        tk.Label(
            self,
            text = "HomeFinance",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.BOTH,
            expand = True,
            padx = 0.8,
            pady = 1,
        )
        tk.Label(
            self,
            text="Menu",
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=1,
            pady=1,)
        tk.Button(
            self,
            text="Persona Finance",
            **style.STYLE,
            command=self.homefinanceFrame,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,
            )
        tk.Button(
            self,
            text="DCA",
            **style.STYLE,
            command=self.dcaFrame,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,
            )
        
        home = tk.Button(
            self,
            text="HOME",
            **style.STYLE,
            command= self.back_home,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,
            )
            
