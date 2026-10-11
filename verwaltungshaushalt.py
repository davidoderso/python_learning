einnahme = []
ausgabe = []

print("Mein Verwaltungshausbuch")
print("1. Einnahmen hinzufügen")
print("2. Ausgaben hinzufügen")
print("3. Buchungen anzeigen")
print("4. Kontostand anzeigen")
print("5. Programm beenden")

while True:
    aktion = input("Was wollen Sie machen? Bitte geben Sie eine Zahl von 1-5 an ")

    if aktion == "1":
        while True:
            try:
                betrag = float(input("Einnahme hinzufügen (€): "))
                if betrag > 0:
                    einnahme.append(betrag)
                    print("Ihre Einnahmen (€): ", einnahme)
                    break
                else:
                    print("Betrag muss eine positive Zahl sein")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl ein")
    elif aktion == "2":
        while True:
            try:
                betrag = float(input("Ausgabe hinzufügen (€): "))
                if betrag > 0:
                    ausgabe.append(betrag)
                    print("Ihre Ausgaben (€): ", ausgabe)
                else:
                    print("Betrag muss eine positive Zahl sein")
            except ValueError:
                print("Bitte geben Sie eine gültige Zahl an")
    elif aktion == "3":
        print("Ihre Buchungen")
        print("Einnahmen in €")
        if einnahme:
            for betrag in einnahme:
                print(betrag)
        else:
            print("Keine Einnahmen vorhanden")
        
        print("Ausgaben in €")
        if ausgabe:
            for z_a in ausgabe:
                print(z_a)
        else:
            print("Keine Ausgabe vorhanden")
    elif aktion == "4":
        sum_einnahmen = sum(einnahme)
        sum_ausgaben = sum(ausgabe)
        kontostand = sum_einnahmen - sum_ausgaben
        print("Ihr Kontostand liegt bei: ", kontostand, "€")
    elif aktion == "5":
        print("Benutzer möchte das Programm beenden")
        break
    else:
        print("Ungültige Auswahl - Keine Konkrete Auswahl angegeben")
