from file_repository import FileRepository
from address_utils import AddressUtils
import json

class AddressContactRepository(FileRepository):
    utils = AddressUtils
    address_contact = None

    def __init__(self) -> None:
        super().__init__("address-details.json")

    def get_address_contacts(self):
        if self.address_contact == None:
            self.address_contact = json.loads(super().readFile())
        return self.address_contact
        

    def add_new_address_contacts(self,address_entry):
        address_entry["id"] = self.utils.generateId()
        self.get_address_contacts()["details"].append(address_entry)
        self.save()

    def update_address_contact(self,address_entry):
        
        #    ---- OLD CODE (WORKS LOCAL, BUT NOT ON WEB SERVICE) ----
        # result = list(filter(lambda entry : entry.get("id") == address_entry["id"], self.get_address_contacts()["details"] ))
        # result[0] = address_entry

        #    ---- NEW CODE (WORKS LOCAL, BUT NOT ON WEB SERVICE) ----
        ctr = 0
        for items in self.get_address_contacts()['details']:
            if items['id'] == address_entry['id']:
                break
            ctr +=1
        self.get_address_contacts()['details'][ctr] = address_entry
        self.save()

    def delete_address_contact(self,address_entry):
        index = 0
        for entry in self.get_address_contacts()["details"]:
            if entry.get("id") == address_entry.get("id"):
                break
            index = index + 1
        self.get_address_contacts()["details"].pop(index)
        self.save()

    def save(self):
        super().writeFile(json.dumps(self.address_contact))


    def find_address_contact(self, name):
        stringComparer = lambda a,b : (a.lower().find(b) > -1 or b == "")

        result = filter(lambda entry : stringComparer(entry.get("name", ""),name), self.get_address_contacts()["details"] )

        return list(result)