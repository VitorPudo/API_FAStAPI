from fastapi import FastAPI, HTTPException
from typing import List
from data import Pets
from schema import PetsSchema

app = FastAPI()
lista_de_pets = Pets()

@app.get("/pets", response_model=list[PetsSchema])
def get_all_pets():
    return lista_de_pets.get_all_pets()


@app.get("/pets/{pet_id}", response_model=PetsSchema)
def get_pet_by_id(pet_id: int):
    return lista_de_pets.get_pet_by_id(pet_id)

@app.post("/pets", response_model=PetsSchema)
def add_pets(pet: PetsSchema):    
   return lista_de_pets.add_pets(pet)
    