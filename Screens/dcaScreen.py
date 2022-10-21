import tkinter as tk
from constants import style
from Screens.HomeScreen import * 
import Manager
from Functions import DcaFunctions as dca
from Functions.functionsConverter import priceRequest




class Dca(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.InitWidget()


    def back_homeHF(self):
        self.controller.showFrame(Manager.Hfinance)


#----------------------------WIDGETS-------------------------------------------------
    
    def InitWidget(self):


#---------------------------variables and functions------------------------------------

        tikresult = tk.StringVar()
        totaldca =tk.StringVar()
        dcaresult = tk.StringVar()

        def dcaInput():
            dcaresult.set(dca.infoInput(coin=coinInput.get(),date=dateE.get(),sats=amountE.get(),fiat=fiatE.get()))

        def dcaTotal():
            totaldca.set(dca.total(coin=coinInput.get()))
       
        def coinElec():
            tikresult.set(priceRequest(coin=coinInput.get()))

#---------------------------buttoms labels entrys--------------------------------             


#___________________________tittle and subtittle______________________   

        tittle = tk.Label(
        
            self,
            text = "DCA BALANCE",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            expand = True,
            padx = 0.8,
            pady = 1,
        )
        subTittle = tk.Label(
            self,
            text="Input information",
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=1,
            pady=1,)

#________________________CoinSelection________________________

        LabelcoinElection=tk.Label(
            self,
            text="choose fiat currency",
            **style.STYLE
        ).pack(
            fill=tk.X,
            padx=1,
            pady=1,)

        coinInput= tk.Entry(
            self,
            text="choose fiat currency",
            **style.STYLE)
        coinInput.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        coinInput.get()

        cointick = tk.Button(
            self,
            text="select",
            command= coinElec,
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(fill=tk.X,
                padx=1,
                pady=1,)
        
        resultPrice = tk.Label(
            self,
            **style.STYLE,
            textvariable=tikresult,
        ).pack(
            fill=tk.X,
            padx=1,
            pady=1,
            )

#____________________________DATE ____________________________

        dateL = tk.Label(
            self,
            text="date: ",
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=1,
            pady=1,)
        dateE = tk.Entry(
            self,
            text="type youre buy date",
            **style.STYLE)
        dateE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        dateE.get()

#________________________Fiat ____________________________________

        fiatL = tk.Label(
            self,
            text="amount fiat: ",
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=1,
            pady=1,)
        fiatE = tk.Entry(
            self,
            text="type dca fiat amount",
            **style.STYLE)
        fiatE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        fiatE.get()

#________________________SATS____________________________________

        amountL = tk.Label(
            self,
            text="amount sats: ",
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=1,
            pady=1,)
        amountE = tk.Entry(
            self,
            text="type dca sat amount",
            **style.STYLE)
        amountE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        amountE.get()

#____________________________submmit Button_______________________

        tk.Button(
            self,
            text="Submmit",
            **style.STYLE,
            command=dcaInput,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,
            )
#________________________ Results Label ________________________________________

        dateL = tk.Label(
            self,
            text="DCA BALANCE",
            textvariable=dcaresult,
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=1,
            pady=1,)

#____________________________ FINISH BUTTON______________
 

        finish = tk.Button(
            self,
            text="finish",
            **style.STYLE,
            command=dcaTotal,
        relief=tk.FLAT,
        activebackground=style.BACKGROUND,
        activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=1,
            pady=1,
            )

#_______________________HomeButton_________________            
        tk.Button(
            self,
            text="Back",
            **style.STYLE,
            command= self.back_homeHF,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
            ).pack(
                side=tk.TOP,
                fill=tk.X,
                padx=1,
                pady=1,
            )
