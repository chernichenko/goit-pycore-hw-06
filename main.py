from models.record import Record
from models.address_book import AddressBook

if __name__ == "__main__":
    book = AddressBook()

    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    book.add_record(john_record)

    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    print("All records in the address book:")
    print(book)

    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print("\nAfter editing John's phone number:")
    print(john)

    found_phone = john.find_phone("5555555555")
    print(f"\nPhone number found for John: {found_phone}")

    book.delete("Jane")

    print("\nAfter deleting Jane's record:")
    print(book)
