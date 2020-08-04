from Person import *
import math
import random
marriage_probs = [0.1 for i in range(100)]

r = 1 #religion difference
e = 2 #education difference
d = 10 #province distance
w = 2 #economic distance

gammaBar = 2 #in calculating social network
alpha = 2 #in calculating social pressure
beta = 2 #in calculating social pressure







def set_parameters(sn):
    w = 10
    r = 5





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

def economic_neighbor(p1, p2):
    if math.abs(p1.w - p2.w) <= w:
        return True
    return False

def educate():
    for i in range(len(people)):
        if people[i].age > 7 and people[i].IE >= 1:
            people[i].education =  1
        if people[i].age > 15 and people[i].IE >= 2:
            people[i].education =  2
        if people[i].age > 18 and people[i].IE >= 3:
            people[i].education = 3
        if people[i].age > 20 and people[i].IE >= 4:
            people[i].education = 4
        if people[i].age > 22 and people[i].IE >= 5:
            people[i].education = 5
        if people[i].age > 27 and people[i].IE >= 6:
            people[i].education = 6

def death(p):
    p.alive = False
    family = families[p.family_id]


    if family.father is not None and p.id == family.father.id:
        family.father = None
    elif family.mother is not None and p.id == family.mother.id:
        family.mother = None
    else:
        #print(p.id, p.parentId, family.parent_id, p.family_id)

        family.children.remove(p)


def age():
    for i in range(len(people)):
        if people[i].alive:
            people[i].age += 1
            if people[i].age >= 100:
                people[i].age = 99
            if people[i].gender == 0: #man:

                if random.random() <= death_probs_male[people[i].age - 1]:
                    death(people[i])

            else:
                if random.random() <= death_probs_female[people[i].age -1]:
                    death(people[i])



def probability_of_marriage(neighbors):
    married = 0
    for person in neighbors:
        if person.married:
            married += 1
    return married/len(neighbors)



def marriage():
    for i in range(len(men)):
        neighbors = []
        for j in range(len(people)):

            if province_neighbor(men[i], people[j]) and  economic_neighbor(men[i], people[j])  :
                if i != j:
                    neighbors.append(people[j])
        potential_wives = []

        social_pressure = math.exp(beta * (probability_of_marriage(neighbors) - alpha)) / (1 + math.exp(beta * (probability_of_marriage(neighbors) - alpha)))

        set_parameters(social_pressure)
        for j in range(len(women)):
            if religoun_neighbor(men[i], neighbors[j]) and \
                    men[i].age - 2 <= neighbors[j].age <= men[i].age + 2 and \
                    education_neighbor(men[i], women[j]) and \
                    economic_neighbor(men[i], women[j]) and \
                    province_neighbor(men[i], women[j]):
                potential_wives.append(neighbors[j])


        wife = select_wife(potential_wives, men[i])
        create_family(men[i], wife)

alive = 0

def simulate():
    global alive
    step = 0
    num_iter = 3
    while step < num_iter:
        print('iteration: ' + str(step))
        step += 1


        age() #age and death
        # marriage()
        # reproduce()
        educate()

simulate()














"""
for j in range(len(neighbors)):
    if religoun_neighbor(men[i], neighbors[j]) and \
            men[i].age - gammaBar <= neighbors[j].age <= men[i].age + gammaBar and \
            education_neighbor(men[i], neighbors[j]):
        socialNetwork.append(neighbors[j])

"""
