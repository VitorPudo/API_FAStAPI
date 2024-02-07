from fastapi.testclient import TestClient
from main import app  # Substitua 'main' pelo nome do arquivo principal do seu aplicativo

client = TestClient(app)

def test_get_all_pets():
    response = client.get("/pets")
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_get_pet_by_id():
    response = client.get("/pets/1")  # Supondo que o pet com ID 1 exista
    assert response.status_code == 200
    assert response.json()["id"] == 1  # Supondo que o JSON retornado tenha um campo 'id'

def test_add_pets():
    new_pet_data = {"id": 9, "name": "NewPet", "species": "Dog", "age": 2, "owner": "Dono"}  # Supondo dados válidos para um novo pet
    response = client.post("/pets", json=new_pet_data)
    assert response.status_code == 200
    assert response.json()["name"] == new_pet_data["name"]

# Você pode adicionar mais testes conforme necessário
