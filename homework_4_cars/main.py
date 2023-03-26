if __name__ == '__main__':
    #
    cars_key = ["id", "brand", "model", "horse power", "price"]

    cars_main_list = [
        [1, "Bentley", "Continental", 110, 6500],
        [2, "Audi", "A8", 170, 4500],
        [3, "Dacia", "Solenza", 100, 900],
        [4, "BMW", "E46", 105, 900],
        [5, "Opel", "Corsa", 130, 4000],
        [6, "Toyota", "Supra", 190, 6000]

    ]

    last_car_list = [
        {key: value for key, value in zip(cars_key, car)}
        for car in cars_main_list
    ]

    sort_by_price1 = [price for price in last_car_list if price.get("price", 0) < 1000]
    print(sort_by_price1)
    sort_by_price2 = [price for price in last_car_list if 1000 < price.get("price", 0) < 5000]
    print(sort_by_price2)
    sort_by_price3 = [price for price in last_car_list if price.get("price", 0) > 5000]
    print(sort_by_price3)

    sort_by_hp1 = [hp for hp in last_car_list if hp.get("horse power", 0) < 120]
    print(sort_by_hp1)
    sort_by_hp2 = [hp for hp in last_car_list if 120 < hp.get("horse power", 0) < 180]
    print(sort_by_hp2)
    sort_by_hp3 = [hp for hp in last_car_list if 120 < hp.get("horse power", 0) < 180]
    print(sort_by_hp3)

