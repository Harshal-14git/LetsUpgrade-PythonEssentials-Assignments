import random
MaxTicketsAvailable = int(input("Enter Maximum Available Tickets : "))
participants = []
for temp in range(MaxTicketsAvailable):
    name = str(input("Enter Participant Name - "))
    participants.append(name)
print("Participants - ",participants)

n = random.randint(0,MaxTicketsAvailable-1)
#print("Lottery winner -",participants[n],",","Index -",n,".") 
print("Lottery winner -",participants[n])