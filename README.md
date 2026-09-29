# Currency_Converter
# Currency_Converter-Introduction to Programming Project

## 📌Overview
This project here shows a currency conversion application done in Python programming language with a command-line interface (CLI) and a graphical user interface (GUI), both.
It uses ExchangeRate-API to search for the exchange-rate data and allows the user to convert any amount from one currency to another currency.

The CLI can run directly through a terminal, while the Tkinter GUI feature provides a simple visual interface. In case of failure to connect to ExchangeRate-API, the program contains a set of default currency exchange rates and can work without an internet connection.

## 📌Features
* **Real-time data fetching:** The program uses ExchangeRate-API to provide the most accurate exchange rates based on current data, trends and rates. It will update based on the rising or falling value of a currency.
* **Command-Line Interface:** The currency conversion function can be launched directly from the command line using this.
* **User-Friendly GUI:** The program has a simple interface with fields for entering amount and selecting currencies from the drop-down list. It also has a button to perform a currency conversion and displays results after pressing it. It is actively using Tkinter. 
* **Input Validation:** It proccesses and handles the empty and non-numeric amount inputted by the user without causing any errors.
* **Currency Validation:** It checks whether the selected currencies are available or not in the given program.
* **Fallback Mode:** In case of an API connection failure, the program uses default exchange rates for USD, INR, and EUR.
* **Cross-Platform Compatibility:** The program can run on any operating system that supports a Python programming language and has all the necessary dependencies installed.

## 📌Technologies/Tools Used
* **Programming Language:** Python 3.14.7 (3.14 or 3.x)
* **GUI Framework:** Tkinter
* **HTTP Library:** Requests
* **Data Format:** JSON
* **API Service:** ExchangeRate-API

## 📌Steps to Install & Run the Project

### 1. Requirement
Install Python 3.x and check the installed version with the follwoing:
```bash
python --version
```

### 2. Clone/Download the Repository
Download or Clone the project and open the project folder in a terminal.

### 3. Install Dependencies
Install all dependencies by running the following:
Run:
```bash
python -m pip install requests
```

### 4. ▶️ Run in CLI Mode
This is the default mode. Run the following command:
```bash
python Currency_Converter.py
```

The program asks for the amount, source currency, and target currency.

for example:
```text
========================================
       CURRENCY CONVERTER
========================================

Enter amount: 100
Enter source currency (example: INR): USD
Enter target currency (example: USD): INR

----------------------------------------
100 USD = 9588.0 INR
----------------------------------------
```
The result may vary slightly because the exchange rate data comes from an API.

### 5. ▶️ Run the Graphical Interface
To launch the Tkinter GUI interfavce:
```bash
python Currency_Converter.py --gui
```

## 📌How the Conversion Works
The value of the source currency and the target currency is quoted in terms of USD which means that the API uses USD as the base currency.

So, if the source currency is not USD:

```text
USD Amount = Amount / Source Currency Rate
```

Then:
```text
Target Amount = USD Amount × Target Currency Rate
```

The value of the final result is then rounded off to two (2) decimal places.

## 📌Instructions for Testing

### 1. Standard Conversion Test
* Run the application.
* Enter any simple amount such as `100` or `10`.
* Select the source and target currencies from the drop down menu.
* Perform the conversion of the amount.

**Expected Output:** The result of the conversion will be displayed in the CLI or GUI, whatever interface chosen or present.

### 2. Input Validation Test
* Leave the amount field blank or enter a non-numeric value such as `abc`.
* Proceed with the conversion.

**Expected Output:** An input error is displayed by the application instead of the it crashing.

### 3. Currency Validation Test
* Run the CLI.
* Enter a currency code that is not available in the application.

**Expected Output:** The program displays that the selected currency is not available.

### 4. Network Error / Fallback Test
* Disconnect from the internet service provider or turn off your wifi connection.
* Start and proceed to run the application.
* If the API can't be reached, predefined fallback exchange rates are used.

## 📌Project Structure
```text
Currency_Converter/
│
├── Currency_Converter.py
├── README.md
├── statement.md
├── project report.pdf
└── currency screen recording.mp4
```

## 📌Screenshots and Recording
The repository contains the project screen recording, and the project report has the GUI screenshots and test results.

The CLI can be tested using the following commands:
```bash
python Currency_Converter.py
```

## 📌Limitations
* Current exchange-rate information relies on the ExchangeRate-API.
* The application has a predefined fallback exchange rates for currencies such as USD, INR, and EUR. These rates are fixed and may not reflect the current market values.
* The application does not support storing previous conversion history..

## 📌Future Enhancements
* The application can be extended to include conversion history and storage.
* Visual display of the exchange rate trends in graphs form can be included.
* The application can have advanced input validation and error handling.
* More financial features and cryptos can be added for conversion.
* The GUI can be more engaging and customizable.
