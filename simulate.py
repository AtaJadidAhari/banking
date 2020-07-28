from Person import *
import math
import random
marriage_probs = [0.1 for i in range(100)]

r = 3 #religion difference
e = 3 #education difference
d = 10 #province distance

def religoun_neighbor(p1, p2):
    if math.abs(p1.religoun - p2.religoun) <= r:
        return True
    return False

def education_neighbor(p1, p2):
    if math.abs(p1.education - p2.education) <= e:
        return True
    return False

def province_neighbor(p1, p2):
    if math.abs(p1.x - p2.x)**2 + math.abs(p1.y - p2.y)**2 <= d:
        return True
    return False

def age():
    for i in range(len(people)):
        people[i].age += 1
        if people[i].age >= 100:
            people[i].age = 99
        if people[i].gender == 0: #man:

            if random.random() <= death_probs_male[people[i].age - 1]:
                people[i].alive = False
        else:
            if random.random() <= death_probs_female[people[i].age -1]:
                people[i].alive = False


def marriage():
    for i in range(len(men)):
        potential_wives = []

alive = 0

def simulate():
    global alive
    step = 0
    num_iter = 100
    while step < num_iter:
        """
        for i in people:
            if i.alive:
                alive += 1
        print("alive: " , alive ,  "dead: " , len(people) - alive , " step: ", step)
        alive = 0
        """
        step += 1

        #marriage()
        age()

simulate()

