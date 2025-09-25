from flask import Flask, render_template, jsonify, request
import requests
import time, random

app = Flask(__name__)
COINGECKO_API = "https://api.coingecko.com/api/v3"

# Placeholder for Vanry/USDT
VANRY = {
    "id": "vanry-placeholder",
    "symbol": "vanry",
    "name": "Vanry",
    "current_price": 0.0123,
    "price_change_percentage_24h": 0.0,
    "image": "https://via.placeholder.com/32"
}

# Fallback coins if API fails
FALLBACK_COINS = [
    {
        "id": "bitcoin",
        "symbol": "btc",
        "name": "Bitcoin",
        "current_price": 30000,
        "price_change_percentage_24h": 0,
        "image": "https://assets.coingecko.com/coins/images/1/large/bitcoin.png"
    },
    {
        "id": "ethereum",
        "symbol": "eth",
        "name": "Ethereum",
        "current_price": 2000,
        "price_change_percentage_24h": 0,
        "image": "https://assets.coingecko.com/coins/images/279/large/ethereum.png"
    }
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/coins')
def get_coins():
    coins = []
    try:
        params = {
            'vs_currency': 'usd',   # must be usd, not usdt
            'order': 'market_cap_desc',
            'per_page': 250,        # get more results for filtering
            'page': 1,
            'sparkline': 'false'
        }
        res = requests.get(f"{COINGECKO_API}/coins/markets", params=params, timeout=10)
        res.raise_for_status()
        data = res.json()
        if isinstance(data, list):
            coins = [c for c in data if isinstance(c, dict)]
    except Exception as e:
        print("CoinGecko API error:", e)

    if not coins or len(coins) < 50:
        existing_ids = {c['id'] for c in coins}
        for fallback in FALLBACK_COINS:
            if fallback['id'] not in existing_ids:
                coins.append(fallback)

    coins = [VANRY] + coins
    return jsonify(coins)

# 🔎 New Search + Filter route
@app.route('/api/search')
def search_coins():
    query = request.args.get("q", "").lower()
    min_price = request.args.get("min_price", type=float)
    max_price = request.args.get("max_price", type=float)

    try:
        params = {
            'vs_currency': 'usd',
            'order': 'market_cap_desc',
            'per_page': 250,
            'page': 1,
            'sparkline': 'false'
        }
        res = requests.get(f"{COINGECKO_API}/coins/markets", params=params, timeout=10)
        res.raise_for_status()
        coins = res.json()
    except Exception as e:
        print("CoinGecko API error (search):", e)
        coins = FALLBACK_COINS

    # Apply search filter
    if query:
        coins = [c for c in coins if query in c["name"].lower() or query in c["symbol"].lower()]

    # Apply price filter
    if min_price is not None:
        coins = [c for c in coins if c.get("current_price", 0) >= min_price]
    if max_price is not None:
        coins = [c for c in coins if c.get("current_price", 0) <= max_price]

    return jsonify(coins)

@app.route('/api/coin/<coin_id>/chart')
def coin_chart(coin_id):
    days = int(request.args.get('days', 7))
    if coin_id == "vanry-placeholder":
        timestamps = [int(time.time() - i*86400)*1000 for i in reversed(range(days))]
        prices = [VANRY['current_price'] * (1 + random.uniform(-0.05,0.05)) for _ in range(days)]
        return jsonify({"prices": list(zip(timestamps, prices))})
    
    try:
        res = requests.get(f"{COINGECKO_API}/coins/{coin_id}/market_chart", params={
            'vs_currency': 'usd', 'days': days
        }, timeout=10)
        res.raise_for_status()
        return jsonify(res.json())
    except Exception as e:
        print("Coin chart API error:", e)
        timestamps = [int(time.time() - i*86400)*1000 for i in reversed(range(days))]
        prices = [30000 * (1 + random.uniform(-0.05,0.05)) for _ in range(days)]
        return jsonify({"prices": list(zip(timestamps, prices))})

if __name__ == '__main__':
    app.run(debug=True)
