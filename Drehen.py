import glob
import time
import math
import tkinter

from tkinter import *
from tkinter.messagebox import showinfo

# Funktionen definieren-------------------------------------------------------------------------------------------------


def save():
    if not glob.glob("Drehen.csv"):
        ergebnisliste = open("Drehen.csv", "w")
        header = ["Datum", "Außendurchmesser", "Innendurchmesser", "Schnittgeschwindigkeit", "Drehzahl",
                  "Anlauf / Überlauf", "Werkstücklänge", "Anzahl der Schnitte", "Vorschub", "Hauptnutzungszeit"]
        ergebnisliste.write(header[0] + ";" + header[1] + ";" + header[2] + ";" + header[3] +
                            ";" + header[4] + ";" + header[5] + ";" + header[6] + ";" + header[7] + ";" + header[8] +
                            ";" + header[9] + "\n")
        lt = time.localtime()
        year, month, day = lt[0:3]
        datum = str(f"{day:02d}.{month:02d}.{year:4d}")

        ergebnisliste.write(datum + ";" +
                            str(outerDiameterInput.get()) + ";" +
                            str(innerDiameterInput.get()) + ";" +
                            str(rotationInput.get()) + ";" +
                            str(speedInput.get()) + ";" +
                            str(startupOverrunInput.get().replace(".", ",")) + ";" +
                            str(workpieceLengthInput.get()) + ";" +
                            str(numberOfCutsInput.get()) + ";" +
                            str(feedRateInput.get().replace(".", ",")) + ";" +
                            str(mainUsageTimeOutput.get()).replace(".", ",") + "\n")
        ergebnisliste.close()

    else:
        ergebnisliste = open("Drehen.csv", "a")
        lt = time.localtime()
        year, month, day = lt[0:3]
        datum = str(f"{day:02d}.{month:02d}.{year:4d}")

        ergebnisliste.write(datum + ";" +
                            str(outerDiameterInput.get()) + ";" +
                            str(innerDiameterInput.get()) + ";" +
                            str(rotationInput.get()) + ";" +
                            str(speedInput.get()) + ";" +
                            str(startupOverrunInput.get().replace(".", ",")) + ";" +
                            str(workpieceLengthInput.get()) + ";" +
                            str(numberOfCutsInput.get()) + ";" +
                            str(feedRateInput.get().replace(".", ",")) + ";" +
                            str(mainUsageTimeOutput.get()).replace(".", ",") + "\n")
        ergebnisliste.close()


def back():
    turnMenue.destroy()
    import UserInterface


def ende():
    turnMenue.destroy()


def reset():
    outerDiameterInput.delete(0, END)
    outerDiameterInput.focus_set()
    innerDiameterInput.delete(0, END)
    innerDiameterInput.insert(10, "0")
    speedInput.delete(0, END)
    speedInput.insert(10, "0")
    rotationInput.delete(0, END)
    rotationInput.insert(10, "0")
    startupOverrunInput.delete(0, END)
    startupOverrunInput.insert(10, "0")
    workpieceLengthInput.delete(0, END)
    workpieceLengthInput.insert(10, "0")
    numberOfCutsInput.delete(0, END)
    numberOfCutsInput.insert(10, "0")
    feedRateInput.delete(0, END)
    feedRateInput.insert(10, "0")
    mainUsageTimeOutput.delete(0, END)
    mainUsageTimeOutput.insert(10, "0")


def calculate():
    try:
        innerdiameter = float(innerDiameterInput.get().replace(",", "."))
        innerdiameter = float(innerdiameter)
        outerdiameter = float(outerDiameterInput.get().replace(",", "."))
        outerdiameter = float(outerdiameter)
        speed = float(speedInput.get().replace(",", "."))
        speed = float(speed)
        rotation = float(rotationInput.get().replace(",", "."))
        rotation = float(rotation)
        choice = turntype.get()
        length = float(workpieceLengthInput.get().replace(",", "."))
        length = float(length)
        cuts = float(numberOfCutsInput.get().replace(",", "."))
        cuts = float(cuts)
        speedperrotation = float(feedRateInput.get().replace(",", "."))
        speedperrotation = float(speedperrotation)
        startup = overrun = float(startupOverrunInput.get().replace(",", "."))
        startup = float(startup)
    except ValueError:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie ausschließlich Zahlen ein!")
        reset()

    if choice == 1:
        turnway = length + startup
        alternativediameter = outerdiameter - cuts * (speedperrotation + 1)
    elif choice == 2:
        turnway = length + startup + overrun
        alternativediameter = outerdiameter - cuts * (speedperrotation + 1)
    elif choice == 3:
        turnway = (outerdiameter - innerdiameter) / 2 + startup
        alternativediameter = (outerdiameter + innerdiameter) / 2 + startup
    else:
        turnway = (outerdiameter - innerdiameter) / 2 + startup + overrun
        alternativediameter = (outerdiameter + innerdiameter) / 2 + startup + overrun

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
        speed = (rotation * alternativediameter * math.pi) / 1000
        speedInput.delete(0, END)
        speedInput.insert(10, speed.__round__(2))
    else:
        rotation = (speed / (alternativediameter * math.pi)) * 1000
        rotationInput.delete(0, END)
        rotationInput.insert(10, rotation.__round__(2))

    mainusagetime = (math.pi * alternativediameter * turnway * cuts)/((speed * 1000) * speedperrotation)
    mainUsageTimeOutput.delete(0, END)
    mainUsageTimeOutput.insert(10, mainusagetime.__round__(2))


# Eingabefenster erstellen----------------------------------------------------------------------------------------------
turnMenue = Tk()
# Fenstername festlegen
turnMenue.title("Drehen")
# Label, Eingabefelder und Buttons erstellen und positionieren----------------------------------------------------------
# Außendurchmesser in mm------------------------------------------------------------------------------------------------
outerDiameterLabel = Label(turnMenue, text='Außendurchmesser [mm]').grid(row=0, column=0, padx=10, sticky='w')
outerDiameterInput = tkinter.Entry(turnMenue, width=10)
outerDiameterInput.grid(row=0, column=1)
# diameterInput.insert(10, "0")
outerDiameterInput.focus_set()
# Innendurchmesser in mm------------------------------------------------------------------------------------------------
innerDiameterLabel = Label(turnMenue, text='Innendurchmesser [mm]').grid(row=1, column=0, padx=10, sticky='w')
innerDiameterInput = tkinter.Entry(turnMenue, width=10)
innerDiameterInput.grid(row=1, column=1)
innerDiameterInput.insert(10, "0")
# Schnittgeschwindigkeit------------------------------------------------------------------------------------------------
speedLabel = Label(turnMenue, text='Schnittgeschwindigkeit [m/min]').grid(row=2, column=0, padx=10, sticky='w')
speedInput = tkinter.Entry(turnMenue, width=10)
speedInput.grid(row=2, column=1, pady=5)
speedInput.insert(10, "0")
# Drehzahl--------------------------------------------------------------------------------------------------------------
rotationLabel = Label(turnMenue, text='Drehzahl [1/min]', anchor='w').grid(row=3, column=0, padx=10, sticky='w')
rotationInput = tkinter.Entry(turnMenue, width=10)
rotationInput.grid(row=3, column=1, pady=5)
rotationInput.insert(10, "0")
# Anlauf / Überlauf-----------------------------------------------------------------------------------------------------
startupOverrunLabel = Label(turnMenue, text='Anlauf / Überlauf [mm]').grid(row=4, column=0, padx=10, sticky='w')
startupOverrunInput = tkinter.Entry(turnMenue, width=10)
startupOverrunInput.grid(row=4, column=1, pady=5)
startupOverrunInput.insert(10, "0")
# Werkstücklänge--------------------------------------------------------------------------------------------------------
workpieceLengthLabel = Label(turnMenue, text='Werkstücklänge [mm]').grid(row=0, column=3, padx=20, sticky='w')
workpieceLengthInput = Entry(turnMenue, width=10)
workpieceLengthInput.grid(row=0, column=4, padx=10, pady=5)
workpieceLengthInput.insert(10, "0")
# Anzahl der Schnitte---------------------------------------------------------------------------------------------------
numberOfCutsLabel = Label(turnMenue, text='Anzahl der Schnitte').grid(row=1, column=3, padx=20, sticky='w')
numberOfCutsInput = Entry(turnMenue, width=10)
numberOfCutsInput.grid(row=1, column=4, pady=5)
numberOfCutsInput.insert(10, "0")
# Vorschub je Umdrehung-------------------------------------------------------------------------------------------------
feedRateLabel = Label(turnMenue, text='Vorschub [mm]').grid(row=2, column=3, padx=20, sticky='w')
feedRateInput = Entry(turnMenue, width=10)
feedRateInput.grid(row=2, column=4, pady=5)
feedRateInput.insert(10, "0")
# Hauptnutzungszeit-----------------------------------------------------------------------------------------------------
mainUsageTimeLabel = Label(turnMenue, text='Hauptnutzungszeit [min]').grid(row=3, column=3, padx=20, sticky='w')
mainUsageTimeOutput = Entry(turnMenue, width=10)
mainUsageTimeOutput.grid(row=3, column=4, pady=5)
mainUsageTimeOutput.insert(10, "0")
# Auswahlschalter-------------------------------------------------------------------------------------------------------
turntype = IntVar()
turntype.set(1)
Radiobutton(turnMenue, text="Runddrehen mit Ansatz", variable=turntype, value=1).grid(row=5, column=0, sticky='w')
Radiobutton(turnMenue, text="Runddrehen ohne Ansatz", variable=turntype, value=2).grid(row=6, column=0, sticky='w')
Radiobutton(turnMenue, text="Plandrehen Vollzylinder", variable=turntype, value=3).grid(row=7, column=0, sticky='w')
Radiobutton(turnMenue, text="Plandrehen Hohlzylinder", variable=turntype, value=4).grid(row=8, column=0, sticky='w')
# Schalter--------------------------------------------------------------------------------------------------------------
buttonFrame = Frame(turnMenue)
buttonFrame.grid(row=9, columnspan=5)

calculateButton = Button(buttonFrame, text='Berechnen', width=10, command=calculate).grid(row=9, column=0, padx=5, pady=20)
resetButton = Button(buttonFrame, text='Zurücksetzen', width=10, command=reset).grid(row=9, column=1, padx=5, pady=20)
saveButton = Button(buttonFrame, text='Speichern', width=10, command=save).grid(row=9, column=2, padx=5, pady=20)
backButton = Button(buttonFrame, text='Zurück', width=10, command=back).grid(row=9, column=3, padx=5, pady=20)
exitButton = Button(buttonFrame, text='Beenden', width=10, command=ende).grid(row=9, column=4, padx=5, pady=20)

turnMenue.mainloop()
