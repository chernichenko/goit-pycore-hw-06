from models.name import Name
from models.phone import Phone

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        phone = Phone(number)
        if phone.validate():
            self.phones.append(phone)
        else:
            print(f"Invalid phone number: {number}")

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                self.phones.remove(phone)
                return
        print(f"Phone number {number} not found for {self.name}")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.value == old_number:
                phone.value = new_number
                return
        print(f"Phone number {old_number} not found for {self.name}")

    def find_phone(self, number):
        for phone in self.phones:
            if phone.value == number:
                return phone
        print(f"Phone number {number} not found for {self.name}")

    def __str__(self):
        return f"Contact name: {self.name}, phones: {', '.join(str(phone) for phone in self.phones)}"