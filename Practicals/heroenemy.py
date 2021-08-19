from errors import CharacterError,MismatchError

class heroenemy:
    en=[]
    st=[]

    def __init__(self,ene,stn):
        self.en=ene
        self.st=stn

    def split(self,s1,s2):
        return s1.split(" "),s2.split(" ")

    def game(self,e,h):
        if len(e) != len(h):
            raise MismatchError
        else:
            for i in range(len(e)):
                try:
                    e[i] = int(e[i])
                    h[i] = int(h[i])
                except ValueError:
                    raise CharacterError
        en=sorted(e,reverse=True)
        he=sorted(h,reverse=True)
        for i in range(len(en)):
            if en[i] >= he[i]:
                return "LOSE"
        return "WIN"