from datahandle import price_dict, mkt_cap_dict, daily_volume_dict, nvt_dict, total_supply_dict


def fair_price(coin_name:str):
    try:
        daily_volume_coin = daily_volume_dict[coin_name]
        total_supply_coin = total_supply_dict[coin_name]

        # calculating average nvt in the nvt_dict
        nvt_sum = 0

        for k, v in nvt_dict.items():
            nvt_sum += v

        nvt_avg = nvt_sum/len(nvt_dict)
            
        # calculating fair price
        fair_mkt_cap = daily_volume_coin * nvt_avg
        fair_price = fair_mkt_cap/total_supply_coin

        return fair_price
    except NameError:
        print("coin_name input is not correct")


print("current BTC price: ", price_dict["Bitcoin"])
print("BTC fair price: ", fair_price("Bitcoin"))
print("current ETH price: ", price_dict["Ethereum"])
print("ETH fair price: ", fair_price("Ethereum"))
