from http_repository import HttpRepository
from address_utils import AddressUtils
import json

class AddressClientApi(HttpRepository):
    utils = AddressUtils
    address_contact = None
    
    def __init__(self)->None:
        super().__init__("http://localhost:8000/api/address")
    
    def get_address_contacts(self):
        self.address_contact = json.loads(super().do_get("/get-address"))
        return self.address_contact
    
    def add_new_address_contacts(self, address_entry):
        request = {"new_entry": json.dumps(address_entry)}
        return super().do_post("/add-address", request)
    
    def update_address_contact(self,address_entry):
        request = {"new_entry": json.dumps(address_entry)}
        return super().do_put("/update-address",request)

    def find_address_contact(self, name):
        stringComparer = lambda a,b : (a.lower().find(b) > -1 or b == "")
        result = filter(lambda entry : stringComparer(entry.get("name", ""),name), self.get_address_contacts()["details"] )
        return list(result)

    def delete_address_contact(self,entry_to_delete):
        request = { "entry_to_delete": json.dumps(entry_to_delete)}
        return super().do_delete("/delete-address", request)