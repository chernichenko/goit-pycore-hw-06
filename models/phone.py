from models.field import Field

class Phone(Field):
    def __init__(self, value):
        super().__init__(value)

    def validate(self):
        # Валідація номера телефону (приклад)
        if len(self.value) == 10 and self.value.isdigit():
            return True
        else:
            return False

    def __str__(self):
        return str(self.value)