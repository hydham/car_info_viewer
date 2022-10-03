cars = {
    1: {
        "make": "CarBrand",
        "model": "Fast",
        "year": 1998,
        "price": 25000.0,
        "engine": "V8",
        "autonomous": False,
        "sold": ["NA","EU"]
    },

    2: {
        "make": "Speedy",
        "model": "FourWheeler SUV",
        "year": 2021,
        "price": 55400.0,
        "engine": "V4",
        "autonomous": False,
        "sold": ["AF","AN","AS","EU","NA","OC","SA"]
    },

    3: {
        "make": "Elektrik",
        "model": "AutoCar",
        "year": 2019,
        "price": 45000.0,
        "engine": "V8",
        "autonomous": True,
        "sold": ["AS"]
    },

    4: {
        "make": "CarBrand",
        "model": "Beetle",
        "year": 2004,
        "price": 21299.99,
        "engine": "V4",
        "autonomous": False,
        "sold": []
    },

    5: {
        "make": "CarPro",
        "model": "Supersonic",
        "year": 2015,
        "price": 215000.0,
        "engine": "V12",
        "autonomous": False,
        "sold": ["NA","AF","OC","SA"]
    }
}

# convert dict into a list and store in variable
# for id, cars in list(cars.items()) [:2]:
#     to_add = {}
#     to_add[id] = cars
#     print(to_add)


# car_id = 2
# response = {}

# if car_id in cars:
#     response[car_id] = cars[car_id]
    
# print(response)

# d = {"a":2, "b":3}

# def foo(a,b):
#     print(a, b)

# f = {**d, "c":3}
# print (f)

# stored = cars.get(1)
# stored = Car(**stored)

# new = cars.get(5)
# new = Car(**new)

# new_dict = new.dict(exclude_unset=T)

# updated = stored.copy(update = new_dict)

# cars[1] = jsonable_encoder(updated)

# Response = {}
# Response[1] = cars[1]