from collections import UserDict

class AddressBook(UserDict):
    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name):
        return self.data.get(name, None)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
        else:
            print(f"Record with name '{name}' not found.")

    def __str__(self):
        return "\n".join(str(record) for record in self.data.values())