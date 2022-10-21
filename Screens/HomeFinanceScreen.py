
import tkinter as tk
from constants import style
from Screens.HomeScreen import * 
import Manager
from Functions.PersonalFinanceFunctions import pfLogic, total


class HomeFinance(tk.Frame):

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

        Selection = tk.StringVar()
        totalString = tk.StringVar()
        
        def spendSelect():

            Selection.set("spend")
            election = "s"
            
            pfLogic(election= election,date= str(dateE.get()),
                    amount= float(amountE.get()),note= str(noteE.get()))
            totalString.set(total())
                    
        def incomeSelect():
            Selection.set("income")
            election = "i"
            
            pfLogic(election= election,date= str(dateE.get()),
                    amount= float(amountE.get()),note= str(noteE.get()))
            totalString.set(total())
             
        def addInput():
            return "y"

        def finish():
            return "n"


            
#---------------------------bottoms labels -----------------------           
        
           
#___________________________tittle and subtittle______________________   

        tittle = tk.Label(
            self,
            text = "Personal Finance",
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

#________________________AMOUNT ____________________________________

        amountL = tk.Label(
            self,
            text="amount: ",
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

 #_____________________________NOTE_________________________

        noteL = tk.Label(
            self,
            text="note: ",
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=False,
            padx=1,
            pady=1,)

        noteE = tk.Entry(
            self,
            text="type youre note here",
            **style.STYLE)
        noteE.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        noteE.get()

#__________Spend Income Selection________________

        tittle = tk.Label(
            self,
            text = "Select spend or income:",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            expand = True,
            padx = 0.8,
            pady = 1,
        )
        
        income = tk.Button(
            self,
            text="income",
            **style.STYLE,
            command=incomeSelect,
        relief=tk.FLAT,
        activebackground=style.BACKGROUND,
        activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=1,
            pady=1,
            )
        
        spend = tk.Button(
            self,
            text="Spend",
            **style.STYLE,
            command=spendSelect,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=1,
            pady=1,
            )

        labelS = tk.Label(
                self,
                textvariable=Selection,
                justify= tk.CENTER,
                **style.STYLE
            ).pack(
                side = tk.TOP,
                fill = tk.X,
                expand = True,
                padx = 0.8,
                pady = 1,
            )
          
#________________________ Results Label ________________________________________

        dateL = tk.Label(
            self,
            text="DCA BALANCE",
            textvariable=totalString,
            justify=tk.CENTER,
            **style.STYLE,
        ).pack( side=tk.TOP,
            fill=tk.X,
            expand=True,
            padx=1,
            pady=1,)

#____________________________ADDINPUT FINISH BUTTON______________
 

        finish = tk.Button(
            self,
            text="finish",
            **style.STYLE,
            command=finish,
        relief=tk.FLAT,
        activebackground=style.BACKGROUND,
        activeforeground=style.TEXT
        ).pack(
            side=tk.TOP,
            fill=tk.X,
            padx=1,
            pady=1,
            )
    
#_______________________backButton_________________            
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
