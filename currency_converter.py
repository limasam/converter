import requests
import tkinter as tk
from tkinter import ttk, messagebox

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Конвертер валют")
        self.root.geometry("300x200")

        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()
        self.amount_var = tk.StringVar()

        self.from_currency_label = tk.Label(root, text="Из валюты:", font=("Arial", 12))
        self.from_currency_label.grid(row=0, column=0, padx=10, pady=10)
        self.from_currency_combo = ttk.Combobox(root, textvariable=self.from_currency_var, values=["USD", "EUR", "RUB"])
        self.from_currency_combo.grid(row=0, column=1, padx=10, pady=10)
        self.from_currency_combo.current(0)

        self.to_currency_label = tk.Label(root, text="В валюту:", font=("Arial", 12))
        self.to_currency_label.grid(row=1, column=0, padx=10, pady=10)
        self.to_currency_combo = ttk.Combobox(root, textvariable=self.to_currency_var, values=["USD", "EUR", "RUB"])
        self.to_currency_combo.grid(row=1, column=1, padx=10, pady=10)
        self.to_currency_combo.current(1)

        self.amount_label = tk.Label(root, text="Сумма:", font=("Arial", 12))
        self.amount_label.grid(row=2, column=0, padx=10, pady=10)
        self.amount_entry = tk.Entry(root, textvariable=self.amount_var, font=("Arial", 12))
        self.amount_entry.grid(row=2, column=1, padx=10, pady=10)

        self.convert_button = tk.Button(root, text="Конвертировать", command=self.convert)
        self.convert_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def convert(self):
        try:
            amount = float(self.amount_var.get())
            from_currency = self.from_currency_combo.get()
            to_currency = self.to_currency_combo.get()

            if from_currency and to_currency:
                url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
                response = requests.get(url)
                data = response.json()

                if "rates" in data and to_currency in data["rates"]:
                    rate = data["rates"][to_currency]
                    result = amount * rate
                    messagebox.showinfo("Результат", f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}")
                else:
                    raise ValueError("Не удалось получить данные о курсе конвертации.")
            else:
                raise ValueError("Введите валюты для конвертации.")
        except ValueError as e:
            messagebox.showerror("Ошибка", str(e))

if __name__ == "__main__":
    root = tk.Tk()
    currency_converter = CurrencyConverter(root)
    root.mainloop()
