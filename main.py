import requests
import tkinter as tk
from tkinter import ttk

API_KEY = 'aee431f697fe601fa2c5d035926ac468'
API_ENDPOINT = 'http://api.exchangeratesapi.io/v1/latest'


def get_exchange_rates(base_currency):
    url = f'{API_ENDPOINT}?access_key={API_KEY}&base={base_currency}'

    try:
        response = requests.get(url)
        data = response.json()

        if 'error' in data:
            print(f"Error: {data['error']['info']}")
            return None

        rates = data['rates']
        return rates
    except requests.exceptions.RequestException as e:
        print('Error occurred:', e)
        return None


def convert_currency():
    base_currency = base_currency_combobox.get()
    target_currency = target_currency_combobox.get()
    amount = float(amount_entry.get())

    rates = get_exchange_rates(base_currency)

    if rates is not None and target_currency in rates:
        conversion_rate = rates[target_currency]
        converted_amount = amount * conversion_rate
        result_label['text'] = f'{amount} {base_currency} = {converted_amount} {target_currency}'
    else:
        result_label['text'] = 'Error: Conversion failed'


# Create a GUI window
window = tk.Tk()
window.title('Currency Converter')

# Create input widgets
base_currency_combobox = ttk.Combobox(window, values=['EUR', 'USD', 'GBP', 'CAD'])
base_currency_combobox.set('EUR')
base_currency_combobox.pack(pady=10)

target_currency_combobox = ttk.Combobox(window, values=['USD', 'EUR', 'GBP', 'CAD'])
target_currency_combobox.set('USD')
target_currency_combobox.pack(pady=10)

amount_entry = ttk.Entry(window)
amount_entry.pack(pady=10)

convert_button = ttk.Button(window, text='Convert', command=convert_currency)
convert_button.pack(pady=10)

result_label = ttk.Label(window, text='')
result_label.pack(pady=10)

# Run the GUI window
window.mainloop()