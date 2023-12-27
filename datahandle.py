from CMCAPI_talk import data
print("-------------------data received-------------------\n")

price_dict = {}
mkt_cap_dict = {}
daily_volume_dict = {}
nvt_dict = {}
total_supply_dict = {}

def crypto_coin(name:str):
    coin_dict = next((d for d in data['data'] if d['name'] == name), None)
    price = coin_dict['quote']['USD']['price']
    price_dict[name] = price
    mkt_cap = coin_dict['quote']['USD']['market_cap']
    mkt_cap_dict[name] = mkt_cap
    daily_volume = coin_dict['quote']['USD']['volume_24h']
    daily_volume_dict[name] = daily_volume
    total_supply = coin_dict['total_supply']
    total_supply_dict[name] = total_supply
    nvt = mkt_cap/daily_volume
    nvt_dict[name] = nvt
    # print("\n-------------------" + name + "-------------------\n")
    # print('price: ' + str(price))
    # print("Market cap: " + str(mkt_cap))
    # print("Daily vol: " + str(daily_volume))
    # print("NVT: " + str(nvt))
    # print("total_supply: " + str(total_supply))

# print the name of top 10 crypto coins in the list (coin positions are changing)
# for i in range(10):
#     print(data["data"][i]['name'])

#BTC quote (name: Bitcoin)
crypto_coin("Bitcoin")

#ETH (name: Ethereum)
crypto_coin("Ethereum")

#Solana (name: Solana)
crypto_coin("Solana")

#Cardano (name: Cardano)
crypto_coin("Cardano")

#Avalanche (name: Avalanche)
crypto_coin("Avalanche")
