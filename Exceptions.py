class InvalidInput(Exception):
    def __init__(self, salary: str, message="Invalid data entry!"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


class InvalidIndex(Exception):
    def __init__(self, salary: int, message="Invalid index for brick!"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)
