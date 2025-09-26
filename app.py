from flask import Flask, jsonify, render_template, request
import requests
import os
from openai import OpenAI

app = Flask(__name__)


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

COINGECKO_API = "https://api.coingecko.com/api/v3"


# ---------- ROUTES ----------

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/coins")
def get_coins():
    url = f"{COINGECKO_API}/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "per_page": 50,
        "page": 1,
        "sparkline": "false"
    }
    response = requests.get(url, params=params)
    return jsonify(response.json())

@app.route("/api/coin/<coin_id>/chart")
def get_coin_chart(coin_id):
    days = request.args.get("days", 30)
    url = f"{COINGECKO_API}/coins/{coin_id}/market_chart"
    params = {"vs_currency": "usd", "days": days}
    response = requests.get(url, params=params)
    return jsonify(response.json())

@app.route("/api/opinion/<coin_id>")
def get_coin_opinion(coin_id):
    """Generate automatic investment opinion using OpenAI"""
    try:
        # Fetch coin data first
        url = f"{COINGECKO_API}/coins/markets"
        params = {"vs_currency": "usd", "ids": coin_id}
        response = requests.get(url, params=params)
        data = response.json()[0]

        # Build prompt
        prompt = f"""
        You are a crypto market analyst. Based on the following data, give a short investment opinion
        (bullish, bearish, or neutral) with reasoning.

        Coin: {data['name']} ({data['symbol'].upper()})
        Current Price: ${data['current_price']}
        24h Change: {data['price_change_percentage_24h']}%
        Market Cap: ${data['market_cap']}
        24h Volume: ${data['total_volume']}
        """

        # Call OpenAI
        completion = client.chat.completions.create(
            model="gpt-4o-mini",  # Or "gpt-3.5-turbo"
            messages=[
                {"role": "system", "content": "You are a financial assistant for crypto insights."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=150,
            temperature=0.7
        )

        opinion = completion.choices[0].message.content.strip()

        return jsonify({"coin": data['name'], "opinion": opinion})

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
