import requests, time

while True:
    res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd")
    res.raise_for_status()

    res_data = res.json()

    print("\n=== CRYPTO PRICE TRACKER ===")
    for k, v in res_data.items():
        with open("price_history.txt", "a") as file:
            file.write(f"{k.upper()}: ${v["usd"]}")
            file.write(" | ")

        print(f"{k.upper()}: ${v["usd"]}")
    print("============================")
    with open("price_history.txt", "a") as file:
            file.write("\n")
    time.sleep(30)