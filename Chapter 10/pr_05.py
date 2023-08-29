




class Train : 

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("XXXXXXXXXXXXXX")
        print(f"The Name of the Train is :- {self.name}")
        print(f"The Seats avalible in the Train are :- {self.seats}")
        print("XXXXXXXXXXXXXX")

    def getfare(self):
        print(f"The Price of the Train ticket is :- {self.fare}")    

    
    def seatInfo(self):
        if(self.seats > 0):
            print(f"Seat is Booked. Your Seat no. is {self.seats}")
            self.seats = self.seats - 1
        else:
            print(f"Sorry ! The seat is not avalible.")     

t1 = Train("Rajdhani Exp. : 14253", 453, 1)
  
t1.getStatus()
t1.getfare()
t1.seatInfo()
t1.seatInfo()
