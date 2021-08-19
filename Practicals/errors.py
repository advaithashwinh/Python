class CharacterError (Exception):
    def __int__(self, message):
        self.message = message

class MismatchError (Exception):
    def __int__(self, message):
        self.message = message