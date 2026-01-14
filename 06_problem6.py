from random import randint


class Train:
     def __init__(slf, trainNo):
         slf.trainNo = trainNo

     def book (Anu, fro, to):
         print(f"Ticket is booked in train no :{Anu.trainNo} from {fro} to {to}")

     def getStatus(self):
         print(f"Train no : {self.trainNo}  running on time")

     def getFare(self, trainNo,fro, to):
         print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222, 5555)} ")


t = Train(12345)
t.book("Pune", "Beed")
t.getFare(12345,"Pune", "Beed")
t.getStatus()