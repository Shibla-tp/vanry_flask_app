# 🚀 AI-Powered Crypto Dashboard

A single-page web app that displays real-time cryptocurrency prices, interactive charts, and AI-powered investment analysis.  
Built with **Flask**, **CoinGecko API**, and **OpenAI GPT**.

---

## ✨ Features

- 📊 Real-time cryptocurrency prices (CoinGecko API)
- 🔍 Sor, Search & filter coins (by name, price range, percentage change)
- 📈 Interactive chart view for selected coins
- 🤖 AI-powered investment insights (OpenAI)
- 🌙 Dark & light mode toggle
- ☁️ Hosted on PythonAnywhere with GitHub integration

---

## 📸 Screenshots

### 🔲 Dark Mode
![alt text](image.png)
![Dark Mode](./assets/screenshot-dark.jpg)

### ⬜ Light Mode
![Light Mode](./assets/screenshot-light.jpg)

### 🔍 Search & Filter
Example: Searching for **Bitcoin** with price range `40 - 1000`
![Search & Filter](./assets/screenshot-search-filter.jpg)

### 🔍 Sort Column
Example: Sorting coin column (or any other column)
![Search & Filter](./assets/screenshot-sort-coin.jpg)


### 📈 Price Chart
Interactive chart view for selected coin (7D/30D/90D trends)
![Price Chart](./assets/screenshot-chart.jpg)

### 🤖 AI Investment Opinion
Example AI-powered analysis for Bitcoin Cash (BCH)- Neutral
![AI Opinion](./assets/screenshot-neutral-opinion.jpg)

Example AI-powered analysis for Bitcoin Cash (BCH) - Bullish
![AI Opinion](./assets/screenshot-bullish-opinion.jpg)

---

## ⚙️ Installation

1. Clone the repo  
   ```bash
   git clone https://github.com/your-username/crypto-dashboard.git
   cd crypto-dashboard
   ```

2. Create virtual environment  
   ```bash
   python -m venv venv
   source venv/bin/activate   # (Linux/Mac)
   venv\Scripts\activate    # (Windows)
   ```

3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```

4. Add `.env` file with your API keys  
   ```env
   OPENAI_API_KEY=your_openai_key
   COINGECKO_API=https://api.coingecko.com/api/v3
   ```

5. Run the app  
   ```bash
   flask run
   ```

6. Visit http://127.0.0.1:5000 in your browser 🎉

---

## 📂 Project Structure

```
crypto-dashboard/
│── app.py               # Flask backend
│── static/              # JS, CSS
│── templates/           # HTML templates
│── assets/              # Screenshots for README
│── requirements.txt     # Python dependencies
│── .env                 # API keys (ignored in Git)
│── README.md            # Documentation
```

---

## 🤝 Contributions

Pull requests are welcome! For major changes, please open an issue first to discuss.  

---
