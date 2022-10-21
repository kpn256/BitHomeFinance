
import tkinter as tk
from Screens.LnmManager import LnManager
from constants import style
from Screens.ConverterScreen import Converter
from Screens.HFmanager import Hfinance
from Screens.LnmTradingScreen import LnmTrading
from Screens.ConverterScreen import Converter
from Screens import *


class Home(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.InitWidget()

    
    def btcConverter(self):
        self.controller.showFrame(Converter)
    def homefinance(self):
        self.controller.showFrame(Hfinance)
    def lnmtrading(self):
        self.controller.showFrame(LnManager)

    def InitWidget(self):
        
        tk.Label(
            self,
            text = "BITHOMEFINANCE",
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
            text="Btc Converter",
            **style.STYLE,
            command=self.btcConverter,
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
            text="Home Finance",
            **style.STYLE,
            command=self.homefinance,
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
            text="LNM Trading",
            **style.STYLE,
            command=self.lnmtrading, 
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,
            )
