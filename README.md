# Bitcoin Price Tracker

A Python-based Bitcoin price tracker that fetches the latest Bitcoin price in USD, converts it to Toman, logs the data, and optionally sends SMS notifications.

## Features
- Fetches real-time Bitcoin price from Coinbase API
- Converts Bitcoin price to Iranian Toman (adjustable exchange rate)
- Logs price history and saves it to a CSV file
- Sends SMS notifications with the latest Bitcoin price (via Kavenegar API)
- Displays price changes in percentage
- Runs automatically at set intervals (default: every 60 seconds)

## Prerequisites
Ensure you have the following installed:
- Python 3.x
- `requests` library

You can install dependencies using:
```sh
pip install requests
```

## Usage

1. Clone this repository:
```sh
git clone https://github.com/yourusername/bitcoin-price-tracker.git
cd bitcoin-price-tracker
```

2. Set up your **Kavenegar API Key** and **phone number**:

```python
btc = BitcoinPrice('YOUR_KAVENEGAR_API_KEY', 'YOUR_PHONE_NUMBER')
```

3. Run the script:
```sh
python bitcoin_tracker.py
```

## Class Overview
### `BitcoinPrice`
#### Methods:
- `response()` – Fetches Bitcoin price in USD
- `price()` – Returns Bitcoin price in both USD and Tomans
- `price_min()` – Updates and logs price every 60 seconds
- `price_send()` – Sends SMS with the latest Bitcoin price
- `price_change()` – Calculates the percentage change in price
- `save_to_csv()` – Saves price data to a CSV file

## Example Output
```sh
Bitcoin price in dollars: 42600.25 and Bitcoin price in Tomans: 4,260,025,000
Price changed by 200.50 USD (0.47%)
Price saved to bitcoin_prices.csv
-------------------------------------------------------
Sent Bitcoin price (42600.25 USD) to +989123456789
```

## Notes
- Make sure your API key is valid for sending SMS messages.
- If the API request fails, the script will handle errors gracefully and retry automatically.

## License
This project is licensed under the MIT License.

