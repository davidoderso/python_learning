import verwaltungshaushalt
import tkinter as tk

fenster = tk.Tk()
fenster.title("Mein Haushaltsbuch")
fenster.geometry("600x400")
fenster.configure(bg="lightblue")

ueberschrift = tk.Label(
    fenster,
    text="Mein Haushaltsbuch",
    font=("Arial", 20, "bold"),
    fg="black",
    bg="lightblue"
)
ueberschrift.pack(pady=20)

kontostand = tk.Label(
    fenster,
    text="Aktueller Kontostand: 0.00 €",
    font=("Arial", 14),
    fg="black",
    bg="lightblue"
)
kontostand.pack(pady=10)

def add_amount_gui():
    print("Neue Einnahme hinzufügen:")
    verwaltungshaushalt.add_amount()


def add_spending_gui():
    print("Neue Ausgabe hinzufügen.")


button_add_amount = tk.Button(
    fenster,
    text="Einnahme hinzufügen",
    command=add_amount_gui
)

label_amount = tk.Label(
        fenster,
        text="Betrag der Einnahme (€):"
    )
label_amount.pack(pady=5)

entry_amount = tk.Entry(fenster)
entry_amount.pack(pady=5)

button_add_spending = tk.Button(
    fenster,
    text="Ausgabe hinzufügen",
    command=add_spending_gui
)

button_add_amount.pack(pady=10)
button_add_spending.pack(pady=10)
fenster.mainloop()