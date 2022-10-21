import tkinter as tk
from constants import style
import Manager
from Functions.LnmFunctions import Trading as Tr



class LnmTrading(tk.Frame):

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.configure(background=style.BACKGROUND)
        self.controller = controller
        self.InitWidget()

    def back_home(self):
        self.controller.showFrame(Manager.LnManager)

#----------------------------WIDGETS-------------------------------------------------
    
    def InitWidget(self):

#----------------------------VARIABLES FUNTION------------------------   
   
        
            
            
                
        


#---------------------------buttoms labels -----------------------           


#___________________________tittle and subtittle______________________   


        tk.Label(
            self,
            text = "LNM Trading",
            justify= tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            expand = True,
            padx = 0.8,
            pady = 1,
            )    

#________________________POSITIONS INFO_________________

        tk.Label(
            self,
            text= "position information",
            
            justify=tk.CENTER,
            **style.STYLE
        ).pack(
            side = tk.TOP,
            fill = tk.X,
            expand = True,
            padx = 0.8,
            pady = 1,
            )





#_______________________HomeButton_________________

        tk.Button(
            self,
            text= "Back",
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
