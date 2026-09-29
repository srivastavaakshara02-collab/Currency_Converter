## 📌Program Statement

In today's global economy, financial transactions often involve cross border transactions, cross nations transactions and cross currency transaction. Manually converting between currencies using an exchange-rate data table can be prone to many errors and it also can be outdated and wrong. Additionally, a user might need to navigate a complex financial website to perform the task which is a simple conversion between two currencies.

This project builds up a simple Currency Converter that performs exchange-rate based conversions through two mediums, which are command-line interface and a graphical user interfaces.

## 📌Scope of the Project

This project aims to build a Currency Converter as a Python-based programming application.

The major aspects of this project includes:

* **External Integration:** Using the ExchangeRate-API, exchange rates data will be obtained.
* **Data Processing:** Currency exchange rates data will be processed and cross-currency calculations will be done.
* **Command-Line Execution:** The project will be developed in a way that it can be run from a python terminal as a command-line application and that the project can be executed without a GUI.
* **Graphical Interface:** A GUI will be added using Tkinter to provide an alternative to the command-line interface for users who prefer and like a visual interface.
* **Input Validation:** The program will be able to handle empty and non-numeric amount input entries and invalid currency selection.
* **Resilience:** The program will have a fallback set of exchange rates in case the external API is unavailable, which can happen during no internet connection or break in connection.

## 📌Target Users

* **International Travelers:** These are people that need to quickly estimate the cost of services and goods in another country using their local currency.
* **Students & Researchers:** This category of users will benefit from the application when doing currency exchange rate calculations as part of their course work, academic or research-related work.
* **Small Business Owners:** This group of users will be able to perform quick approximate currency exchange calculations.
* **General Users:** For people that need a currency conversion tool but do not want to navigate through a complex and difficult financial website.

## 📌High-Level Features

* **Live Rate Extraction:** The application will be able to get currency exchange rates from an ExchangeRate-API.
* **Cross-Currency Conversion:** The application will convert between any of the available currencies in the API using the USD as the base currency. 
* **Command-Line Interface:** Allows the application to be run directly from a terminal.
* **Input Validation:** The program will be able to handle empty and non-numeric amount input entries.
* **Currency Validation:** Checks whether selected currency codes are available.
* **Fallback Mode:** The program will have a predefined fallback set of exchange rates in case the external API is unavailable or can't be reached.
* **GUI:** Provides a Tkinter GUI interface with input fields, drop-down menu selections and will display the result for ease of use.
