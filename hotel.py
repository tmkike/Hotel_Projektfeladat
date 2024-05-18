#----------------------------------------------------------------------ADATOK--------------------------------------------------------------------------------

# Név:        Tamási Miklós
# Neptkód:    O070E2
# Szak:       Mérnökinfo

#----------------------------------------------------------------------Konyvtarak----------------------------------------------------------------------------

from abc import ABC, abstractmethod
from tkinter import *
from tkinter import messagebox
import os

#----------------------------------------------------------------------Globalis valtozok---------------------------------------------------------------------

hatter = "#5CFCFF"
gombHatter = "teal"
udv = "Üdvözlünk a Szobafoglaló applikációnkban!"
kiiras ="Itt lehetőség van a szobátfoglalni, törölni, \nvalamint a foglalások átnézésére a különböző hotelek között.\n\n\nKérlék válasz az alábbi lehetőségek közül:"
szovegSzin = "black"
terkoz = 40
ablakMeret = "800x900"
FoglalasFileNeve = "Foglalas.txt"
SzallodaFileNeve = "Szalloda.txt"
global FoglalasAdatbazis
FoglalasAdatbazis = []
global SzallodaAdatbazis
SzallodaAdatbazis = []

#----------------------------------------------------------------------Osztalyok-----------------------------------------------------------------------------
#----Adatszerkezet

class Szoba(ABC):
    def __init__(self, ar):
        self.ar = ar
    
    @abstractmethod
    def GetSzobaAr(self):       pass

class EgyagyasSzoba(Szoba):
    def GetSzobaAr(self):       return self.ar

class KetagyasSzoba(Szoba):
    def GetSzobaAr(self):       return self.ar

class Szalloda:
    def __init__(self, nev, egyAr, ketAgy):
        self.nev = nev
        egy = EgyagyasSzoba(egyAr)
        self.egyszobaar = egy.GetSzobaAr()
        ket = KetagyasSzoba(ketAgy)
        self.ketszoba = ket.GetSzobaAr()
     
    def GetSzallodaNev(self):       return self.nev 
    def GetSzallodaEgyAgyAr(self):  return self.egyszobaar
    def GetSzallodaKetAgyAr(self):  return self.ketszoba
    def GetSzallodaEgyben(self):    return f"{self.nev}; {self.egyszobaar}; {self.ketszoba}"

    # Újra kellet definiálni
    def __repr__(self):
        return f"{self.nev}, {self.egyszobaar}, {self.ketszoba}"

class Foglalas:
    def __init__(self, nev, szalloda, agyak, szoba, checkIn, checkOut):
        self.nev = nev
        self.szalloda = szalloda
        self.agyak = agyak
        self.szoba = szoba
        self.checkIn = checkIn
        self.checkOut = checkOut

    def GetFoglalasNev(self):       return self.nev
    def GetFoglalasEgyben(self):    return (self.nev + "; " + self.szalloda + "; " + self.agyak + "; " + self.szoba + "; " + self.checkIn + "; " + self.checkOut)

    def __form__(self):
        return 0

    # Újra kellet definiálni
    def __repr__(self):
        return f"{self.nev}, {self.szalloda}, {self.agyak}, {self.szoba}, {self.checkIn}, {self.checkOut}"
    
#----Különböző műveletek
class Muveletek:
    def Beolvasas():
        beolvasVagva = []

        if os.path.exists(FoglalasFileNeve):   
            try:
                file = open(FoglalasFileNeve, "r", encoding="latin-1")
                
                for sor in file:
                    beolvasVagva.clear()
                    beolvasVagva = sor.split(";")
                    FoglalasAdatbazis.append(Foglalas(*beolvasVagva))
                file.close()

            except Exception as e:
                messagebox.showinfo(title="Foglalási adatbázis hiba!", message="A Foglalások betöltése során hiba lépett fel!\n" + str(e))

        else:   messagebox.showinfo("Foglalások","A foglalások törlődtek, ezért újra kell rögzíteni őket!")
            
        if os.path.exists(SzallodaFileNeve):   
            try:
                file = open(SzallodaFileNeve, "r", encoding="latin-1")
            
                for sor in file:
                    beolvasVagva.clear()
                    beolvasVagva = sor.split(";")
                    SzallodaAdatbazis.append(Szalloda(*beolvasVagva))

                file.close()

            except Exception as e:
                messagebox.showinfo(title="Foglalási adatbázis hiba!", message="A Foglalások betöltése során hiba lépett fel!\n" + str(e))

        else:   messagebox.showinfo("Szállások","A szállodák törlődtek, ezért újra kell rögzíteni őket!")
            
    def Kiiratas():
        if os.path.exists(FoglalasFileNeve):
             try:
                 file = open(FoglalasFileNeve, "w")
                 file.write("")
                 file.close()

             except Exception as e:
                 messagebox.showinfo("Másolás hiba!", "Probléma merült fel az adatbázis kiirása során!\n" + str(e))
        else:
             with open(FoglalasFileNeve, "w"):     pass
             messagebox.showinfo("Foglalás adatbázis", "A foglalási adatbázis sérült vagy megsemmisült!\nAz adatbázis újra lett létrehozva, ezért\na korábbi adatok elveszhettek!")

        if os.path.exists(SzallodaFileNeve):
             try:
                 file = open(SzallodaFileNeve, "w")
                 file.write("")
                 file.close()
                 
             except Exception as e:
                 messagebox.showinfo("Másolás hiba!", "Probléma merült fel az adatbázis kiirása során!\n" + str(e))
        else:
             with open(SzallodaFileNeve, "w"):     pass
             messagebox.showinfo("Szálloda adatbázis", "A szállodai adatbázis sérült vagy megsemmisült!\nAz adatbázis újra lett létrehozva, ezért\na korábbi adatok elveszhettek!")
        
        try:
            with open(FoglalasFileNeve, 'a') as hozzaad:
                for elem in FoglalasAdatbazis:
                     sor = elem
                     hozzaad.write(str(sor.GetFoglalasEgyben()) + "\n")
                 
        except Exception as e:
            messagebox.showinfo("Hiba", "Hiba a fájl kiírása közben!\n" + str(e))
        try:
            with open(SzallodaFileNeve, 'a') as hozzaad:
                for elem in SzallodaAdatbazis:
                     sor = elem
                     hozzaad.write(str(sor.GetSzallodaEgyben()) + "\n")
               
        except Exception as e:
            messagebox.showinfo("Hiba", "Hiba a fájl kiírása közben!\n" + str(e))
    
class AblakSzulo(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.geometry(ablakMeret)
        self.config(background=hatter)
        self.transient(master)
        self.grab_set()
        self.resizable(width=False, height=False)

    # Újra kellet definiálni
    def destroy(self):
        super().destroy()
        self.master.grab_release()

class GombEvent():
    def Foglalas():
        global fogablak, felhasznaloEntri, szallodamegjelen, agyak, checkIn, checkOut, szobaSzamEntry
        fogablak = AblakSzulo()
        
        fogudv = "Szoba foglalás"
        szovegSzin="black"
        cimke = Label(fogablak,
                       text=fogudv, 
                       background=hatter, 
                       font=('Arial', 25, 'bold'), 
                       fg=szovegSzin,
                       pady=10 
                       )
        
        felhasznaloNeve = Label(fogablak,
                       text="Foglaló neve: ", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )
        
        szallodaKivalasztas = Label(fogablak,
                       text="Szálloda kiválasztása: ", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )

        agyKivalasztasa = Label(fogablak,
                       text="Hány ágyas szobát szeretne: ", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )
        
        erkezesiIdo = Label(fogablak,
                       text="Érkezés időpontja(ÉÉÉÉ-HH-NN):", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10 )

        tavozasiIdo = Label(fogablak,
                       text="Távozás időpontja(ÉÉÉÉ-HH-NN):", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10
                       )

        felhasznaloEntri = Entry(fogablak, width=30)

        elemek = []
        elemek.append("Szállodák listája:")

        for szallo in SzallodaAdatbazis:
            sz = szallo
            elemek.append(sz.GetSzallodaNev())
            
        szallodamegjelen = Listbox(fogablak, selectmode=SINGLE)

        for elem in elemek:
             szallodamegjelen.insert(END, elem)

        szallodamegjelen.selection_set(0)

        agyak = StringVar(value="Egy ágyas szoba")
        egy = Radiobutton(fogablak, text="Egy ágyas szoba", variable=agyak, value="Egy ágyas szoba", background=hatter)
        ketto = Radiobutton(fogablak, text="Két ágyas szoba", variable=agyak, value="Két ágyas szoba", background=hatter)

        checkIn = Entry(fogablak, width=20)
        checkOut = Entry(fogablak, width=20)

        checkIn.insert(0, "ÉÉÉÉ-HH-NN")
        checkOut.insert(0, "ÉÉÉÉ-HH-NN")

        szobaSzamLabel = Label(fogablak,
                       text="Foglalni kívánt szoba száma:", 
                       background=hatter, 
                       font=('Arial', 15, 'bold'), 
                       fg=szovegSzin,
                       pady=10)
        szobaSzamEntry = Entry(fogablak)

        ujszalloda = Button(fogablak,
                      text="Új szálloda felvétele",
                      command=GombEvent.UjSzalloda,
                      font=("Consolas", 10, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        cimke.pack()
        felhasznaloNeve.pack()
        felhasznaloEntri.pack()
        szallodaKivalasztas.pack()
        szallodamegjelen.pack()
        ujszalloda.pack()
        agyKivalasztasa.pack()
        egy.pack()
        ketto.pack()
        szobaSzamLabel.pack()
        szobaSzamEntry.pack()
        erkezesiIdo.pack()
        checkIn.pack()
        tavozasiIdo.pack()
        checkOut.pack()

        foglalasMentese = Button(fogablak,
                      text="Foglalás mentése",
                      command=GombEvent.FoglalasAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )
        
        torles = Button(fogablak,
                      text="Adatok törlése",
                      command=GombEvent.TorlesAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        vissza = Button(fogablak ,
                      text="Vissza a főmenübe",
                      command=fogablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        foglalasMentese.pack(side=LEFT)
        torles.pack(side=LEFT)
        vissza.pack(side=LEFT)

        checkIn.bind("<Button-1>", checkIn.delete(0, END))
        checkOut.bind("<Button-1>", checkOut.delete(0, END))

    def Lemondas():
        global lemondablak, foglalasiNevEntri, lemondoLista, lemondasi
        lemondasi = ["Kérlek adja meg a foglalási nevet!", "", ""]
        lemondablak = AblakSzulo()
        
        udvozloAblakon = Label(lemondablak, 
                       text="Szoba foglalásának lemondása", 
                       background=hatter, 
                       font=('Arial', 25, 'bold'),
                       pady=10
                       )
        nevMegAdasa = Label(lemondablak, 
                      text="Foglalási név:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )

        foglalasiNevEntri = Entry(lemondablak, width=50)

        foglalasiNevButton = Button(lemondablak,
                      text="Keresés",
                      command= GombEvent.LemondasAlEsemeny,
                      font=("Consolas", 10, "bold"),
                      fg= szovegSzin,
                      bg= gombHatter,
                      activeforeground= szovegSzin,
                      activebackground= "blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )
        
        
        lemondoLista = Listbox(lemondablak, selectmode=SINGLE, width=120, height=40)

        for lemond in lemondasi:
             lemondoLista.insert(END, lemond)
        
        keresGomb = Button(
                      lemondablak,
                      text="Lemondás",
                      command=GombEvent.LemondasTorlesGomb,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        torles = Button(lemondablak,
                        text="Keresés törlése",
                        command=GombEvent.LemondasTorles,
                        font=("Consolas", 15, "bold"),
                        fg=szovegSzin,
                        bg=gombHatter,
                        activeforeground=szovegSzin,
                        activebackground="blue",
                        justify=CENTER,
                        width=22,
                        bd=5,
                        padx=5
                        )

        visszaGomb = Button(lemondablak,
                      text="Vissza a főmenübe",
                      command=lemondablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        udvozloAblakon.pack()
        nevMegAdasa.pack()
        foglalasiNevEntri.pack()
        foglalasiNevButton.pack()
        lemondoLista.pack()

        keresGomb.pack(side=LEFT)
        torles.pack(side=LEFT)
        visszaGomb.pack(side=LEFT)

    def LemondasAlEsemeny():
        listaMutato = 0
        global nevMutato
        nevMutato = 0
        lemondasi = []
        lemondasi.append(foglalasiNevEntri.get() + " név alatt foglalt szobák listája:")
        lemondoLista.delete(0, END)

        for foglal in FoglalasAdatbazis:
                             
            if foglalasiNevEntri.get() == foglal.GetFoglalasNev():
                lemondasi.append(str(listaMutato) + "; " + foglal.GetFoglalasEgyben())
                nevMutato += 1

            listaMutato += 1

        for lemond in lemondasi:
            lemondoLista.insert(END, lemond)

    def LemondasTorlesGomb():
        try:
            selected_index = lemondoLista.curselection()[0]

            if lemondoLista.curselection()[0] == 0:
                messagebox.showinfo("Lemondás", "Nem választottál ki foglalást!")
                return

            actual_index = selected_index - 1

            if actual_index < nevMutato:
                toroltAdat = FoglalasAdatbazis[actual_index]
                del FoglalasAdatbazis[actual_index]
                messagebox.showinfo("Törlés", "Az alábbi foglalást sikeresen töröltük!\n" + str(toroltAdat.GetFoglalasEgyben()))
                GombEvent.LemondasAlEsemeny()
            else:
                messagebox.showinfo("Lemondás", "Érvénytelen kiválasztás!")

        except IndexError:
            messagebox.showinfo("Lemondás", "Nem választottál ki foglalást!")
        except Exception as e:
            messagebox.showinfo("Törlés", "A kért foglalás nem törölhető!\n" + str(e))

        GombEvent.LemondasAlEsemeny()

    def Listazas():
        global listazasablak
        listazasablak = AblakSzulo()

        udvozlo_frame = Frame(listazasablak)

        udvozloAblakon = Label(udvozlo_frame, 
                       text="Szállodák és foglalások listája:", 
                       background=hatter, 
                       font=('Arial', 25, 'bold')
                       )
        
        gomb_frame = Frame(listazasablak)

        visszaGomb = Button(gomb_frame,
                      text="Vissza a főmenübe",
                      command=listazasablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )  

        canvas = Canvas(listazasablak, width=760, height=2, bg="black", highlightthickness=0)

        foglalas_frame = Frame(listazasablak, bg=hatter)
        szalloda_frame = Frame(listazasablak, bg=hatter)

        cim10_label = LabelFrame(foglalas_frame, text="Foglalások listája:", width=15, bg=hatter)

        cim1_label = Label(foglalas_frame, text="Név:", width=15, bg=hatter)
        cim2_label = Label(foglalas_frame, text="Szálloda:", width=15, bg=hatter)
        cim3_label = Label(foglalas_frame, text="Ágyak típusa", width=15, bg=hatter)
        cim4_label = Label(foglalas_frame, text="Szobaszám:", width=15, bg=hatter)
        cim5_label = Label(foglalas_frame, text="checkIn", width=15, bg=hatter)
        cim6_label = Label(foglalas_frame, text="checkOut", width=15, bg=hatter)

        entri1 = Listbox(foglalas_frame, width=15, justify=CENTER)
        entri2 = Listbox(foglalas_frame, width=15, justify=CENTER)
        entri3 = Listbox(foglalas_frame, width=15, justify=CENTER)
        entri4 = Listbox(foglalas_frame, width=15, justify=CENTER)
        entri5 = Listbox(foglalas_frame, width=15, justify=CENTER)
        entri6 = Listbox(foglalas_frame, width=15, justify=CENTER)

        cim7_label = LabelFrame(szalloda_frame, text="Szálloda neve:", width=20, bg=hatter)
        cim8_label = LabelFrame(szalloda_frame, text="Egyágyas ár(Ft):", width=20, bg=hatter)
        cim9_label = LabelFrame(szalloda_frame, text="Kétágyas ár(Ft):", width=20, bg=hatter)

        entri7 = Listbox(szalloda_frame, width=15, justify=CENTER)
        entri8 = Listbox(szalloda_frame, width=15, justify=CENTER)
        entri9 = Listbox(szalloda_frame, width=15, justify=CENTER)

        udvozloAblakon.grid(row=0, column=0)

        cim10_label.grid(row=0, column=0)

        cim1_label.grid(row=1, column=0, padx=10)
        cim2_label.grid(row=1, column=1, padx=10)
        cim3_label.grid(row=1, column=2, padx=10)
        cim4_label.grid(row=1, column=3, padx=10)
        cim5_label.grid(row=1, column=4, padx=10)
        cim6_label.grid(row=1, column=5, padx=10)

        entri1.grid(row=2, column=0, padx=20)
        entri2.grid(row=2, column=1, padx=20)
        entri3.grid(row=2, column=2, padx=20)
        entri4.grid(row=2, column=3, padx=20)
        entri5.grid(row=2, column=4, padx=20)
        entri6.grid(row=2, column=5, padx=20)

        cim7_label.grid(row=0, column=1, padx=10)
        cim8_label.grid(row=0, column=2, padx=10)
        cim9_label.grid(row=0, column=3, padx=10)

        entri7.grid(row=0, column=0, padx=20)
        entri8.grid(row=0, column=1, padx=20)
        entri9.grid(row=0, column=2, padx=20)

        visszaGomb.grid(row=0, column=0)

        for elem in FoglalasAdatbazis:
            sor = elem.GetFoglalasEgyben()
            tomb = sor.split(";")
            entri1.insert(END, tomb[0])
            entri2.insert(END, tomb[1])
            entri3.insert(END, tomb[2])
            entri4.insert(END, tomb[3])
            entri5.insert(END, tomb[4])
            entri6.insert(END, tomb[5])
                    
        for elem in SzallodaAdatbazis:
            sor = elem.GetSzallodaEgyben()
            tomb = sor.split(";")
            entri7.insert(END, tomb[0])
            entri8.insert(END, tomb[1])
            entri9.insert(END, tomb[2])


        udvozlo_frame.pack()
        foglalas_frame.pack()
        canvas.pack(padx=10, pady=10)
        szalloda_frame.pack()
        gomb_frame.pack()

    def UjSzalloda():
        fogablak.destroy()

        global ujszallodaablak, szallodaNeveEntri, szallodaEgyArEntri, szallodaKetArEntri
        ujszallodaablak = AblakSzulo()

        udvozloAblakon = Label(ujszallodaablak, 
                       text="Új szálloda hozzáadása", 
                       background=hatter, 
                       font=('Arial', 25, 'bold'),
                       pady=10
                       )
        
        szallodaNeveLabel = Label(ujszallodaablak, 
                      text="Szálloda neve:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )
        
        szallodaNeveEntri = Entry(ujszallodaablak, width=30)

        szallodaEgyArLabel = Label(ujszallodaablak, 
                      text="Egy ágyas szoba ára:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )
        
        szallodaEgyArEntri = Entry(ujszallodaablak, width=30)

        szallodaKetArLabel = Label(ujszallodaablak, 
                      text="Két ágyas szoba ára:", 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=10
                      )
        
        szallodaKetArEntri = Entry(ujszallodaablak, width=30)

        foglalasMentese = Button(ujszallodaablak,
                      text="Szálloda mentése",
                      command=GombEvent.UjSzalloAlEsemeny,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )
        
        torles = Button(ujszallodaablak,
                      text="Adatok törlése",
                      command=GombEvent.SzallodaTorles,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        vissza = Button(ujszallodaablak,
                      text="Vissza a főmenübe",
                      command=ujszallodaablak.destroy,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

        udvozloAblakon.pack()
        szallodaNeveLabel.pack()
        szallodaNeveEntri.pack()
        szallodaEgyArLabel.pack()
        szallodaEgyArEntri.pack()
        szallodaKetArLabel.pack()
        szallodaKetArEntri.pack()

        foglalasMentese.pack(side=LEFT)
        torles.pack(side=LEFT)
        vissza.pack(side=LEFT)

    def UjSzalloAlEsemeny():
        ujSzallodaAdatok = []
        hianyos = True

        ujSzallodaAdatok.append(szallodaNeveEntri.get())
        ujSzallodaAdatok.append(szallodaEgyArEntri.get())
        ujSzallodaAdatok.append(szallodaKetArEntri.get())

        for adat in ujSzallodaAdatok:
            if not adat:
                hianyos = False
                break
        
        if hianyos:
            try:
                sz = Szalloda(*ujSzallodaAdatok)
                SzallodaAdatbazis.append(sz)
                Muveletek.Kiiratas()
                messagebox.showinfo("Új szálloda", "Az új szálloda adatait sikeresen rögzítettük!")
                fogablak.destroy()
            except Exception as e:
                messagebox.showerror("Hiba", "Hiba történt a az új szálloda rögzítése közben:\n" + str(e))
        
        else:
            messagebox.showinfo("Hiányos mező", "Hiányosan töltötted ki a beviteli mezőket!\nKérlek ellenőrizd őket!")

        ujszallodaablak.destroy()

    def FoglalasAlEsemeny():
        foglalasiAdatok = []

        foglalasiAdatok.append(felhasznaloEntri.get())
        index = szallodamegjelen.curselection()[0]
        foglalasiAdatok.append(szallodamegjelen.get(index))
        foglalasiAdatok.append(agyak.get())
        foglalasiAdatok.append(szobaSzamEntry.get())
        foglalasiAdatok.append(checkIn.get())
        foglalasiAdatok.append(checkOut.get())
        hianyos = True

        if index == 0:  hianyos = False

        for adat in foglalasiAdatok:
            if not adat:
                hianyos = False
                break
        
        if hianyos:
            try:
                FoglalasAdatbazis.append(Foglalas(*foglalasiAdatok))
                Muveletek.Kiiratas()
                messagebox.showinfo("Foglalás", "A Foglalást sikeresen rögzítettük!")
                fogablak.destroy()
            except Exception as e:
                messagebox.showerror("Hiba", "Hiba történt a foglalás közben:\n" + str(e))
        
        else:
            messagebox.showinfo("Hiányos mező", "Hiányosan vagy hibásan töltötted ki a beviteli mezőket!\nKérlek ellenőrizd őket!")
        
    def TorlesAlEsemeny():
        checkIn.insert(0, "ÉÉÉÉ-HH-NN")
        checkOut.insert(0, "ÉÉÉÉ-HH-NN")
        szallodamegjelen.selection_set(0)
        felhasznaloEntri.delete(0, END)
        checkIn.bind("<Button-1>", checkIn.delete(0, END))
        checkOut.bind("<Button-1>", checkOut.delete(0, END))

    def SzallodaTorles():
        szallodaNeveEntri.delete(0, END)
        szallodaEgyArEntri.delete(0, END)
        szallodaKetArEntri.delete(0, END)

    def LemondasTorles():
        foglalasiNevEntri.delete(0, END)
        lemondoLista.delete(0, END)
        lemondasi = ["Kérlek adja meg a foglalási nevet!", "", ""]
        lemondoLista = Listbox(lemondablak, selectmode=SINGLE, width=120, height=40)

        for lemond in lemondasi:
             lemondoLista.insert(END, lemond)

#----------------------------------------------------------------------MAIN----------------------------------------------------------------------------------

def Main():
    kezdoAblak = Tk()

    kezdoAblak.geometry(ablakMeret)
    kezdoAblak.title("Hotel Foglalás")
    kezdoAblak.config(background=hatter)
    kezdoAblak.resizable(width=False, height=False)
    Muveletek.Beolvasas()

    ikon = PhotoImage(file="icon.png")
    kezdoAblak.iconphoto(True, ikon)

    listazasGomb = Button(
        kezdoAblak,
        text="Foglalások litázása",
        command=GombEvent.Listazas,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

    lemondasGomb = Button(kezdoAblak,
                      text="Szoba lemondás",
                      command=GombEvent.Lemondas,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

    foglalasGomb = Button(kezdoAblak,
                      text="Szoba foglalás",
                      command=GombEvent.Foglalas,
                      font=("Consolas", 15, "bold"),
                      fg=szovegSzin,
                      bg=gombHatter,
                      activeforeground=szovegSzin,
                      activebackground="blue",
                      justify=CENTER,
                      width=22,
                      bd=5,
                      padx=5
                      )

    udvozloAblakon = Label(kezdoAblak, 
                       text=udv, 
                       background=hatter, 
                       font=('Arial', 25, 'bold'), 
                       fg=szovegSzin,
                       pady=10
                       )

    szovegAblakon = Label(kezdoAblak, 
                      text=kiiras, 
                      background=hatter,
                      font=('Arial', 15), 
                      pady=300
                      )

    udvozloAblakon.pack()
    szovegAblakon.pack()

    foglalasGomb.pack(side=LEFT)
    lemondasGomb.pack(side=LEFT)
    listazasGomb.pack(side=LEFT)

    kezdoAblak.mainloop()

#----------------------------------------------------------------------START---------------------------------------------------------------------------------

Main()
