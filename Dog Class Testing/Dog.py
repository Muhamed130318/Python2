import DogClass

dog1 = DogClass.Dog("cuko", 5, 25)

dog2 = {
    "race": "cuko",
    "speed": 10,
    "weight" : 44
}

print(" Race is:", dog1.race, "\n","Speed is:", dog1.speed, "\n", "Weight is:", dog1.weight)
#print(" Race is:", dog2["race"], "\n","Speed is:", dog2["speed"], "\n", "Weight is:", dog2["weight"])

dog1.increaseSpeed()

print("Dog1 increased speed is:", dog1.speed, "and weight is:", dog1.weight)

dog1.eatFood()

print("After eating, Dog1 speed is:", dog1.speed, "and weight is:", dog1.weight)

dog1.loseWeight(2)

print("After losing weight, dog1's weight is:", dog1.weight)