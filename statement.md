## 📌Program Statement
As the world becomes increasingly globalized, it is normal to have financial transactions that cross borders. 
However, this can easily lead to discrepancy and errors in finances whenever there is a manual currency conversion using a static table .
Many of the current solutions force users to filter through complicated, advertisement-ridden financial news sites simply to obtain a simple exchange rate. 

## 📌Scope of the Project
This project aims to develop a Currency Converter, a client-side desktop application.
It bridges the gap between raw financial data and user-friendly tools.

The scope includes:
* External Integration: Using a live API - ExchangeRate-API for dynamic data fetch.
* Data Processing: Logic to process cross currency calculations like directly converting INR to USD.
* Resilience means that the application still works with less data when some network connection is lost.
  
## 📌Target Users
* International Travelers: People who need quick, accurate estimates of expenses in foreign currencies.
* Students & Researchers: Users who need to verify economic data or calculate costs for international studies.
* Small Business Owners: These are traders who need to verify rough exchange rates quickly before making international purchase decisions.
* General Users: The people who need fast and easy utility for everyday currency conversion, without additional browser overhead.
  
## 📌High-Level Features 
* Live Rate Extraction: Automated fetching of the latest exchange rates for more than 150 global currencies.
* Smart Input Validation: A robust error-handling system that refuses to take non-numeric or invalid inputs, thus preventing crashes.
* Offline Fallback Mode: A failsafe mode that resorts to cached/default rates so that the system remains usable during periods of network failure.
* Modern GUI: A clean, user-friendly interface using Tkinter where inputs, controls, and results are separated.
