class Garage:
    
    def solution(self):
        ticket = 10
        p_spaces = 10
        while True:
        
            answer = input('Would you like to park in the garage? Please select, Y/N: ').lower()
            while answer not in ["y","n"]:
                answer = input("Incorrect Response. Please enter only Y/N: ").lower()
        
            if answer == "y":
                self.takeTicket(ticket,p_spaces)
                response = self.leaveGarage()
                while response == "no":
                    if response == "pay":
                        break
                    else:
                        response = self.leaveGarage()
                self.payForParking(ticket, p_spaces)
                break
            else:
                break
            
    
    def takeTicket(self, ticket, p_spaces):
        if ticket > 0:
            ticket -= 1
            p_spaces -= 1
        else:
            print("Sorry. There are no more tickets available.")
            print("Please wait for a car to leave.")
            quit
            
    def leaveGarage(self):
        print("Thank you for staying at our Parking Garage.")
        while True:
            pay = input("What would you like to do? Will you like to pay or leave? Pay/Leave: ").lower()
            while pay not in ["pay","leave"]:
                pay = input("Incorrect Response. Please enter only Pay/Leave: ").lower()
            
            if pay == "pay":
                return pay
                
            elif pay == "leave":
                pay = input("Will you be paying for this? Or will it be your surviving family members?: Pay/No: ").lower() # Postal 2 joke.
                while pay not in ["pay","no"]:
                    pay = input("Incorrect Response. Please enter only Pay/No: ").lower()
                
                if pay == "no":
                    print("You are not getting out of here without paying.")
                    return pay 
                elif pay == "pay":
                    return pay  
        
    
    def payForParking(self, ticket, p_spaces):
        print("Thank you, and have a nice day!")
        ticket += 1
        p_spaces += 1
        
        

g = Garage()
g.solution()
