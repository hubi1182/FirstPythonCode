from tkinter import *


def ende():
    mainMenue.destroy()


def bohrenoeffnen():
    mainMenue.destroy()
    import Bohren


def drehenoeffnen():
    mainMenue.destroy()
    import Drehen


def fraesenoeffnen():
    mainMenue.destroy()
    import Fraesen


# Hauptfenster erstellen
mainMenue = Tk()
# Name Fenster
mainMenue.title("Hauptmenü")

# Label und Buttons erstellen
bohrenButton = Button(mainMenue, text='Bohren', width=8, command=bohrenoeffnen).pack(padx=20, pady=5)
fraesenButton = Button(mainMenue, text='Fräsen', width=8, command=fraesenoeffnen).pack(pady=5)
drehenButton = Button(mainMenue, text='Drehen', width=8, command=drehenoeffnen).pack(pady=5)
exitButton = Button(mainMenue, text='Beenden', width=8, command=ende).pack(pady=5)

mainMenue.mainloop()
