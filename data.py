from typing import List, Dict, Optional

class Pets:
        pets: List[Dict[str, any]] = [
            {"id": 1, "name": "Bolinha", "species": "Cachorro", "age": 5, "owner": "João"},
            {"id": 2, "name": "Miau", "species": "Gato", "age": 3, "owner": "Maria"},
            {"id": 3, "name": "Rex", "species": "Cachorro", "age": 2, "owner": "Carlos"},
            {"id": 4, "name": "Frajola", "species": "Gato", "age": 4, "owner": "Ana"}
        ]

        def get_all_pets(self):
            return self.pets

        def get_pet_by_id(self, pet_id):
            for pet in self.pets:
                if pet["id"] == pet_id:
                    return pet
            return {"Status": 404, "Mensagem": "Pet não encontrado"}

        def add_pets(self, pet):
            self.pets.append(pet.dict())
            return pet

