einnahme = []
ausgabe = []

def load_bookings():
    # load bookings out of bookings.txt
    einnahme.clear()
    ausgabe.clear()
    section = None
    try:
        with open("bookings.txt", "r") as datei:
            for zeile in datei:
                zeile = zeile.strip()

                if zeile == "input":
                    section = "einnahme"
                
                elif zeile == "spendings":
                    section = "ausgabe"

                elif section == "einnahme":
                    betrag = float(zeile)
                    einnahme.append(betrag)
                elif section == "ausgabe":
                    betrag = float(zeile)
                    ausgabe.append(betrag)
    except FileNotFoundError:
        print("Keine Save-Datei gefunden.")

def safe_bookings():
    with open("bookings.txt", "w") as datei:
        datei.write("My Account Bookings\n")

        datei.write("input\n")
        if einnahme:
            for betrag in einnahme:
                datei.write(str(betrag)+ "\n")
        
        datei.write("spendings\n")
        if ausgabe:
            for betrag in ausgabe:
                datei.write(str(betrag)+ "\n")
    
def add_amount():
    # Add an Amount to your Inputs
    while True:
        try:
            betrag = float(input("Einnahme hinzufügen (€): "))
            if betrag > 0:
                return betrag
            else:
                print("Betrag muss eine positive Zahl sein")
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl ein")

def add_spending():
    # Add a Money Spending to your booking
    while True:
        try:
            betrag = float(input("Ausgabe hinzufügen (€): "))
            if betrag > 0:
                return betrag
            else:
                print("Betrag muss eine positive Zahl sein")
        except ValueError:
            print("Bitte geben Sie eine gültige Zahl an")

def get_bookings():
    # get all Account bookings
    print("Ihre Buchungen")

    if einnahme:
        print("Einnahmen in €")
        for betrag in einnahme:
            print(betrag)
    else:
        print("Keine Einnahmen vorhanden")

    if ausgabe:
        print("Ausgaben in €")
        for z_a in ausgabe:
            print(z_a)
    else:
        print("Keine Ausgaben vorhanden")

def get_account_balance():
        # Get Account Balance out of input and spendings
        sum_einnahmen = sum(einnahme)
        sum_ausgaben = sum(ausgabe)
        kontostand = sum_einnahmen - sum_ausgaben
        print(f"Ihr Kontostand liegt bei: {kontostand:.2f} €")


print("Mein Verwaltungshausbuch")
print("1. Einnahmen hinzufügen")
print("2. Ausgaben hinzufügen")
print("3. Buchungen anzeigen")
print("4. Kontostand anzeigen")
print("5. Programm beenden")

while True:
    load_bookings()
    aktion = input("Was wollen Sie machen? Bitte geben Sie eine Zahl von 1-5 an ")

    if aktion == "1":
        amount = add_amount()
        einnahme.append(amount)
    elif aktion == "2":
        spending = add_spending()
        ausgabe.append(spending)
    elif aktion == "3":
        get_bookings()
    elif aktion == "4":
        get_account_balance()
    elif aktion == "5":
        print("Benutzer möchte das Programm beenden")
        safe_bookings()
        break
    else:
        print("Ungültige Auswahl - Keine Konkrete Auswahl angegeben")
