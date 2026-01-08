class Team:
    def __init__(self, name, total_score):
        self.name=name
        self.total_score=0

    def display(self):
        print("======================")
        print("Team's information: ")
        print("Team Name: "+ self.name)
        print(f"Score: {self.total_score}")


class Match:
    def __init__(self, team1, team2):
        self.team1=team1
        self.team2=team2
        self.winner=None

    def play(self, team1goal, team2goal):
        if team1goal > team2goal:
           self.winner= self.team1
           self.team1.score +=3

        elif team1goal < team2goal:
            self.winner= self.team2
            self.team2.score+=3

        else:
            self.winner="Draw"
            self.team1.score+=1
            self.team2.score+=1
        

        print(f"Match: {self.team1.name}  vs {self.team2.name} || Result: {self.winner} with goal {team1goal}:{team2goal}")

class Tournament:

    def __init__(self, tournament_name):
        self.tournament_name= tournament_name
        self.listteam=[]


    def addteam(self, team):
       self.listteam.append(team)

    def declare_champion(self):
        print(f"\n--- {self.tournament_name} Final Standings ---")
        sorted_teams = sorted(self.teams, key=lambda x: x.total_score, reverse=True)
        
        for t in sorted_teams:
            print(f"{t.name}: {t.total_score} pts")
        
        champion = sorted_teams[0]
        print(f"\n The Champion is: {champion.name} ")
            
t1 = Team("Lions")
t2 = Team("Eagles")
t3 = Team("Sharks")

my_cup = Tournament("Grand Slam")
my_cup.add_team(t1)
my_cup.add_team(t2)
my_cup.add_team(t3)

m1 = Match(t1, t2)
m1.play(2, 0) 

m2 = Match(t2, t3)
m2.play(1, 1)  

my_cup.declare_champion()