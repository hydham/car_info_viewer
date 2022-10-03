from operator import mod
from optparse import Option
from urllib import response
from xmlrpc.client import Boolean
from fastapi import FastAPI, Query, Path, HTTPException, status, Body
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field
from typing import Dict, List, Optional
from database import cars

class Car(BaseModel):
    make: Optional[str]
    model: Optional[str]
    year: Optional[int] = Field(..., ge= 1997, lt= 2022)
    price: Optional[float]
    engine: Optional[str] = "v4"
    autonomous: Optional[bool]
    sold: Optional[List[str]]


app = FastAPI()

@app.get("/")
def root():
    return {"Hello to my first fastAPI ": "World"}

@app.get("/cars", response_model= List[Dict[str, Car]])
def get_cars(number: Optional[str] = Query(10, max_length=3)):
    response = []

    for id, car in list(cars.items()) [:int (number)]:
        to_add = {}
        to_add[id] = car
        response.append(to_add)

    return response

@app.get("/cars/{id}", response_model= Car)
def get_cars_by_id(id: int = Path(..., gt=0, lt = 1000)):

    car = cars.get(id)

    if not car:
        raise(HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= "no id to search"))

    return car

@app.post("/cars", status_code=status.HTTP_201_CREATED)
def add_cars(body_cars: List[Car], min_id: Optional[int] = Body(0)):
    if len(body_cars) < 1:
        raise(HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail= "No cars added"))

    min_id = len(cars.values()) + min_id #fixing the id for the car -> length of the cars dict + offset from the request body

    for car in body_cars:
        while cars.get(min_id): #checking the id selected is not returning car, if yes increment id by 1 and check until false
            min_id += 1
        cars[min_id] = car
        min_id += 1

@app.put("/cars/{id}",response_model=Dict[str,Car])
def update_car(id: int, car: Car = Body(...)):
    stored = cars.get(id)
    if not stored:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Could not find car with given ID.")
    stored = Car(**stored)
    new = car.dict(exclude_unset=True)
    new = stored.copy(update=new)
    cars[id] = jsonable_encoder(new)
    response = {}
    response[id] = cars[id]
    return response