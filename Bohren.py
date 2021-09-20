import glob
import time
import csv
import math
import tkinter
import sys

from tkinter import *
from tkinter.messagebox import showinfo

# Funktionen definieren-------------------------------------------------------------------------------------------------


def save():
    if not glob.glob("Bohren.csv"):
        ergebnisliste = open("Bohren.csv", "w")
        header = ["Datum", "Werkzeugdurchmesser", "Drehzahl", "Schnittgeschwindigkeit", "Spitzenwinkel",
                  "Anzahl der Schnitte", "Vorschub je Umdrehung", "Bohrungstiefe", "Hauptnutzungszeit"]
        ergebnisliste.write(header[0] + ";" + header[1] + ";" + header[2] + ";" + header[3] +
                            ";" + header[4] + ";" + header[5] + ";" + header[6] + ";" + header[7] +
                            ";" + header[8] + "\n")
        lt = time.localtime()
        year, month, day = lt[0:3]
        datum = str(f"{day:02d}.{month:02d}.{year:4d}")

        ergebnisliste.write(datum + ";" +
                            str(diameterInput.get()) + ";" +
                            str(rotationInput.get()) + ";" +
                            str(speedInput.get().replace(".", ",")) + ";" +
                            str(firstCutList.get("active")) + ";" +
                            str(numberOfCutsInput.get()) + ";" +
                            str(feedRateInput.get().replace(".", ",")) + ";" +
                            str(drillDepthInput.get()) + ";" +
                            str(mainUsageTimeOutput.get()).replace(".", ",") + "\n")
        ergebnisliste.close()

    else:
        ergebnisliste = open("Bohren.csv", "a")
        lt = time.localtime()
        year, month, day = lt[0:3]
        datum = str(f"{day:02d}.{month:02d}.{year:4d}")

        ergebnisliste.write(datum + ";" +
                            str(diameterInput.get()) + ";" +
                            str(rotationInput.get()) + ";" +
                            str(speedInput.get().replace(".", ",")) + ";" +
                            str(firstCutList.get("active")) + ";" +
                            str(numberOfCutsInput.get()) + ";" +
                            str(feedRateInput.get().replace(".", ",")) + ";" +
                            str(drillDepthInput.get()) + ";" +
                            str(mainUsageTimeOutput.get()).replace(".", ",") + "\n")
        ergebnisliste.close()


def back():
    drillMenue.destroy()
    import UserInterface


def ende():
    drillMenue.destroy()


def calculate():
    try:
        diameter = float(diameterInput.get().replace(",", "."))
        diameter = float(diameter)
        rotation = float(rotationInput.get().replace(",", "."))
        rotation = float(rotation)
        speed = float(speedInput.get().replace(",", "."))
        speed = float(speed)
        choice = drilltype.get()
        drilldepth = float(drillDepthInput.get().replace(",", "."))
        drilldepth = float(drilldepth)
        firstcutangle = float(firstCutList.get("active"))
        firstcutangle = float(firstcutangle)
        startup = overrun = 1

        if firstcutangle == 80:
            firstcut = 0.6 * diameter
        elif firstcutangle == 118:
            firstcut = 0.3 * diameter
        elif firstcutangle == 130:
            firstcut = 0.23 * diameter
        else:
            firstcut = 0.18 * diameter

        cuts = float(numberOfCutsInput.get())
        cuts = float(cuts)
        speedperrotation = float(feedRateInput.get().replace(",", "."))
        speedperrotation = float(speedperrotation)
    except ValueError:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie ausschließlich Zahlen ein!")
        reset()

    if speed == 0 and rotation == 0:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie einen Wert für die Schnittgeschwindigkeit / Drehzahl ein.")
    elif speedperrotation == 0:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie einen Wert für den Vorschub ein!")
        feedRateInput.delete(0, END)
        feedRateInput.focus_set()
    elif speed != 0 and rotation != 0:
        speedInput.delete(0, END)
        speedInput.insert(10, speed.__round__(2))
        rotationInput.delete(0, END)
        rotationInput.insert(10, rotation.__round__(2))
    elif speed == 0:
        speed = (rotation * diameter * math.pi) / 1000
        speedInput.delete(0, END)
        speedInput.insert(10, speed.__round__(2))
    else:
        rotation = (speed / (diameter * math.pi)) * 1000
        rotationInput.delete(0, END)
        rotationInput.insert(10, rotation.__round__(2))

    if choice == 1:
        drillway = drilldepth + firstcut + startup + overrun

    else:
        drillway = drilldepth + firstcut + startup

    mainusagetime = (drillway * cuts)/(rotation * speedperrotation)
    mainUsageTimeOutput.delete(0, END)
    mainUsageTimeOutput.insert(10, mainusagetime.__round__(2))


def reset():
    diameterInput.delete(0, END)
    diameterInput.focus_set()
    speedInput.delete(0, END)
    speedInput.insert(10, "0")
    rotationInput.delete(0, END)
    rotationInput.insert(10, "0")
    drillDepthInput.delete(0, END)
    drillDepthInput.insert(10, "0")
    numberOfCutsInput.delete(0, END)
    numberOfCutsInput.insert(10, "0")
    feedRateInput.delete(0, END)
    feedRateInput.insert(10, "0")
    mainUsageTimeOutput.delete(0, END)
    mainUsageTimeOutput.insert(10, "0")


# Eingabefenster erstellen----------------------------------------------------------------------------------------------
drillMenue = Tk()
# Fenstername festlegen
drillMenue.title("Bohren")
# Label, Eingabefelder und Buttons erstellen und positionieren
# Bohrerdurchmesser in mm-----------------------------------------------------------------------------------------------
diameterLabel = Label(drillMenue, text='Werkzeugdurchmesser [mm]').grid(row=0, column=0, sticky='w')
diameterInput = tkinter.Entry(drillMenue, width=10)
diameterInput.grid(row=0, column=1)
# diameterInput.insert(10, "0")
diameterInput.focus_set()
# Drehzahl--------------------------------------------------------------------------------------------------------------
rotationLabel = Label(drillMenue, text='Drehzahl [1/min]', anchor='w').grid(row=1, column=0, sticky='w')
rotationInput = tkinter.Entry(drillMenue, width=10)
rotationInput.grid(row=1, column=1, pady=5)
rotationInput.insert(10, "0")
# Schnittgeschwindigkeit------------------------------------------------------------------------------------------------
speedLabel = Label(drillMenue, text='Schnittgeschwindigkeit ').grid(row=2, column=0, sticky='w')
speedInput = tkinter.Entry(drillMenue, width=10)
speedInput.grid(row=2, column=1, pady=5)
speedInput.insert(10, "0")
# Listbox---------------------------------------------------------------------------------------------------------------
firstcutLabel = Label(drillMenue, text='Spitzenwinkel [°]').grid(row=0, column=2, sticky='w')
scrollBar = Scrollbar(drillMenue, orient="vertical")
firstCutList = Listbox(drillMenue, height=1, yscrollcommand=scrollBar.set, width=10)
# firstCutList = Listbox(drillMenue, height=4)
scrollBar["command"] = firstCutList.yview
angle = ["80", "118", "130", "140"]

for a in angle:
    firstCutList.insert("end", a)

firstCutList.grid(row=0, column=3)
scrollBar.grid(row=0, column=4)
# Anzahl der Schnitte---------------------------------------------------------------------------------------------------
numberOfCutsLabel = Label(drillMenue, text='Anzahl der Schnitte').grid(row=1, column=2, sticky='w')
numberOfCutsInput = Entry(drillMenue, width=10)
numberOfCutsInput.grid(row=1, column=3, pady=5)
numberOfCutsInput.insert(10, "0")
# Vorschub je Umdrehung-------------------------------------------------------------------------------------------------
feedRateLabel = Label(drillMenue, text='Vorschub je Umdrehung [mm]').grid(row=2, column=2, sticky='w')
feedRateInput = Entry(drillMenue, width=10)
feedRateInput.grid(row=2, column=3, pady=5)
feedRateInput.insert(10, "0")
# Bohrungstiefe---------------------------------------------------------------------------------------------------------
drillDepthLabel = Label(drillMenue, text='Bohrungstiefe [mm]').grid(row=3, column=2, sticky='w')
drillDepthInput = Entry(drillMenue, width=10)
drillDepthInput.grid(row=3, column=3, pady=5)
drillDepthInput.insert(10, "0")
# Hauptnutzungszeit-----------------------------------------------------------------------------------------------------
mainUsageTimeLabel = Label(drillMenue, text='Hauptnutzungszeit [min]').grid(row=4, column=2, sticky='w')
mainUsageTimeOutput = Entry(drillMenue, width=10)
mainUsageTimeOutput.grid(row=4, column=3, pady=5)
mainUsageTimeOutput.insert(10, "0")
# Auswahlschalter-------------------------------------------------------------------------------------------------------
drilltype = IntVar()
drilltype.set(1)
Radiobutton(drillMenue, text="Durchgangsbohrung", variable=drilltype, value=1).grid(row=3, column=0, sticky='w')
Radiobutton(drillMenue, text="Grundlochbohrung", variable=drilltype, value=2).grid(row=4, column=0, sticky='w')
# Schalter--------------------------------------------------------------------------------------------------------------
buttonFrame = Frame(drillMenue)
buttonFrame.grid(row=9, columnspan=5)

calculateButton = Button(buttonFrame, text='Berechnen', width=10, command=calculate).grid(row=9, column=0, padx=5, pady=20)
resetButton = Button(buttonFrame, text='Zurücksetzen', width=10, command=reset).grid(row=9, column=1, padx=5, pady=20)
saveButton = Button(buttonFrame, text='Speichern', width=10, command=save).grid(row=9, column=2, padx=5, pady=20)
backButton = Button(buttonFrame, text='Zurück', width=10, command=back).grid(row=9, column=3, padx=5, pady=20)
exitButton = Button(buttonFrame, text='Beenden', width=10, command=ende).grid(row=9, column=4, padx=5, pady=20)

drillMenue.mainloop()
