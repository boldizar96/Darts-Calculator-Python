#importok
import sys
from jatekos import Jatekos
import os
clear = lambda: os.system('cls')
import time

uj = True
while(uj):
    #játéktípus kiválasztása
    jatekTipusB = True
    jatekTipus = True #501 true, 301 false
    while(jatekTipusB):
        jatekTipusS = input("501-es vagy 301-es játékot szeretnél játszani?\n(Írd be, hogy:\"501\" vagy \"301\", kilépés \"q\")\n")
        jatekTipusS = jatekTipusS.strip()
        if(jatekTipusS == "501"):
            print("A kiválasztott játéktípus: 501")
            jatekTipus = True
            jatekTipusB = False
        elif(jatekTipusS == "301"):
            print("A kiválasztott játéktípus: 301")
            jatekTipus = False
            jatekTipusB = False
        elif(jatekTipusS == "q"):
            print("A program most kilép.")
            exit()
        else:
            print("Nincs ilyen típusú játék.")
            jatekTipusB = True
    clear()

    #játékosok számának megadása
    jatekosokSzamaB = True
    jatekosokSzama = 0
    while(jatekosokSzamaB):
        jatekosokSzamaS = input("Add meg, hogy hányan szeretnétek játszani!\n(1-6 játékos)\nkilépés \"q\"\n")
        jatekosokSzamaS = jatekosokSzamaS.strip()
        if(jatekosokSzamaS == "Q" or jatekosokSzamaS == "q"):
            print("A program most kilép.")
            exit()
        try:
            jatekosokSzama = int(jatekosokSzamaS)
        except:
            print("Számot adj meg 1-től 6-ig!")
        if(jatekosokSzama>6 or jatekosokSzama < 1):
            print("1-től 6-ig adj meg számot!")
            jatekosokSzamaB = True
        else:
            print("Játékosok száma: " + str(jatekosokSzama) + "\n")
            jatekosokSzamaB = False
    clear()

    #kiszálló típusa
    kiszalloB = True
    kiszallo = True #szimpla(bármilyen nyíllal ki lehet szállni) = True, dupla (csak dupla kiszálló) = False
    while(kiszalloB):
        kiszalloS = input("Add meg, hogy szimpla vagy dupla kiszállós játékot szeretnél-e játszani!\n\"S\": szimpla, \"D\": dupla\nkilépés: \"q\"\n")
        kiszalloS = kiszalloS.strip()
        kiszalloS = kiszalloS.upper()
        if(kiszalloS == "S"):
            print("Szimpla kiszállós játékot választottál!")
            kiszallo = True
            kiszalloB = False
        elif(kiszalloS == "D"):
            print("Dupla kiszállós játékot választottál!")
            kiszallo = False
            kiszalloB = False
        elif(kiszalloS == "Q"):
            print("A program most kilép.")
            exit()
        else:
            print("Hibás bemenet. Próbáld újra!")
            kiszalloB = True
    clear()

    #játékosok generálása
    print("Játékosok beállítása.")
    nevMegad = False
    nevMegadB = True
    while(nevMegadB):
        nevMegadS = input("Szeretnél a játékosoknak nevet adni, vagy sorszám elég?\n1 - név megadás\n2 - elég a sorszám(alapértelmezett\nenter - alapértelmezett\n\"q\" - kilépés\n")
        nevMegadS = nevMegadS.strip()
        nevMegadS = nevMegadS.upper()
        if(nevMegadS == "" or nevMegadS == "2"):
            nevMegad = False
            nevMegadB = False
        elif(nevMegadS == "1"):
            nevMegad = True
            nevMegadB = False
        elif(nevMegad == "Q"):
            print("A program most kilép.")
            exit()
        else:
            print("Hibás bemenet! Próbáld újra!")
            nevMegadB = True
    clear()

    jatekosok = []
    if(nevMegad):
        for i in range(jatekosokSzama):
            if(jatekTipus == True):
                nev = input("Add meg az " + str(i+1) + ". játékos nevét:")
                jatekosok.append(Jatekos(nev,501))
            if(jatekTipus == False):
                nev = input("Add meg az " + str(i+1) + ". játékos nevét:")
                jatekosok.append(Jatekos(nev,301))
    else:
        for i in range(jatekosokSzama):
            if(jatekTipus == True):
                jatekosok.append(Jatekos(str(i+1) + ".játékos",501))
            if(jatekTipus == False):
                jatekosok.append(Jatekos(str(i+1) + ".játékos",301))
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
        if(jatekTipus):
            if(kiszallo):
                print("501 - szimpla")
                print("------------------------------")
            else:
                print("501 - dupla")
                print("------------------------------")
        else:
            if(kiszallo):
                print("301 - szimpla")
                print("------------------------------")
            else:
                print("301 - dupla")
                print("------------------------------")

    if(kiszallo):
        #szimpla játék
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
                                    raise ValueError()
                                dobas1 = 3 * dobas1
                                dobasok = dobasok + dobas1
                                dobas2 = jatekosok[i].dob(dobas1)
                                if(dobas2 == "hiba"):
                                    raise AttributeError()
                                elif(dobas2 == "vege"):
                                    raise Exception()
                                db = db + 1
                                print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                            except ValueError:
                                print("Hibás bemenet!")
                                sugo()
                                ok = True
                            except AttributeError:
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
                                    raise ValueError()
                                dobas1 = 2 * dobas1
                                dobasok = dobasok + dobas1
                                dobas2 = jatekosok[i].dob(dobas1)
                                if(dobas2 == "hiba"):
                                    raise AttributeError()
                                elif(dobas2 == "vege"):
                                    raise Exception()
                                db = db + 1
                                print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                            except ValueError:
                                print("Hibás bemenet!")
                                sugo()
                                ok = True
                            except AttributeError:
                                print("Túl sokat dobtál...")
                                ok = False
                                jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1
                            except:
                                ok = False
                        elif(dobas1s.isdigit()):
                            try:
                                dobas1 = int(dobas1s)
                                if(dobas1 > 20 and (dobas1 != 25 and dobas1 != 50)):
                                    raise ValueError()
                                dobas1 = dobas1
                                dobasok = dobasok + dobas1
                                dobas2 = jatekosok[i].dob(dobas1)
                                if(dobas2 == "hiba"):
                                    raise AttributeError()
                                elif(dobas2 == "vege"):
                                    raise Exception()
                                db = db + 1
                                print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                            except ValueError:
                                print("Hibás bemenet!")
                                sugo()
                                ok = True
                            except AttributeError:
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
    else:
        #dupla játék
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
                jatekosok[i].kiszallo()
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
                                    raise ValueError()
                                dobas1 = 3 * dobas1
                                dobasok = dobasok + dobas1
                                dobas2 = jatekosok[i].dobD1(dobas1)
                                if(dobas2 == "hiba"):
                                    raise AttributeError()
                                elif(dobas2 == "vege"):
                                    raise Exception()
                                db = db + 1
                                print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                            except ValueError:
                                print("Hibás bemenet!")
                                sugo()
                                ok = True
                            except AttributeError:
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
                                    raise ValueError()
                                dobas1 = 2 * dobas1
                                dobasok = dobasok + dobas1
                                dobas2 = jatekosok[i].dobD2(dobas1)
                                if(dobas2 == "hiba"):
                                    raise AttributeError()
                                elif(dobas2 == "vege"):
                                    raise Exception()
                                db = db + 1
                                print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                            except ValueError:
                                print("Hibás bemenet!")
                                sugo()
                                ok = True
                            except AttributeError:
                                print("Túl sokat dobtál...")
                                ok = False
                                jatekosok[i].pontok = jatekosok[i].pontok + dobasok - dobas1
                            except:
                                ok = False
                        elif(dobas1s.isdigit()):
                            try:
                                dobas1 = int(dobas1s)
                                if(dobas1 > 20 and (dobas1 != 25 and dobas1 != 50)):
                                    raise ValueError()
                                dobas1 = dobas1
                                dobasok = dobasok + dobas1
                                dobas2 = jatekosok[i].dobD1(dobas1)
                                if(dobas2 == "hiba"):
                                    raise AttributeError()
                                elif(dobas2 == "vege"):
                                    raise Exception()
                                db = db + 1
                                print(jatekosok[i].nev + " - " + str(jatekosok[i].pontok))
                            except ValueError:
                                print("Hibás bemenet!")
                                sugo()
                                ok = True
                            except AttributeError:
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