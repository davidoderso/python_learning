import json

einnahme = []
ausgabe = []

def load_bookings():
    # load bookings out of bookings.txt
    try:
        with open("bookings.json", "r", encoding="utf-8") as datei:
            daten = json.load(datei)

            einnahme.clear()
            ausgabe.clear()

            einnahme.extend(daten["einnahme"])
            ausgabe.extend(daten["ausgabe"])

    except FileNotFoundError:
        print("Noch keine gespeicherten Buchungen vorhanden.")

def safe_bookings():

    daten = {
        "einnahme": einnahme,
        "ausgabe": ausgabe
    }

    with open("bookings.json", "w", encoding="utf-8") as datei:
        json.dump(daten, datei, indent=4, ensure_ascii=False)

    
def add_amount():
    # Add an Amount to your Inputs
    while True:
        try:
            betrag = float(input("Einnahme hinzufügen (€): "))
            if betrag > 0:
                date= input("Datum (TT.MM.JJJJ): ")
                description = input("Woher stammt die Einnahme? ")
                return {
                    "amount": betrag,
                    "date": date,
                    "description": description
                } 
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
                date = input("Datum (TT.MM.JJJJ): ")
                description = input("Wo ist das Geld hin? ")
                return {"amount": betrag,
                        "date" : date,
                        "description": description
                        }
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
            print(f'{betrag["date"]} | {betrag["description"]}: {betrag["amount"]:.2f} €')
    else:
        print("Keine Einnahmen vorhanden")

    if ausgabe:
        print("Ausgaben in €")
        for betrag in ausgabe:
            print(f'{betrag["date"]} | {betrag["description"]}: {betrag["amount"]:.2f} €')
    else:
        print("Keine Ausgaben vorhanden")

def get_account_balance():
        # Get Account Balance out of input and spendings
        sum_einnahmen = sum( buchung["amount"] for buchung in einnahme)
        sum_ausgaben = sum( buchung["amount"] for buchung in ausgabe)
        kontostand = sum_einnahmen - sum_ausgaben
        print(f"Ihr Kontostand liegt bei: {kontostand:.2f} €")


print("Mein Verwaltungshausbuch")
print("1. Einnahmen hinzufügen")
print("2. Ausgaben hinzufügen")
print("3. Buchungen anzeigen")
print("4. Kontostand anzeigen")
print("5. Programm beenden")

load_bookings()

while True:

    aktion = input("Was wollen Sie machen? Bitte geben Sie eine Zahl von 1-5 an ")

    if aktion == "1":
        col_amount = add_amount()
        einnahme.append(col_amount)
        print(einnahme)
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
