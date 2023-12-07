from CoinMarketCapTest import data
print("-------------------data received-------------------\n")

price_dict = {}
mkt_cap_dict = {}
daily_volume_dict = {}
nvt_dict = {}
total_supply_dict = {}

def crypto_coin(pos):
    price = pos['quote']['USD']['price']
    price_dict[pos['name']] = price
    mkt_cap = pos['quote']['USD']['market_cap']
    mkt_cap_dict[pos['name']] = mkt_cap
    daily_volume = pos['quote']['USD']['volume_24h']
    daily_volume_dict[pos['name']] = daily_volume
    total_supply = pos['total_supply']
    total_supply_dict[pos['name']] = total_supply
    nvt = mkt_cap/daily_volume
    nvt_dict[pos['name']] = nvt
    # print("\n-------------------" + pos['name'] + "-------------------\n")
    # print('price: ' + str(price))
    # print("Market cap: " + str(mkt_cap))
    # print("Daily vol: " + str(daily_volume))
    # print("NVT: " + str(nvt))
    # print("total_supply: " + str(total_supply))


#BTC quote
#print(data["data"][0])
crypto_coin(data['data'][0])

#ETH
#print(data["data"][1])
crypto_coin(data['data'][1])

#Solana
#print(data["data"][5])
crypto_coin(data['data'][5])

#Cardano
#print(data["data"][7])
crypto_coin(data['data'][7])

#Avalanche
#print(data["data"][9])
crypto_coin(data['data'][9])

