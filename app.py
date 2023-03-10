from flask import Flask, render_template, url_for
import requests

app = Flask(__name__)

@app.route("/")
def index():
    api_key = ""
    url = f"https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=10&convert=USD"

    headers = {
        "Accepts": "application/json",
        "X-CMC_PRO_API_KEY": api_key
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        coins = []
        for coin in data["data"]:
            coins.append({
                "name": coin["name"],
                "symbol": coin["symbol"],
                "price": f"{coin['quote']['USD']['price']:.2f} USD"
            })
        return render_template("index.html", coins=coins)
    else:
        return f"Error al obtener datos: {response.status_code}"

if __name__ == "__main__":
    app.run(debuge=False, host='0.0.0.0')
