#importok
import sys
from jatekos import Jatekos
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')
import time
from hiba import TulSok
from hiba import HibasBemenet

uj = True
while(uj):
    #játéktípus kiválasztása
    jatekTipusWhile = True
    jatekTipus = 501 #501 vagy 301 
    while(jatekTipusWhile):
        jatekTipusInput = input("501-es vagy 301-es játékot szeretnél játszani?\n(Írd be, hogy:\"501\" vagy \"301\", kilépés \"q\")\n")
        jatekTipusInput = jatekTipusInput.strip()
        if(jatekTipusInput == "501"):
            print("A kiválasztott játéktípus: 501")
            jatekTipus = int(jatekTipusInput)
            jatekTipusWhile = False
        elif(jatekTipusInput == "301"):
            print("A kiválasztott játéktípus: 301")
            jatekTipus = int(jatekTipusInput)
            jatekTipusWhile = False
        elif(jatekTipusInput == "q"):
            print("A program most kilép.")
            exit()
        else:
            print("Nincs ilyen típusú játék.")
            jatekTipusWhile = True
    clear()

    #játékosok számának megadása
    jatekosokSzamaWhile = True
    jatekosokSzama = 0
    while(jatekosokSzamaWhile):
        jatekosokSzamaInput = input("Add meg, hogy hányan szeretnétek játszani!\n(1-6 játékos)\nkilépés \"q\"\n")
        jatekosokSzamaInput = jatekosokSzamaInput.strip()
        if(jatekosokSzamaInput == "Q" or jatekosokSzamaInput == "q"):
            print("A program most kilép.")
            exit()
        try:
            jatekosokSzama = int(jatekosokSzamaInput)
        except:
            print("Számot adj meg 1-től 6-ig!")
        if(jatekosokSzama>6 or jatekosokSzama < 1):
            print("1-től 6-ig adj meg számot!")
            jatekosokSzamaWhile = True
        else:
            print("Játékosok száma: {}\n".format(jatekosokSzama))
            jatekosokSzamaWhile = False
    clear()

    #kiszálló típusa
    kiszalloWhile = True
    kiszallo = "szimpla" #szimpla(bármilyen nyíllal ki lehet szállni), dupla (csak dupla kiszálló)
    while(kiszalloWhile):
        kiszalloInput = input("Add meg, hogy szimpla vagy dupla kiszállós játékot szeretnél-e játszani!\n\"S\": szimpla, \"D\": dupla\nkilépés: \"q\"\n")
        kiszalloInput = kiszalloInput.strip()
        kiszalloInput = kiszalloInput.upper()
        if(kiszalloInput == "S"):
            print("Szimpla kiszállós játékot választottál!")
            kiszallo = "szimpla"
            kiszalloWhile = False
        elif(kiszalloInput == "D"):
            print("Dupla kiszállós játékot választottál!")
            kiszallo = "dupla"
            kiszalloWhile = False
        elif(kiszalloInput == "Q"):
            print("A program most kilép.")
            exit()
        else:
            print("Hibás bemenet. Próbáld újra!")
            kiszalloWhile = True
    clear()

    #játékosok generálása
    print("Játékosok beállítása.")
    nevMegad = False
    nevMegadWhile = True
    while(nevMegadWhile):
        nevMegadInput = input("Szeretnél a játékosoknak nevet adni, vagy sorszám elég?\n1 - név megadás\n2 - elég a sorszám(alapértelmezett\nenter - alapértelmezett\n\"q\" - kilépés\n")
        nevMegadInput = nevMegadInput.strip()
        nevMegadInput = nevMegadInput.upper()
        if(nevMegadInput == "" or nevMegadInput == "2"):
            nevMegad = False
            nevMegadWhile = False
        elif(nevMegadInput == "1"):
            nevMegad = True
            nevMegadWhile = False
        elif(nevMegadInput == "Q"):
            print("A program most kilép.")
            exit()
        else:
            print("Hibás bemenet! Próbáld újra!")
            nevMegadWhile = True
    clear()

    jatekosok = []
    if(nevMegad):
        for i in range(jatekosokSzama):
            nev = input("Add meg a(z) {}. játékos nevét:".format(i+1))
            jatekosok.append(Jatekos(nev,jatekTipus))
    else:
        for i in range(jatekosokSzama):
            jatekosok.append(Jatekos("{}.játékos".format(i+1),jatekTipus))
    clear()

    #súgó
    def sugo():
        print("Pontok megadása:")
        print("T# - tripla")
        print("D# - dupla")
        print("# - szimpla")
        print("Megjegyzés: # = zóna értéke")
        print("BULL(kicsi) - 25")
        print("BULL(nagy) - 50")
        print("------------------------------")
        print("{} - {}".format(jatekTipus,kiszallo))
        print("------------------------------")

    nyert = True
    brekk = False
    while(nyert):
        clear()
        sugo()
        brekk = False
        for i in range(jatekosokSzama):
            print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
        print("------------------------------")
        for i in range(jatekosokSzama):
            ok = True
            db = 1
            dobas1 = 0
            dobas2 = ""
            dobasok = 0
            if(brekk):
                break
            print(jatekosok[i].nev + ":")
            if(kiszallo):
                jatekosok[i].kiszallo()
            else:
                jatekosok[i].kiszallo2()
            while(ok and db < 4):                
                dobas1s = input(str(db) + ". nyíl: ")
                dobas1s = dobas1s.strip()
                dobas1s = dobas1s.upper()
                if(len(dobas1s)>=1):
                    if(dobas1s[0] == "T"):
                        dobas1s = dobas1s[1:]
                        try:
                            dobas1 = int(dobas1s)
                            if(dobas1 > 20):
                                raise HibasBemenet()
                            dobas1 = 3 * dobas1
                            dobasok = dobasok + dobas1
                            dobas2 = ""
                            if(kiszallo == "dupla"):
                                dobas2 = jatekosok[i].dobD1(dobas1)
                            else:
                                dobas2 = jatekosok[i].dob(dobas1)
                            if(dobas2 == "hiba"):
                                raise TulSok()
                            elif(dobas2 == "vege"):
                                raise Exception()
                            db = db + 1
                            print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                        except HibasBemenet:
                            print("Hibás bemenet!")
                            sugo()
                            ok = True
                        except TulSok:
                            print("Túl sokat dobtál...")
                            ok = False
                            jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1
                        except:
                            ok = False
                    elif(dobas1s[0] == "D"):
                        dobas1s = dobas1s[1:]
                        try:
                            dobas1 = int(dobas1s)
                            if(dobas1 > 20):
                                raise HibasBemenet()
                            dobas1 = 2 * dobas1
                            dobasok = dobasok + dobas1
                            dobas2 = ""
                            if(kiszallo == "dupla"):
                                dobas2 = jatekosok[i].dobD2(dobas1)
                            else:
                                dobas2 = jatekosok[i].dob(dobas1)
                            if(dobas2 == "hiba"):
                                raise TulSok()
                            elif(dobas2 == "vege"):
                                raise Exception()
                            db = db + 1
                            print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                        except HibasBemenet:
                            print("Hibás bemenet!")
                            sugo()
                            ok = True
                        except TulSok:
                            print("Túl sokat dobtál...")
                            ok = False
                            jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1
                        except:
                            ok = False
                    elif(dobas1s.isdigit()):
                        try:
                            dobas1 = int(dobas1s)
                            if(dobas1 > 20 and (dobas1 != 25 and dobas1 != 50)):
                                raise HibasBemenet()
                            dobas1 = dobas1
                            dobasok = dobasok + dobas1
                            dobas2 = ""
                            if(kiszallo == "dupla"):
                                if(dobas1 == 50):
                                    dobas2 = jatekosok[i].dob(dobas1)
                                else:
                                    dobas2 = jatekosok[i].dobD1(dobas1)
                            else:
                                dobas2 = jatekosok[i].dob(dobas1)
                            if(dobas2 == "hiba"):
                                raise TulSok()
                            elif(dobas2 == "vege"):
                                raise Exception()
                            db = db + 1
                            print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                        except HibasBemenet:
                            print("Hibás bemenet!")
                            sugo()
                            ok = True
                        except TulSok:
                            print("Túl sokat dobtál...")
                            ok = False
                            jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1
                        except:
                            ok = False
                    else:
                        print("Hibás bemenet!")
                        sugo()
                        ok = True
                else:
                    print("Hibás bemenet!")
                    sugo()
                    ok = True
                if(db > 4):
                    ok = False
                if(jatekosok[i].nyert()):
                    print(str(jatekosok[i].nev) + " nyert.")
                    ujjatekB = True
                    while(ujjatekB):
                        ujjatek = input("Szeretnél új játékot kezdeni?\nI - Igen\nN - Nem\n")
                        ujjatek = ujjatek.strip()
                        ujjatek = ujjatek.upper()
                        #print(ujjatek)
                        if(ujjatek == "I"):
                            ujjatekB = False
                            nyert = False
                            ok = False
                            brekk = True
                            uj = True
                        elif(ujjatek == "N"):
                            ujjatekB = False
                            nyert = False
                            ok = False
                            brekk = True
                            uj = False
                        else:
                            print("Hibás bemenet. Próbáld újra!")
                            ujjatekB = True
            print("------------------------------------")
        time.sleep(2)

print("A program most kilép.")
exit()