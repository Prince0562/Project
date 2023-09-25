import pyttsx3
engine = pyttsx3.init()
engine.say("Welcome to Prince Ticket Booking project , Kindly Choose an option")
engine.runAndWait()
engine.stop()

class BusInfo():
    
    def __init__(self, Name , Bus_number, fare , destination , seats ):
        self.Name = Name
        self.num = Bus_number
        self.Fare = fare
        self.Destination = destination
        self.seats = seats
    
    def busname(self):
        print("The name of the Bus is :", self.Name)
        # engine.say(f"The name of the Bus is : {self.Name}")
        # engine.runAndWait()

    def bus_No(self):
        print("The number of the bus is : ", self.num)

    def fair(self):
        print("The fare of the Bus is :", self.Fare)

    def destination(self):
        print(self.Destination ,"  is the destination of the Bus")

    def availableseats(self):
        print("Available seats in this bus ", self.seats)

    def Bookticket(self):
        if self.seats > 0:
            self.seats = self.seats-1
            print("Your ticket has been booked: Kindly check your mailbox")
        
        else:
            print("There is no avaialable seats in this bus")
 
    def Cancelled_Ticket(self):
        print("Your ticket has been cancelled")
        self.seats = self.seats + 1

Service = BusInfo("Hulchul" , 55 , 2222 , "Kedarnath" , 5)
        


while True:
    print("\n")
    WelcomeMsg = '''***Welcome to Prince Ticket Booking Project***
    Please choose one option from the given list:
          ******************
    Press 1 to Know the name of the Bus:
    Press 2 to Check the Bus No.:
    Press 3 to Check the fair of the Bus:
    Press 4 to Check the Destination of the Bus:
    Press 5 to Check the Seat avaialability of the Bus:
    Press 6 to Book the ticket of the Bus:
    Press 7 to Know the destination of the Bus:
    Press 8 to Cancelled the Ticket:
    Press 9 to exit the program:
    '''
    print(WelcomeMsg)
    # engine.say(WelcomeMsg)  
    # engine.runAndWait()
    # engine.stop()
    
    a = int(input("Enter your choice: "))   
    
    if  a==1:
        Service.busname()
    
    elif a==2:
        Service.bus_No()
    
    elif a==3:
        Service.fair()
    
    elif a==4:
        Service.destination()
    
    elif a==5:
        Service.availableseats()

    elif a ==6:
        Service.Bookticket()

    elif a==7:
        Service.destination()
       
    elif a ==8:
        Service.Cancelled_Ticket()
        
    
    elif a ==9:
        print("Thank you for choosing Prince Ticket booking Project")
        engine.say("Thank you for choosing Prince Ticket booking Project")
        engine.runAndWait()
        engine.stop()
        exit()
    
    else:
        print("Invalid choice")

    

