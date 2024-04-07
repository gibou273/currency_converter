from tkinter import Tk, StringVar, Label, OptionMenu, Entry, Button
from backend import get_current_rate, currency_list, get_currency

# Call the get_current_rate function with default values, so the 2 OptionMenu can have values
get_current_rate("SEK", "USD")


window = Tk()
window.title("Currency Converter")
window.geometry("700x500")
window.config(padx=160, pady=100)


# Variable to keep track of the option
# selected in OptionMenu
value_currency_from = StringVar(window)
value_currency_to = StringVar(window)
# Set the default value of the variable
value_currency_from.set("Select Currency")
value_currency_to.set("Select Currency")

# Logo Text
log_text = Label(text="Currency Converter", fg="blue", font=("Ariel", 20, "bold"))
log_text.grid(row=0, column=1, padx=10, pady=10)

from_currency_label = Label(text="From Currency:")
from_currency_label.grid(row=1, column=0)
from_option_menu = OptionMenu(window, value_currency_from, *currency_list)
from_option_menu.config(width=23)
from_option_menu.grid(row=1, column=1, padx=10, pady=10)

to_currency_label = Label(text="To Currency:")
to_currency_label.grid(row=2, column=0)
to_option_menu = OptionMenu(window, value_currency_to, *currency_list)
to_option_menu.config(width=23)
to_option_menu.grid(row=2, column=1, padx=10, pady=10)

amount_label = Label(text="Amount:")
amount_label.grid(row=3, column=0)
amount_entry = Entry()
amount_entry.grid(row=3, column=1, padx=10, pady=10)

calculate_btn = Button(text="Convert", command=lambda: get_currency(value_currency_from, value_currency_to, amount_entry, current_amount))
calculate_btn.grid(row=4, column=1, padx=10, pady=10)

current_amount = Label(text=0.0)
current_amount.grid(row=5, column=1)


window.mainloop()
