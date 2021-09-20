import glob
import time
import math
import tkinter

from tkinter import *
from tkinter.messagebox import showinfo
# Funktionen definieren-------------------------------------------------------------------------------------------------


def save():
    if not glob.glob("Fraesen.csv"):
        ergebnisliste = open("Fraesen.csv", "w")
        header = ["Datum", "Fräserdurchmesser", "Spanungstiefe", "Zähnezahl des Fräsers", "Drehzahl",
                  "Anlauf / Überlauf", "Werkstücklänge", "Anzahl der Schnitte", "Vorschub je Fräserzahn",
                  "Werkstückbreite", "Nuttiefe", "Hauptnutzungszeit"]
        ergebnisliste.write(header[0] + ";" + header[1] + ";" + header[2] + ";" + header[3] +
                            ";" + header[4] + ";" + header[5] + ";" + header[6] + ";" + header[7] +
                            ";" + header[8] + ";" + header[9] + ";" + header[10] + ";" + header[11] +
                            "\n")
        lt = time.localtime()
        year, month, day = lt[0:3]
        datum = str(f"{day:02d}.{month:02d}.{year:4d}")

        if milltype == 1 or milltype == 2:
            ergebnisliste.write(datum + ";" +
                                str(diameterInput.get()) + ";" +
                                str(cuttingDepthInput.get()) + ";" +
                                str(numberOfTeethInput.get()) + ";" +
                                str(rotationInput.get()) + ";" +
                                str(startupOverrunInput.get().replace(".", ",")) + ";" +
                                str(workpieceLengthInput.get()) + ";" +
                                str(numberOfCutsInput.get()) + ";" +
                                str(feedRateInput.get().replace(".", ",")) + ";" + "-" + ";" + "-" + ";" +
                                str(mainUsageTimeOutput.get().replace(".", ",")) + "\n")

            ergebnisliste.close()
        elif milltype == 3:
            ergebnisliste.write(datum + ";" +
                                str(diameterInput.get()) + ";" +
                                str(cuttingDepthInput.get()) + ";" +
                                str(numberOfTeethInput.get()) + ";" +
                                str(rotationInput.get()) + ";" +
                                str(startupOverrunInput.get().replace(".", ",")) + ";" +
                                str(workpieceLengthInput.get()) + ";" +
                                str(numberOfCutsInput.get()) + ";" +
                                str(feedRateInput.get().replace(".", ",")) + ";" +
                                str(widthInput.get()) + ";" + "-" + ";" +
                                str(mainUsageTimeOutput.get().replace(".", ",")) + "\n")
            ergebnisliste.close()
        else:
            ergebnisliste.write(datum + ";" +
                                str(diameterInput.get()) + ";" +
                                str(cuttingDepthInput.get()) + ";" +
                                str(numberOfTeethInput.get()) + ";" +
                                str(rotationInput.get()) + ";" +
                                str(startupOverrunInput.get().replace(".", ",")) + ";" +
                                str(workpieceLengthInput.get()) + ";" +
                                str(numberOfCutsInput.get()) + ";" +
                                str(feedRateInput.get().replace(".", ",")) + ";" + "-" + ";" +
                                str(grooveDepthInput.get()) + ";" +
                                str(mainUsageTimeOutput.get()).replace(".", ",") + "\n")
            ergebnisliste.close()

    else:
        ergebnisliste = open("Fraesen.csv", "a")
        lt = time.localtime()
        year, month, day = lt[0:3]
        datum = str(f"{day:02d}.{month:02d}.{year:4d}")

        if milltype == 1 or milltype == 2:
            ergebnisliste.write(datum + ";" +
                                str(diameterInput.get()) + ";" +
                                str(cuttingDepthInput.get()) + ";" +
                                str(numberOfTeethInput.get()) + ";" +
                                str(rotationInput.get()) + ";" +
                                str(startupOverrunInput.get().replace(".", ",")) + ";" +
                                str(workpieceLengthInput.get()) + ";" +
                                str(numberOfCutsInput.get()) + ";" +
                                str(feedRateInput.get().replace(".", ",")) + ";" + "-" + ";" + "-" + ";" +
                                str(mainUsageTimeOutput.get().replace(".", ",")) + "\n")

            ergebnisliste.close()
        elif milltype == 3:
            ergebnisliste.write(datum + ";" +
                                str(diameterInput.get()) + ";" +
                                str(cuttingDepthInput.get()) + ";" +
                                str(numberOfTeethInput.get()) + ";" +
                                str(rotationInput.get()) + ";" +
                                str(startupOverrunInput.get().replace(".", ",")) + ";" +
                                str(workpieceLengthInput.get()) + ";" +
                                str(numberOfCutsInput.get()) + ";" +
                                str(feedRateInput.get().replace(".", ",")) + ";" +
                                str(widthInput.get()) + ";" + "-" + ";" +
                                str(mainUsageTimeOutput.get().replace(".", ",")) + "\n")
            ergebnisliste.close()
        else:
            ergebnisliste.write(datum + ";" +
                                str(diameterInput.get()) + ";" +
                                str(cuttingDepthInput.get()) + ";" +
                                str(numberOfTeethInput.get()) + ";" +
                                str(rotationInput.get()) + ";" +
                                str(startupOverrunInput.get().replace(".", ",")) + ";" +
                                str(workpieceLengthInput.get()) + ";" +
                                str(numberOfCutsInput.get()) + ";" +
                                str(feedRateInput.get().replace(".", ",")) + ";" + "-" + ";" +
                                str(grooveDepthInput.get()) + ";" +
                                str(mainUsageTimeOutput.get()).replace(".", ",") + "\n")
            ergebnisliste.close()


def back():
    millMenue.destroy()
    import UserInterface


def ende():
    millMenue.destroy()


def selection():

    if milltype.get() == 4:
        roughingFinishingFrame.grid_forget()
        slottedHolesFrame.grid(row=5, column=3, sticky='w')
        method.set(3)
        widthFrame.grid_forget()
        widthInput.grid_forget()
        grooveDepthFrame.grid(row=3, column=3, sticky='w')
        grooveDepthInput.grid(row=3, column=4)
        millMenue.update()
    elif milltype.get() == 3:
        grooveDepthFrame.grid_forget()
        grooveDepthInput.grid_forget()
        widthFrame.grid(row=3, column=3, sticky='w')
        widthInput.grid(row=3, column=4, pady=5)
        method.set(1)
        slottedHolesFrame.grid_forget()
        roughingFinishingFrame.grid(row=5, column=3, sticky='w')
        millMenue.update()
    else:
        method.set(1)
        slottedHolesFrame.grid_forget()
        grooveDepthFrame.grid_forget()
        grooveDepthInput.grid_forget()
        widthFrame.grid_forget()
        widthInput.grid_forget()
        roughingFinishingFrame.grid(row=5, column=3, sticky='w')
        millMenue.update()


def reset():
    diameterInput.delete(0, END)
    diameterInput.focus_set()
    cuttingDepthInput.delete(0, END)
    cuttingDepthInput.insert(10, "0")
    numberOfTeethInput.delete(0, END)
    numberOfTeethInput.insert(10, "0")
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
        diameter = float(diameterInput.get().replace(",", "."))
        diameter = float(diameter)
        cuttingdepth = float(cuttingDepthInput.get().replace(",", "."))
        cuttingdepth = float(cuttingdepth)
        rotation = float(rotationInput.get().replace(",", "."))
        rotation = float(rotation)
        choice = milltype.get()
        length = float(workpieceLengthInput.get().replace(",", "."))
        length = float(length)
        width = float(widthInput.get().replace(",", "."))
        width = float(width)
        groovedepth = float(grooveDepthInput.get().replace(",", "."))
        groovedepth = float(groovedepth)
        cuts = float(numberOfCutsInput.get().replace(",", "."))
        cuts = float(cuts)
        speedperteeth = float(feedRateInput.get().replace(",", "."))
        speedperteeth = float(speedperteeth)
        numberofteeth = float(numberOfTeethInput.get().replace(",", "."))
        numberofteeth = float(numberofteeth)

        speedperrotation = speedperteeth * numberofteeth

        startup = overrun = float(startupOverrunInput.get().replace(",", "."))
        startup = float(startup)
    except ValueError:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie ausschließlich Zahlen ein!")
        reset()

    if numberofteeth == 0:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie die Anzahl der Zähne ein!")
        numberOfTeethInput.delete(0, END)
        numberOfTeethInput.focus_set()
    elif rotation == 0:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie eine Drehzahl ein!")
        rotationInput.delete(0, END)
        rotationInput.focus_set()
    elif speedperrotation == 0:
        tkinter.messagebox.showinfo("Info", "Bitte geben Sie einen Wert für den Vorschub ein!")
        feedRateInput.delete(0, END)
        feedRateInput.focus_set()

    if choice == 1:
        firstcut = math.sqrt(diameter * cuttingdepth - cuttingdepth ** 2)
        millway = length + startup + overrun + firstcut
    elif choice == 2:
        firstcut = math.sqrt(diameter * cuttingdepth - cuttingdepth ** 2)
        if method == 1:
            millway = length + startup + overrun + firstcut
        else:
            millway = length + startup + overrun + 2 * firstcut
    elif choice == 3:
        if method == 1:
            firstcut = 1/2 * math.sqrt(diameter ** 2 - width ** 2)
            millway = length + (diameter / 2) - firstcut + startup + overrun
        else:
            millway = length + diameter + startup + overrun
    else:
        cuts = (groovedepth + startup) / cuttingdepth
        if method == 3:
            millway = length - (diameter / 2) + overrun
        else:
            millway = length - diameter

    mainusagetime = (millway * cuts)/(rotation * speedperrotation)
    mainUsageTimeOutput.delete(0, END)
    mainUsageTimeOutput.insert(10, mainusagetime.__round__(2))


# Eingabefenster erstellen----------------------------------------------------------------------------------------------
millMenue = Tk()
# Fenstername festlegen
millMenue.title("Fräsen")
# Label, Eingabefelder und Buttons erstellen und positionieren----------------------------------------------------------
# Außendurchmesser in mm------------------------------------------------------------------------------------------------
diameterLabel = Label(millMenue, text='Fräserdurchmesser [mm]').grid(row=0, column=0, padx=10, sticky='w')
diameterInput = tkinter.Entry(millMenue, width=10)
diameterInput.grid(row=0, column=1)
# diameterInput.insert(10, "0")
diameterInput.focus_set()
# Spanungstiefe in mm------------------------------------------------------------------------------------------------
cuttingDepthLabel = Label(millMenue, text='Spanungstiefe [mm]').grid(row=1, column=0, padx=10, sticky='w')
cuttingDepthInput = tkinter.Entry(millMenue, width=10)
cuttingDepthInput.grid(row=1, column=1)
cuttingDepthInput.insert(10, "0")
# Zähnezahl des Fräsers------------------------------------------------------------------------------------------------
numberOfTeethLabel = Label(millMenue, text='Zähnezahl des Fräsers').grid(row=2, column=0, padx=10, sticky='w')
numberOfTeethInput = tkinter.Entry(millMenue, width=10)
numberOfTeethInput.grid(row=2, column=1, pady=5)
numberOfTeethInput.insert(10, "0")
# Drehzahl--------------------------------------------------------------------------------------------------------------
rotationLabel = Label(millMenue, text='Drehzahl [1/min]', anchor='w').grid(row=3, column=0, padx=10, sticky='w')
rotationInput = tkinter.Entry(millMenue, width=10)
rotationInput.grid(row=3, column=1, pady=5)
rotationInput.insert(10, "0")
# Anlauf / Überlauf-----------------------------------------------------------------------------------------------------
startupOverrunLabel = Label(millMenue, text='Anlauf / Überlauf [mm]').grid(row=4, column=0, padx=10, sticky='w')
startupOverrunInput = tkinter.Entry(millMenue, width=10)
startupOverrunInput.grid(row=4, column=1, pady=5)
startupOverrunInput.insert(10, "0")
# Werkstücklänge--------------------------------------------------------------------------------------------------------
workpieceLengthLabel = Label(millMenue, text='Werkstücklänge [mm]').grid(row=0, column=3, padx=20, sticky='w')
workpieceLengthInput = Entry(millMenue, width=10)
workpieceLengthInput.grid(row=0, column=4, padx=10, pady=5)
workpieceLengthInput.insert(10, "0")
# Anzahl der Schnitte---------------------------------------------------------------------------------------------------
numberOfCutsLabel = Label(millMenue, text='Anzahl der Schnitte').grid(row=1, column=3, padx=20, sticky='w')
numberOfCutsInput = Entry(millMenue, width=10)
numberOfCutsInput.grid(row=1, column=4, pady=5)
numberOfCutsInput.insert(10, "0")
# Vorschub je Fräserzahn------------------------------------------------------------------------------------------------
feedRateLabel = Label(millMenue, text='Vorschub je Fräserzahn [mm]').grid(row=2, column=3, padx=20, sticky='w')
feedRateInput = Entry(millMenue, width=10)
feedRateInput.grid(row=2, column=4, pady=5)
feedRateInput.insert(10, "0")
# Hauptnutzungszeit-----------------------------------------------------------------------------------------------------
mainUsageTimeLabel = Label(millMenue, text='Hauptnutzungszeit [min]').grid(row=4, column=3, padx=20, sticky='w')
mainUsageTimeOutput = Entry(millMenue, width=10)
mainUsageTimeOutput.grid(row=4, column=4, pady=5)
mainUsageTimeOutput.insert(10, "0")
# Auswahlschalter-------------------------------------------------------------------------------------------------------
selectionFrame = Frame(millMenue)
selectionFrame.grid(row=5, column=0, sticky='w')
milltype = IntVar()
milltype.set(1)
Radiobutton(selectionFrame, text="Umfangs-Planfräsen", variable=milltype, value=1, command=selection).grid(row=0, column=0, sticky='w')
Radiobutton(selectionFrame, text="Stirn-Umfangs-Planfräsen", variable=milltype, value=2, command=selection).grid(row=1, column=0, sticky='w')
Radiobutton(selectionFrame, text="Stirn-Planfräsen", variable=milltype, value=3, command=selection).grid(row=2, column=0, sticky='w')
Radiobutton(selectionFrame, text="Nutenfräsen", variable=milltype, value=4, command=selection).grid(row=3, column=0, sticky='w')
# Rahmen zum ein und ausblenden der Auswahlbuttons----------------------------------------------------------------------
roughingFinishingFrame = Frame(millMenue)
roughingFinishingFrame.grid(row=5, column=3, sticky='w')
slottedHolesFrame = Frame(millMenue)

method = IntVar()
method.set(1)
Radiobutton(roughingFinishingFrame, text="Schruppen", variable=method, value=1).grid(row=0, column=0, sticky='w', padx=20)
Radiobutton(roughingFinishingFrame, text="Schlichten", variable=method, value=2).grid(row=1, column=0, sticky='w', padx=20)
Radiobutton(slottedHolesFrame, text="Einseitig offene Nut", variable=method, value=3).grid(row=0, column=0, sticky='w', padx=20)
Radiobutton(slottedHolesFrame, text="Geschlossene Nut", variable=method, value=4).grid(row=1, column=0, sticky='w', padx=20)
# Rahmen und zusätzliches Eingabefelder---------------------------------------------------------------------------------
widthFrame = Frame(millMenue)
widthLabel = Label(widthFrame, text="Werkstückbreite [mm]").grid(row=0, column=0, sticky='w', padx=20)
widthInput = Entry(millMenue, width=10)
widthInput.insert(10, "0")

grooveDepthFrame = Frame(millMenue)
grooveDepthLabel = Label(grooveDepthFrame, text="Nuttiefe [mm]").grid(row=0, column=0, sticky='w', padx=20)
grooveDepthInput = Entry(millMenue, width=10)
grooveDepthInput.insert(10, "0")
# Schalter--------------------------------------------------------------------------------------------------------------
buttonFrame = Frame(millMenue)
buttonFrame.grid(row=9, columnspan=5)

calculateButton = Button(buttonFrame, text='Berechnen', width=10, command=calculate).grid(row=9, column=0, padx=5, pady=20)
resetButton = Button(buttonFrame, text='Zurücksetzen', width=10, command=reset).grid(row=9, column=1, padx=5, pady=20)
saveButton = Button(buttonFrame, text='Speichern', width=10, command=save).grid(row=9, column=2, padx=5, pady=20)
backButton = Button(buttonFrame, text='Zurück', width=10, command=back).grid(row=9, column=3, padx=5, pady=20)
exitButton = Button(buttonFrame, text='Beenden', width=10, command=ende).grid(row=9, column=4, padx=5, pady=20)

millMenue.update()
millMenue.mainloop()
