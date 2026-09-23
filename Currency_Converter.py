import tkinter as tk
from tkinter import ttk, messagebox
import requests

class CurrencyConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Currency Converter")
        self.root.geometry("450x500")
        
        # Connecting api to the program
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.rates = {}
        
        # Run setup functions
        self.fetch_rates()
        self.create_widgets()

    def fetch_rates(self):
        try:
            response = requests.get(self.api_url)
            data = response.json()
            self.rates = data.get("rates", {})
        except Exception as e:
            # If API is not connected
            messagebox.showerror("Error", f"Network Error: {e}")
            self.rates = {"USD": 1.0, "INR": 83.0, "EUR": 0.92} 

    def convert(self):
        try:
            amount_val = self.amount_entry.get()
            
            # Check if input is empty
            if not amount_val:
                messagebox.showwarning("Input Error", "Please enter an amount")
                return

            amount = float(amount_val)
            from_currency = self.from_var.get()
            to_currency = self.to_var.get()

            # Conversion Logic: (Amount / From_Rate) * To_Rate
            if from_currency != "USD":
                amount = amount / self.rates[from_currency]
            
            result = round(amount * self.rates[to_currency], 2)
            self.result_label.config(text=f"Result: {result} {to_currency}")
        
        # Error to the value entered
        except ValueError:
            messagebox.showwarning("Wrong Amount Entered", "Please enter a valid numeric amount")
        except KeyError:
            messagebox.showerror("Error", "Selected currency not available.")

    def create_widgets(self):
        # Title
        tk.Label(self.root, text="Currency Converter", font=("Arial", 18, "bold")).pack(pady=10)

        # Amount Input
        tk.Label(self.root, text="Amount:").pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack(pady=15)

        currencies_list = list(self.rates.keys())
        
        # From Selection
        tk.Label(self.root, text="From:").pack()
        self.from_var = tk.StringVar(value="USD")
        ttk.Combobox(self.root, textvariable=self.from_var, values=currencies_list).pack()

        # To Selection
        tk.Label(self.root, text="To:").pack()
        self.to_var = tk.StringVar(value="INR")
        # Changed 'values=currencies' to 'values=currencies_list'
        ttk.Combobox(self.root, textvariable=self.to_var, values=currencies_list).pack()

        # Convert button
        tk.Button(self.root, text="Convert Now", command=self.convert, bg="light blue", fg="black").pack(pady=20)

        # Result of the conversion
        self.result_label = tk.Label(self.root, text="Result: --", font=("Arial", 18, "bold"))
        self.result_label.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = CurrencyConverter(root)
    root.mainloop()
