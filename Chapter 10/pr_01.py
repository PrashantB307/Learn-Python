



class Programmer:
    company = "Microsoft"
    def __init__(self, name, product):
        self.name = name
        self.product = product

    def getDetails(self):
        print(f"Programmer Name is {self.name} and Product is {self.product}")



P1 = Programmer("Pawan", "Skype")
P2 = Programmer("Bhardwaj", "Github")

P1.getDetails()
# ====> Programmer Name is Pawan and Product is Skype

P2.getDetails()       
# ====> Programmer Name is Bhardwaj and Product is Github