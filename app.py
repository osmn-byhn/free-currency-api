from flask import Flask, request, jsonify
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def fetch_exchange_rate(base_currency, target_currency):
    url = f"https://www.google.com/finance/quote/{target_currency}-{base_currency}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        exchange_rate = soup.find('div', class_='YMlKec fxKbKc').text
        return exchange_rate
    else:
        return None

@app.route('/exchange-rate', methods=['GET'])
def get_rate():
    base_currency = request.args.get('base', 'EUR')
    target_currency = request.args.get('target', 'TRY')
    rate = fetch_exchange_rate(base_currency, target_currency)

    if rate:
        return jsonify({
            "base_currency": base_currency,
            "target_currency": target_currency,
            "exchange_rate": rate
        })
    else:
        return jsonify({"error": "Could not fetch exchange rate"}), 500

if __name__ == '__main__':
    app.run(debug=True)
