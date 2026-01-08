class Player:
    def __init__(self, name, sport, score=0):
        self.name= name
        self.sport=sport
        self.score=score

    def show_info(self):
        print("Player detail:")
        print("Player Name: "+ self.name)
        print("Sport: "+ self.sport)
        print("Score: ", self.score)
    def increase_score(self,points):
        oldscore= self.score
        self.score+= points
        print(f"Player {self.name} has increased the scored from {oldscore} to {self.score}")
        self.show_info()
        return self.score
    def reset_score(self):
        self.score=0
        print(f"The score of player {self.name} has been reseted")
        self.show_info()
        return self.score



Player1= Player("Messi", "Football")
Player2=Player("Ronaldo", "Football")
Player1.show_info()
Player2.show_info()
Player1.increase_score(5)
Player2.increase_score(10)
Player1.reset_score()























