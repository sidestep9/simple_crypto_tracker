import requests, time, json

while True:
    res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd")
    res.raise_for_status()

    res_data = res.json()

    with open("price_data.json", "r", encoding="utf-8") as file:
        prev_data = json.load(file)
    
    print(prev_data)
    
    with open("price_data.json", "w") as file:
        json.dump(res_data, file)

    print("\n=== CRYPTO PRICE TRACKER ===")
    for k, v in res_data.items():
        print(f"{k.upper()}: ${v["usd"]}")
    print("============================")
    time.sleep(30)