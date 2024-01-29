class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"

    def to_dict(self):
        return {
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

    @classmethod
    def from_dict(cls, contact_dict):
        return cls(
            name=contact_dict['name'],
            phone=contact_dict['phone'],
            email=contact_dict['email']
        )
