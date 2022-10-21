import tkinter as tk
from constants import style
import Manager
from Functions import functionsConverter as fc

class Converter(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.InitWidget()
        
    

    def back_home(self):
        self.controller.showFrame(Manager.Home)

    
#----------------------------WIDGETS-------------------------------------------------
    def InitWidget(self):

#---------------------------variables and functions-------------------------------------
        
        tikresult = tk.StringVar()
        fiatElec = tk.StringVar()
        satElec = tk.StringVar()
        

        def coinElec():
            tikresult.set(fc.priceRequest(coin=coinInput.get()))

        def fiatConversion():
            fiatElec.set(fc.fiatToSats(coin=coinInput.get(),amount=amountFiat.get(), prima=prima.get()))
    
        def satConversion():
            satElec.set(fc.satToFiat(sats=amountSats.get(),coin=coinInput.get(),prima=prima.get()))
         
            
            
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
        
#________________________prima_______________________________


        Prima =tk.Label(
            self,
            text="if you need add or substract a %\ntype it here:",
            **style.STYLE
        ).pack(
            fill=tk.X,
            padx=1,
            pady=1,)
        prima = tk.Entry(
            self,
            **style.STYLE)
        prima.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        prima.get()
#________________________FiatConversion__________________________

        FiatAmount =tk.Label(
            self,
            text="fiat amount",
            **style.STYLE
            ).pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        amountFiat = tk.Entry(
            self,
            text="amount Fiat: ",
            **style.STYLE)
        amountFiat.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        amountFiat.get()

        convertFiat = tk.Button(
            self,
            text="convert fiat/Sats",
            
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
            command= fiatConversion,
            ).pack(fill=tk.X,
                padx=1,
                pady=1,)
        resultConvert = tk.Label(
            self,
            **style.STYLE,  
            textvariable=fiatElec,
        ).pack(
            fill=tk.X,
            padx=1,
            pady=1,
        )


#_______________________satsConversion______________________________

        SatsAmount =tk.Label(
            self,
            text="sats amount",
            **style.STYLE
            ).pack(
                fill=tk.X,
                padx=1,
                pady=1,)

        amountSats = tk.Entry(
            self,
            text="amount sats:",
            **style.STYLE)
        amountSats.pack(
                fill=tk.X,
                padx=1,
                pady=1,)
        amountSats.get()

        convertSats = tk.Button(
            self,
            text="convert Sats/fiat",
            
            **style.STYLE,
            relief=tk.FLAT,
            activebackground=style.BACKGROUND,
            activeforeground=style.TEXT,
            command=satConversion,
            ).pack(fill=tk.X,
                padx=1,
                pady=1,
                )
        
        satresultConvert = tk.Label(
            self,
            **style.STYLE,  
            textvariable= satElec,
        ).pack(
            fill=tk.X,
            padx=1,
            pady=1,
            )
        

#_______________________HomeButton_________________
        
        tk.Button(
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

