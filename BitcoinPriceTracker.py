#!/usr/bin/env python
# coding: utf-8

# In[1]:


class BitcoinPrice:
    import requests
    from time import sleep
    import csv
    @staticmethod
    def response():
        try:
            url = "https://api.coinbase.com/v2/prices/buy?currency=USD"
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            price = response.json()['data']['amount']
            return float(price)
        except requests.exceptions.RequestException as e:
            print(f"Error fetching price: {e}")
            return None
    
    def __init__(self, API_Key, number, exchange_rate=100000):
        self.buy = self.response()
        self.API_Key = API_Key
        self.number = number
        self.exchange_rate = exchange_rate
        self.history = []  
    
    def price(self):
        if self.buy is not None:
            self.history.append(self.buy)  
            return f"Bitcoin price in dollars: {self.buy:.2f} and Bitcoin price in Tomans: {self.buy * self.exchange_rate:.0f}"
        else:
            return "Error fetching Bitcoin price."
    
    def price_min(self):
        while True:
            self.buy = self.response()
            print(self.price())
            print(self.price_change())  
            print("-------------------------------------------------------")
            self.save_to_csv()  
            sleep(60)
    
    def price_send(self):
        while True:
            buy = self.response()
            if buy is None:
                print("Failed to fetch Bitcoin price. Skipping SMS sending.")
                sleep(100)
                continue

            url = f'https://api.kavenegar.com/v1/{self.API_Key}/sms/send.json'
            payload = {'receptor': self.number, 'message': f'Bitcoin price: {buy:.2f} USD'}
            
            try:
                response = requests.post(url, data=payload)
                response.raise_for_status()
                print(f'Sent Bitcoin price ({buy:.2f} USD) to {self.number}')
            except requests.exceptions.RequestException as e:
                print(f"Error sending SMS: {e}")

            sleep(100)

    def price_change(self):
        if len(self.history) < 2:
            return "No previous price data available."
        
        last_price = self.history[-2]
        current_price = self.history[-1]
        change = current_price - last_price
        percent_change = (change / last_price) * 100

        return f"Price changed by {change:.2f} USD ({percent_change:.2f}%)"
    
    def save_to_csv(self, filename="bitcoin_prices.csv"):
        with open(filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([self.buy])
        print(f"Price saved to {filename}")

