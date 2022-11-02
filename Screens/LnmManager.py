import tkinter as tk
from constants import style
from Screens.LnmTradingScreen import LnmTrading
import Manager
from Functions.LnmFunctions import Trading as Tr


class LnManager(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.InitWidget()

    def controlFrame(self):
        self.controller.showFrame(LnmTrading)

    def tradingFrame(self):
        self.controller.showFrame()

    def back_home(self):
        self.controller.showFrame(Manager.Home)

    def InitWidget(self):
# ----------------------------VARIABLES FUNTION------------------------

        user = Tr(
                key="tJlOA0pSR8PRTZksov3iqGhRbqaYktS4F5tbYK+dDQ8=",
                secret="I6d2pLEZln+yGHPXZzlGvN5XFCxsnDRQnllikA4JNTADPNct/3zMr7nLFJ593YUzCuKAsqfKZCXWGAkJrHdQ9w==",
                passphrase="9d0hb89h1e4e6")

        '''key = tk.StringVar()
        secret = tk.StringVar()
        passphrase = tk.StringVar()'''

        info_position = tk.StringVar()

        def log():
            user.login()
            user.show_status()
            return info_position.set(user.show_open_p())

# ---------------------------LogIn Widget-------------------------------------

        apikL = tk.Label(
                self,
                text="Api Key",
                justify=tk.CENTER,
                **style.STYLE)
        apikL.pack(
                side=tk.TOP,
                fill=tk.X,)
        apikE = tk.Entry(
                self,
                text="api Key:",
                **style.STYLE)
        apikE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        apikE.get()

        secretkL = tk.Label(
                self,
                text="secret",
                justify=tk.CENTER,
                **style.STYLE)
        secretkL.pack(
                side=tk.TOP,
                fill=tk.X,)
        secretkE = tk.Entry(
                self,
                text="secret:",
                **style.STYLE)
        secretkE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        secretkE.get()

        passkL = tk.Label(
                self,
                text="passphrase",
                justify=tk.CENTER,
                **style.STYLE)
        passkL.pack(
                side=tk.TOP,
                fill=tk.X,)
        passkE = tk.Entry(
                self,
                text="passphrase",
                **style.STYLE)
        passkE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        passkE.get()

        tk.Button(
                self,
                text="logIn",
                **style.STYLE,
                command=log,
                relief=tk.FLAT,
                activebackground=style.BACKGROUND,
                activeforeground=style.TEXT,
        ).pack(
            fill=tk.X,
            padx=1,
            pady=1,
        )

# ---------------------------buttoms labels -----------------------


# ___________________________tittle and subtittle______________________

        tk.Label(
            self,
            text="LNM Trading",
            textvariable=info_position,
            justify=tk.LEFT,
            wraplength=130,
            **style.STYLE
        ).pack(
            side=tk.TOP,
            fill=tk.BOTH,
            expand=True,
            padx=0.8,
            pady=1,
        )
# ________________________back button_______________

        tk.Button(
            self,
            text="HOME",
            **style.STYLE,
            command=self.back_home,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,)
