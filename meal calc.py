import math

def cost(mealCost, tipPercent, taxPercent):
    tipPercent = (tipPercent * mealCost)/100
    taxPercent = (taxPercent * mealCost)/100
    total = round(mealCost + tipPercent + taxPercent)
    print(total)


meal = 10.25
tip = 17
tax = 5

cost(meal, tip, tax)