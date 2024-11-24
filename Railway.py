class RailwayReservationSystem:
    def __init__(self):
        self.ct=[]
        self.rac=[]
        self.wl=[]
        self.tc=2
        self.trac=2
        self.twl=2
    def bookTickets(self):
        name=input("Enter Your Name:")
        age=int(input("Enter Your Age:"))
        gender=input("Enter Your Gender:")
        berth=input("Enter Your Berth Preference:")

        if len(self.ct)<self.tc:
            if age > 60 or (gender.lower() == "female" and age<=60 and  berth.lower() == "lower"):
                berth = "Lower"
            else:
                berth=berth.capitalize()

            self.ct.append({"Name":name,"Age":age,"Gender":gender,"Berth":berth})
            print("Ticket Booked Successfully for",name)

        elif len(self.rac)<self.trac:
            self.rac.append({"Name":name,"Age":age,"Gender":gender,"Berth":berth})
            print("Added to RAC list for",name)
        elif len(self.wl)<self.twl:
            self.wl.append({"Name":name,"Age":age,"Gender":gender,"Berth":berth})
            print("Added to waiting list for",name)
        else:
            print("Ticket Not Available")

    def cancelTickets(self):
        #confirmed
        name=input("Enter Your Name:")
        for i in self.ct:
            if i["Name"] == name:
                self.ct.remove(i)
                print("Ticket was Cancelled Successfully for",name)
                self.r_a_c()
                self.w_l()
                return

        #RAC
        for j in self.rac:
            if j["Name"] == name:
                self.ct.remove(j)
                print("RAC was Cancelled Successfully for",name)
                self.w_l()
                return

        #WL
        for k in self.rwl:
            if k["Name"] == name:
                self.ct.remove(k)
                print("Waiting list ticket was Cancelled Successfully for",name)
                return
        

    def r_a_c(self):
        if self.rac:
                m=self.rac.pop(0)
                m["Berth"]="Lower"
                self.ct.append(m)
                print("RAC ticket confirmed for",m["Name"])
    def w_l(self):
        if self.wl:
            m=self.wl.pop(0)
            m["Berth"]="Side Lower"
            self.rac.append(m)
            print("Waiting list ticket moved to RAC for",m["Name"])
                

    def printBookedTickets(self):
        for i in self.ct:
            print(i)

    def printAvailableTickets(self):
        print("Available Confirmed Tickets:",self.tc-len(self.ct))
        print("Available RAC Tickets:",self.trac-len(self.rac))
        print("Available Waiting List Tickets:",self.twl-len(self.wl))
            


r=RailwayReservationSystem()
while True:
    opt=int(input("Welcome to Railway Reservation System\n1.Book Tickets\n2.Cancel Tickets\n3.Print Booked Tickets\n4.Print Available Tickets\n5.Exit\n"))
    match opt:
        case 1: r.bookTickets()
        case 2:r.cancelTickets()
        case 3:r.printBookedTickets()
        case 4:r.printAvailableTickets()
        case 5:print("Thank You") ;break
        case _:print("Invalid Option")
