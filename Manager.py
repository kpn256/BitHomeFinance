from turtle import Screen
from Screens.LnmManager import LnManager
from constants import style
import tkinter as tk
from Screens.HomeScreen import Home
from Screens.HFmanager import Hfinance
from Screens.LnmTradingScreen import LnmTrading
from Screens.ConverterScreen import Converter
from Screens.HomeFinanceScreen import HomeFinance
from Screens.dcaScreen import Dca
from Screens import *

class Manager(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.title("BITHOMEFINANCE")
        container = tk.Frame(self)
        container.pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True
        )
        container.configure(background=style.BACKGROUND)
        container.grid_columnconfigure(0, weight=1)
        container.grid_rowconfigure(0, weight=1)

        self.frames = {}
        for F in (Home,Hfinance,LnmTrading,Converter,HomeFinance,Dca,LnManager):
            frame = F(container, self)
            self.frames[F] = frame 
            frame.grid(row=0, column=0, sticky=tk.NSEW)
        self.showFrame(Home)

    def showFrame(self, container):
        frame = self.frames[container]
        frame.tkraise()


