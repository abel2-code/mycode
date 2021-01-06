#!/usr/bin/env python3

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

for animal in farms[0]["agriculture"]:
    print(animal)

print("Which farm's animals and plants would you like to see? (Enter the number)")
answer1 = int(input("1: NE Farm \n2: W Farm \n3: SE Farm \n")) - 1

for animal in farms[answer1]["agriculture"]:
    print(animal)

not_animals = ["carrots", "celery"]

print("Which farm's animals would you like to see? (Enter the number)")
answer2 = int(input("1: NE Farm \n2: W Farm \n3: SE Farm \n")) - 1

for animal in farms[answer2]["agriculture"]:
    if animal not in not_animals:
        print(animal)
