import requests, json

res = requests.get("https://api.coingecko.com/api/v3/simple/price?ids=bitcoin,ethereum,solana&vs_currencies=usd")
res.raise_for_status()

res_data = json.loads(res.text)

print("=== CRYPTO PRICE TRACKER ===")
for k, v in res_data.items():
    print(f"{k.upper()}: ${v["usd"]}")
print("============================")