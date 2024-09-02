class Dog:
    def __init__(self, race, speed, weight):
        self.race = race
        self.speed = speed
        self.weight = weight
    
    def increaseSpeed(self):
        self.speed += 2
    
    def eatFood(self):
        self.weight += 1
        self.speed -= 1

    def loseWeight(self, n):
        self.weight = self.weight - n