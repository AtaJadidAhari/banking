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


r_low = -1
r_high = 2
w_low = -1
w_high = 2
e_low = -1
e_high = 2







def set_parameters(sn):
    global r_low, r_high, w_low, w_high, e_low, e_high
    if 0 <= sn <= 0.2:
        r_low = w_low = e_low = -1
        r_high = w_high = e_high = 2

    elif sn <= 0.5:
        r_low = w_low = e_low = -1
        r_high = w_high = e_high = 3

    elif sn <= 0.8:
        r_low = w_low = e_low = -2
        r_high = w_high = e_high = 4

    else:
        r_low = w_low = e_low = -1
        r_high = w_high = e_high = -3






def religion_neighbor(p1, p2, method=0):
    if method == 0:
        if math.abs(p1.religion - p2.religion) <= r:
            return True
        return False
    else:
        if r_low <= p2.religion - p1.religion <= r_high:
            return True
        return False

def education_neighbor(p1, p2, method=0):
    if method == 0:
        if math.abs(p1.education - p2.education) <= e:
            return True
        return False
    else:
        if e_low <= p2.education - p1.education <= e_high:
            return True
        return False

def province_neighbor(p1, p2, method=0):

    if math.abs(p1.x - p2.x)**2 + math.abs(p1.y - p2.y)**2 <= d:
        return True
    return False

def economic_neighbor(p1, p2, method=0):
    if method == 0:
        if math.abs(p1.w - p2.w) <= w:
            return True
        return False
    else:
        if w_low <= p2.w - p1.w <= w_high:
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


def create_family(husband, wife):
    families.append(Family(len(families), husband.id, husband, wife, 0, [], 0, 100))
    husband.married = True
    wife.married = True

def select_wife(wifes, man):
    #select wife based on probability
    return wifes[0]


def marriage():
    for i in range(len(men)):
        neighbors = []
        for j in range(len(people)):

            if province_neighbor(men[i], people[j]) and  economic_neighbor(men[i], people[j])  :
                if i != j:
                    neighbors.append(people[j])

        social_network = []
        b = random.randInt(men[i].age - gammaBar, men[i].age + gammaBar)


        for j in range(len(neighbors)):

            if b - gammaBar <= men[i].age <= b + gammaBar and  religion_neighbor(men[i], neighbors[j]) and education_neighbor(men[i], neighbors[j]):
                if i != j:
                    social_network.append(people[j])
        potential_wives = []


        social_pressure = math.exp(beta * (probability_of_marriage(social_network) - alpha)) / (1 + math.exp(beta * (probability_of_marriage(social_network) - alpha)))

        set_parameters(social_pressure)
        for j in range(len(women)):
            if religion_neighbor(men[i], neighbors[j], 1) and \
                    men[i].age - 2 <= neighbors[j].age <= men[i].age + 2 and \
                    education_neighbor(men[i], women[j], 1) and \
                    economic_neighbor(men[i], women[j], 1) and \
                    province_neighbor(men[i], women[j], 1):
                potential_wives.append(women[j])


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









