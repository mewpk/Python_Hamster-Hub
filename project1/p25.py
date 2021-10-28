import random
pi =[]
py1 =[]
py2 =[]
for x in range(1,10):
    pi.append(str(x)+"♠")
    pi.append(str(x)+"♦")
    pi.append(str(x)+"♥")
    pi.append(str(x)+"♣")
class Deck:
    def __init__(self,card_number):
        self.number = card_number
    def drew(self):
        x=pi[random.randrange(52)]
        print(str(self.number)+x)
        pi.remove(x)
class Player:
    def __init__(self,player_number):
        self.number = player_number
    def drew(self):
        x=pi[random.randrange(0,39)]
        print(str(self.number)+x)
        pi.remove(x)
Player1 = Player("mew")
Player2 = Player("x")
py1.append(Player1.drew())
py2.append(Player2.drew())
py1.append(Player1.drew())
py2.append(Player2.drew())
print(py1)
print(py2)


    