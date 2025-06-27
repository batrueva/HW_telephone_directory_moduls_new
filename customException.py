class InvalidInputUser(Exception):
    pass
    # def __init__(self, message):
    #     self.message = message
    #     super().__init__(self.message)


class InvalidDictData(Exception):
    pass


class InvalidChoiceMenu(InvalidInputUser):
    pass


class InvalidContactData(InvalidInputUser):
    pass
