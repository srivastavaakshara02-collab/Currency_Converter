import requests
import sys


class CurrencyConverter:
    def __init__(self):
        # API used to get the latest exchange rates
        self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
        self.rates = {}

        self.fetch_rates()

    def fetch_rates(self):
        try:
            # Send a request to the API
            response = requests.get(self.api_url, timeout=10)
            response.raise_for_status()

            # Convert the response into JSON
            data = response.json()

            # Store the exchange rates in a dictionary
            self.rates = data.get("rates", {})

        except Exception as e:
            print("Network Error:", e)
            print("Using predefined fallback rates.")

            # Use these rates if the API cannot be reached
            self.rates = {
                "USD": 1.0,
                "INR": 83.0,
                "EUR": 0.92
            }

    def convert_amount(self, amount, from_currency, to_currency):
        # Convert the source currency to USD first
        if from_currency != "USD":
            amount = amount / self.rates[from_currency]

        # Convert USD to the target currency
        result = amount * self.rates[to_currency]

        return round(result, 2)


def run_cli():
    print("=" * 40)
    print("       CURRENCY CONVERTER")
    print("=" * 40)

    converter = CurrencyConverter()

    try:
        # Get amount from the user
        amount_input = input("\nEnter amount: ")

        if not amount_input:
            print("Error: Please enter an amount.")
            return

        amount = float(amount_input)

        # Get source and target currencies
        from_currency = input(
            "Enter source currency (example: INR): "
        ).upper()

        to_currency = input(
            "Enter target currency (example: USD): "
        ).upper()

        # Check if currencies are available
        if from_currency not in converter.rates:
            print("Error: Source currency not available.")
            return

        if to_currency not in converter.rates:
            print("Error: Target currency not available.")
            return

        # Perform the conversion
        result = converter.convert_amount(
            amount,
            from_currency,
            to_currency
        )

        print("\n----------------------------------------")
        print(
            f"{amount_input} {from_currency} = "
            f"{result} {to_currency}"
        )
        print("----------------------------------------")

    except ValueError:
        print("Error: Please enter a valid numeric amount.")

    except KeyError:
        print("Error: Selected currency not available.")


def run_gui():
    # Tkinter is imported only when GUI mode is selected
    import tkinter as tk
    from tkinter import ttk, messagebox

    class CurrencyConverterGUI:
        def __init__(self, root):
            self.root = root
            self.root.title("Currency Converter")
            self.root.geometry("450x500")

            # API used to get exchange rates
            self.api_url = "https://api.exchangerate-api.com/v4/latest/USD"
            self.rates = {}

            # Get rates and create the GUI
            self.fetch_rates()
            self.create_widgets()

        def fetch_rates(self):
            try:
                # Send a request to the API
                response = requests.get(self.api_url, timeout=10)
                response.raise_for_status()

                # Convert response to JSON
                data = response.json()

                # Store rates in a dictionary
                self.rates = data.get("rates", {})

            except Exception as e:
                messagebox.showerror(
                    "Error",
                    f"Network Error: {e}"
                )

                # Use fallback rates if the API fails
                self.rates = {
                    "USD": 1.0,
                    "INR": 83.0,
                    "EUR": 0.92
                }

        def convert(self):
            try:
                # Get the amount entered by the user
                amount_val = self.amount_entry.get()

                # Check for empty input
                if not amount_val:
                    messagebox.showwarning(
                        "Input Error",
                        "Please enter an amount"
                    )
                    return

                amount = float(amount_val)

                # Get selected currencies
                from_currency = self.from_var.get()
                to_currency = self.to_var.get()

                # Convert source currency to USD
                if from_currency != "USD":
                    amount = amount / self.rates[from_currency]

                # Convert USD to target currency
                result = round(
                    amount * self.rates[to_currency],
                    2
                )

                # Display the result
                self.result_label.config(
                    text=f"Result: {result} {to_currency}"
                )

            except ValueError:
                messagebox.showwarning(
                    "Wrong Amount Entered",
                    "Please enter a valid numeric amount"
                )

            except KeyError:
                messagebox.showerror(
                    "Error",
                    "Selected currency not available."
                )

        def create_widgets(self):

            # Application heading
            tk.Label(
                self.root,
                text="Currency Converter",
                font=("Arial", 18, "bold")
            ).pack(pady=10)

            # Amount input
            tk.Label(
                self.root,
                text="Amount:"
            ).pack()

            self.amount_entry = tk.Entry(self.root)
            self.amount_entry.pack(pady=15)

            # Get available currencies
            currencies_list = list(self.rates.keys())

            # From currency
            tk.Label(
                self.root,
                text="From:"
            ).pack()

            self.from_var = tk.StringVar(value="USD")

            ttk.Combobox(
                self.root,
                textvariable=self.from_var,
                values=currencies_list
            ).pack()

            # To currency
            tk.Label(
                self.root,
                text="To:"
            ).pack()

            self.to_var = tk.StringVar(value="INR")

            ttk.Combobox(
                self.root,
                textvariable=self.to_var,
                values=currencies_list
            ).pack()

            # Conversion button
            tk.Button(
                self.root,
                text="Convert Now",
                command=self.convert,
                bg="light blue",
                fg="black"
            ).pack(pady=20)

            # Display result
            self.result_label = tk.Label(
                self.root,
                text="Result: --",
                font=("Arial", 18, "bold")
            )

            self.result_label.pack()

    root = tk.Tk()
    app = CurrencyConverterGUI(root)
    root.mainloop()


# CLI is the default mode
if __name__ == "__main__":

    if "--gui" in sys.argv:
        run_gui()
    else:
        run_cli()