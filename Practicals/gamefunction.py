class CharacterError (Exception):
    def __int__(self, message):
        self.message = message

class MismatchError (Exception):
    def __int__(self, message):
        self.message = message

def game(e,h):
    if len(e) != len(h):
        raise MismatchError
    else:
        for i in range(len(e)):
            try:
                e[i] = int(e[i])
                h[i] = int(h[i])
            except ValueError:
                raise CharacterError
    en = sorted(e, reverse=True)
    he = sorted(h, reverse=True)
    for i in range(len(en)):
        if en[i] >= he[i]:
            return "LOSE"
    return "WIN"
