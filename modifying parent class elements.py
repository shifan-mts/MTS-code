class mts:
    def __init__(self):
        self.shif = "Founder"
        self.subu = "cofounder"
        self.nithesh = "cofounder"
class mts_public(mts):
    def _init__(self):
        super().__init__() # super() is used for modifying the variable of parents class self attribute poda theva illa
        self.shif = "admin"
s=mts_public()
print(s.shif)       