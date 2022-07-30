from fastapi import FastAPI
from address_contact_repository import AddressContactRepository
import json

app = FastAPI()
addressContactRepository = AddressContactRepository()

@app.get("/api/address/get-address")
def get_address():
    return addressContactRepository.get_address_contacts()


@app.post("/api/address/add-address")
def add_address(new_entry):
    addressContactRepository.add_new_address_contacts(json.loads(new_entry))
    return json.dumps({
        "code" : 200,
        "message" : "Successfully added!"
    })

@app.put("/api/address/update-address")
def update_address(new_entry):
    contacts = addressContactRepository.update_address_contact(json.loads(new_entry))
    return json.dumps({"code":200, "message":"Successfully updated"})

@app.delete("/api/address/delete-address")
def delete_address(entry_to_delete):
    addressContactRepository.delete_address_contact(json.loads(entry_to_delete))
    return json.dumps({"code":200, "message":"Successfully updated"})
