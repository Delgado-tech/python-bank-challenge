class Address:
    street: str
    number: str
    neighborhood: str
    city: str
    state: str

    def __init__(self, *, street: str, number: str, neighborhood: str, city: str, state: str) -> None:
        self.street = street
        self.number = number
        self.neighborhood = neighborhood
        self.city = city
        self.state = state

    def toString(self) -> str:
        return f"{self.street}, {self.number} - {self.neighborhood} - {self.city}/{self.state}"