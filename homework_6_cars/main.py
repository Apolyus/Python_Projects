import uuid
import json
import csv
import shutil
import os


OUTPUT_DIR = "output_data"


def clean_directory():
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)
    os.makedirs(OUTPUT_DIR)


def write_in_json(file_name_input, file_name_output):
    with open(file_name_input, "w") as file:
        json.dump(file_name_output, file, indent=2)


def read_from_csv():

    with open("input.csv") as file:
        csv_dict = csv.DictReader(file)
        data = {
            str(uuid.uuid4()): car for car in csv_dict
        }
        return data


def data_management(cars:list):
    sort_by_price1 = [price for price in cars if cars["price"] < 1000]
    print(sort_by_price1)
    sort_by_price2 = [price for price in cars if 1000 < cars["price"] < 5000]
    print(sort_by_price2)
    sort_by_price3 = [price for price in cars if cars["price"] > 5000]
    print(sort_by_price3)
    sort_by_hp1 = [hp for hp in cars if cars["hp"] < 120]
    print(sort_by_hp1)
    sort_by_hp2 = [hp for hp in cars if 120 < cars["hp"] < 180]
    print(sort_by_hp2)
    sort_by_hp3 = [hp for hp in cars if 120 < cars["hp"] < 180]
    print(sort_by_hp3)

if __name__ == '__main__':
    clean_directory()
    cars = read_from_csv()
    print("cars", cars)
    data_management(cars)

    # cars_key = ["id", "brand", "model", "horse power", "price"]
    #
    # cars_main_list = [
    #     [1, "Bentley", "Continental", 110, 6500],
    #     [2, "Audi", "A8", 170, 4500],
    #     [3, "Dacia", "Solenza", 100, 900],
    #     [4, "BMW", "E46", 105, 900],
    #     [5, "Opel", "Corsa", 130, 4000],
    #     [6, "Toyota", "Supra", 190, 6000],
    #     [8, "Dacia", "Duster", 120, 950]
    # ]
    #
    # last_car_list = [
    #     {key: value for key, value in zip(cars_key, car)}
    #     for car in cars_main_list
    # ]
    #
    # sort_by_price1 = [price for price in last_car_list if price.get("price", 0) < 1000]
    # print(sort_by_price1)
    # sort_by_price2 = [price for price in last_car_list if 1000 < price.get("price", 0) < 5000]
    # print(sort_by_price2)
    # sort_by_price3 = [price for price in last_car_list if price.get("price", 0) > 5000]
    # print(sort_by_price3)
    #
    # sort_by_hp1 = [hp for hp in last_car_list if hp.get("horse power", 0) < 120]
    # print(sort_by_hp1)
    # sort_by_hp2 = [hp for hp in last_car_list if 120 < hp.get("horse power", 0) < 180]
    # print(sort_by_hp2)
    # sort_by_hp3 = [hp for hp in last_car_list if 120 < hp.get("horse power", 0) < 180]
    # print(sort_by_hp3)
    #
    # map_my_cars = {brand: [car for car in last_car_list if car['brand'] == brand] for brand in
    #                set(car['brand'] for car in last_car_list)
    #                }
    # matching_cars = [car for car in last_car_list if car['brand'] == 'Dacia']
    #
    # with open("cheap_cars.json", "w") as file:
    #     json.dump(sort_by_price1, file, indent=2)
    #
    # with open("medium_cars.json", "w") as file:
    #     json.dump(sort_by_price2, file, indent=2)
    #
    # with open("expensive_cars.json", "w") as file:
    #     json.dump(sort_by_price3, file, indent=2)
    #
    # with open("slow_cars.json", "w") as file:
    #     json.dump(sort_by_hp1, file, indent=2)
    #
    # with open("fast_cars.json", "w") as file:
    #     json.dump(sort_by_hp2, file, indent=2)
    #
    # with open("sport_cars.json", "w") as file:
    #     json.dump(sort_by_hp3, file, indent=2)
    #
    # with open("Dacia.json", "w") as file:
    #     json.dump(matching_cars, file, indent=2)
    # a = "Dacia123.json"
    # b = matching_cars
    # write_in_json(a, b)
    #
