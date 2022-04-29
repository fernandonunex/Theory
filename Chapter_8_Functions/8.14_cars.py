def make_car(manufacturer, model, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model
    return car_info


def run():
    car = make_car("Chevrolet", "Silverado",
                   year=2022, color='black',
                   seats=5)
    print(car)

    car_2 = make_car('subaru', 'outback', color='blue', tow_package=True)
    print(car_2)


if __name__ == "__main__":
    run()
