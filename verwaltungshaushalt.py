import json

einnahme = []
ausgabe = []
categories = []

def load_bookings():
    # load bookings out of bookings.txt
    try:
        with open("bookings.json", "r", encoding="utf-8") as datei:
            daten = json.load(datei)

            einnahme.clear()
            ausgabe.clear()
            categories.clear

            einnahme.extend(daten["einnahme"])
            ausgabe.extend(daten["ausgabe"])
            categories.extend(daten["categories"])

    except FileNotFoundError:
        print("Noch keine gespeicherten Buchungen vorhanden.")

def safe_bookings():

    daten = {
        "einnahme": einnahme,
        "ausgabe": ausgabe,
        "categories": categories
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
                category = get_category("Einnahme")
                return {
                    "amount": betrag,
                    "date": date,
                    "description": description,
                    "category": category
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
                category = get_category("Ausgabe")
                return {"amount": betrag,
                        "date" : date,
                        "description": description,
                        "category": category
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
            print(f'{betrag["date"]} | {betrag["category"]} | {betrag["description"]}: {betrag["amount"]:.2f} €')
    else:
        print("Keine Einnahmen vorhanden")

    if ausgabe:
        print("Ausgaben in €")
        for betrag in ausgabe:
            print(f'{betrag["date"]} | {betrag["category"]} | {betrag["description"]}: {betrag["amount"]:.2f} €')
    else:
        print("Keine Ausgaben vorhanden")

def get_account_balance():
        # Get Account Balance out of input and spendings
        sum_einnahmen = sum( buchung["amount"] for buchung in einnahme)
        sum_ausgaben = sum( buchung["amount"] for buchung in ausgabe)
        kontostand = sum_einnahmen - sum_ausgaben
        print(f"Ihr Kontostand liegt bei: {kontostand:.2f} €")

def new_category():
    type = input("Zu was soll die Kategorie hinzugefügt werden? (Einnahme/Ausgabe)")

    if type == "Einnahme":
        name = input("Name der neuen Kategorie: ")
        if name:
            return {"type": type,
                    "name": name
                    }
        else:
            print("Kein Name angegeben")
    elif type == "Ausgabe":
        name = input("Name der neuen Kategorie: ")
        if name:
            return {"type": type,
                    "name": name
                    }
        else:
            print("Kein Name angegeben")

        
def get_all_category():
    # {type (input or spending), name}

    if categories:
        print("Ihre Kategorien:")
        for category in categories:
            print(f'{category["type"]} - {category["name"]}')
    #FIXME change to possible inputs (yes, y, enter and no, n)
    new_cat = input("Wollen Sie eine Kategorie hinzufügen? (yes/no) ")

    if new_cat == "yes":
        new_cat_infos = new_category()

        categories.append(new_cat_infos)
    elif new_cat == "no":
        print("Keine neue Kategorie hinzugefügt")

def get_category(booking_type):
    # Categories which has the same type (input or spendings)
    same_cat = [
        category for category in categories
        if category["type"] == booking_type
    ]

    if same_cat:
        print("vorhandene Kategorien:")
        for i, category in enumerate(same_cat, start=1):
            print(f'{i}. {category["name"]}')
        auswahl = input("Nummer auswählen oder 'neu' eingeben: ")

        if auswahl == "neu":
            new_category()
            if new_cat and new_cat["type"] == booking_type:
                categories.append(new_cat)
                return new_cat["name"]
            else:
                print("Keine passende Kategorie hinzugefügt.")
                return None

        try:
            nummer = int(auswahl)

            if 1 <= nummer <= len(same_cat):
                return same_cat[nummer - 1]["name"]
            else:
                print("Diese Nummer gibt es nicht.")
                return None

        except ValueError:
            print("Bitte eine Nummer oder 'neu' eingeben.")
            return None

    else:
        print("Noch keine passenden Kategorien vorhanden.")
        new_cat = new_category()

        if new_cat and new_cat["type"] == booking_type:
            categories.append(new_cat)
            return new_cat["name"]

        print("Keine passende Kategorie hinzugefügt.")
        return None

def start():
    print("Mein Verwaltungshausbuch")
    print("1. Einnahmen hinzufügen")
    print("2. Ausgaben hinzufügen")
    print("3. Buchungen anzeigen")
    print("4. Kontostand anzeigen")
    print("5. Kategorien bearbeiten")
    print("6. Programm beenden")

    load_bookings()

    while True:

        aktion = input("Was wollen Sie machen? Bitte geben Sie eine Zahl von 1-6 an ")

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
            get_all_category()
        elif aktion == "6":
            print("Benutzer möchte das Programm beenden")
            safe_bookings()
            break
        else:
            print("Ungültige Auswahl - Keine Konkrete Auswahl angegeben")
