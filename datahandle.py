from os import close
from CMCAPI_talk import latest_data
from CMCAPI_talk import hist_data
from datetime import date, timedelta
print("-------------------data received-------------------\n")
print(hist_data)

#--------------------------------------------this section gets historical data--------------------------------------------
today = date.today()
date_list = []

for i in range(5):
    day = today - timedelta(days = i)
    day_str = day.strftime("%Y-%m-%d")
    date_list.append(day_str)

print('date_list' , date_list)
volume_48hr = {}
volume_5days = {}


# function calculating 48 hr average volume with coin's daily_volume list as uinput
def avg_48hr_vol_calc(list, expected_size = 5):
    if len(list) != expected_size:
        raise ValueError(f"List must be exactly {expected_size} elements long")
    
    first_weight = 1.5  # weight of today's volume
    second_weight = 2 - first_weight    # weight of yesterday's volume
    avg_48hr_vol = (first_weight * list[0] + second_weight * list[1])/2 # calculate 48 hr average volume
    return avg_48hr_vol


# function calculating 5 days average volume with coin's daily_volume list as uinput
def avg_5days_vol_calc(list, expected_size = 5):
    if len(list) != expected_size:
        raise ValueError(f"List must be exactly {expected_size} elements long")
    
    first_weight = 2  # weight of today's volume
    second_weight = 1.2    # weight of yesterday's volume
    third_weight = 1
    fourth_weight = 0.5
    fifth_weight = 5 - first_weight - second_weight - third_weight - fourth_weight
    avg_5days_vol = (first_weight * list[0] + second_weight * list[1] + third_weight * list[2] + 
                    fourth_weight * list[3] + fifth_weight * list[4])/5 # calculate 48 hr average volume
    return avg_5days_vol


def hist_crypto_vol(name:str):
    coin_dict = next((d for d in hist_data if d['Meta Data']['3. Digital Currency Name'] == name), None)
    daily_volume = []
    # daily_volume[0] is today's volume
    for date in date_list:
        daily_volume.append(float(coin_dict["Time Series (Digital Currency Daily)"][date]['5. volume']))

    print(f'{name} daily_volume:' , daily_volume)

    volume_48hr[name] = avg_48hr_vol_calc(daily_volume)
    volume_5days[name] = avg_5days_vol_calc(daily_volume)

#--------------------------------------------this section gets latest listing data--------------------------------------------
price_dict = {}
mkt_cap_dict = {}
daily_volume_dict = {}
nvt_dict = {}
total_supply_dict = {}

def crypto_coin(name:str):
    coin_dict = next((d for d in latest_data['data'] if d['name'] == name), None)
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
#     print(latest_data["data"][i]['name'])

#BTC quote (name: Bitcoin)
# crypto_coin("Bitcoin")
hist_crypto_vol('Bitcoin')

#ETH (name: Ethereum)
# crypto_coin("Ethereum")
hist_crypto_vol('Ethereum')

#Solana (name: Solana)
# crypto_coin("Solana")
hist_crypto_vol('Solana')

#Cardano (name: Cardano)
# crypto_coin("Cardano")
# hist_crypto_vol('Cardano')

#Avalanche (name: Avalanche)
# crypto_coin("Avalanche")
# hist_crypto_vol('Avalanche')

print('48 hrs volume:' , volume_48hr)
print('5 days volume:' , volume_5days)