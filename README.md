# Vanry/USDT Crypto Flask App

This is a Flask single-page app that shows cryptocurrency prices using CoinGecko API.  
Vanry/USDT pair is prioritized at the top.

## Features
- Homepage with coins, prices, % change
- Vanry/USDT shown first
- Clicking a coin shows chart (7 days history)
- Search + filter
- Dark/light mode toggle
- TailwindCSS + Chart.js UI

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## Deploy on Vercel
- Add `app.py` as entrypoint
- Use Python runtime (Vercel supports Flask via `vercel-python`)
- Or deploy on Render/Heroku easily

