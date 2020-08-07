from Person import *
import math
import random
marriage_probs = [0.1 for i in range(100)]

r = 1 #religion difference
e = 2 #education difference
d = 4 #province distance
w = 2 #economic distance

gammaBar = 2 #in calculating social network
alpha = 0 #in calculating social pressure
beta = 1#in calculating social pressure


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
        r_high = w_high = e_high = 5






def religion_neighbor(p1, p2, method=0):
    if method == 0:
        if math.fabs(p1.religion - p2.religion) <= r:
            return True
        return False
    else:
        if r_low <= p2.religion - p1.religion <= r_high:
            return True
        return False

def education_neighbor(p1, p2, method=0):
    if method == 0:
        if math.fabs(p1.education - p2.education) <= e:
            return True
        return False
    else:
        if e_low <= p2.education - p1.education <= e_high:
            return True
        return False

def province_neighbor(p1, p2, method=0):

    if math.fabs(p1.x - p2.x)**2 + math.fabs(p1.y - p2.y)**2 <= d:
        return True
    return False

def economic_neighbor(p1, p2, method=0):
    if method == 0:
        if math.fabs(p1.w - p2.w) <= w:
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
        if family.mother is None and len(family.children) == 0:
            family.alive = False
        elif family.mother is None:
            set_parent_to_orphans(family)
    elif family.mother is not None and p.id == family.mother.id:
        family.mother = None
        if family.father is None and len(family.children) == 0:
            family.alive = False
        elif family.father is None:
            set_parent_to_orphans(family)
    else:


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

added_familis = []





def add_child(p, family_id):
    family = families[family_id]
    family.append(p)



def create_new_child(family):
    father = family.father
    mother = family.mother

    child = Person([0 for i in range(44)])

    child.IE = (father.IE + mother.IE)/2
    child.family_id = family.family_id
    child.parent_id = father.id

    add_child(child, family.family_id)
    
















def create_family(husband, wife):
    #print(husband.family_id, wife.family_id, 'here')
    wife_family = families[wife.family_id]
    husband_family = families[husband.family_id]
    if husband.id == husband.parent_id:

        family = families[husband.family_id]
        wife.family_id = family.family_id
        if wife.parent_id == wife.id:
            for i in range(len(wife_family.children)):
                family.children.append(wife_family.children[i])
                wife_family.children[i].family_id = family.family_id
                wife_family.children[i].parent_id = husband.id

            wife_family.alive = False
    elif wife.id == wife.parent_id:
        family = families[wife.family_id]
        family.father = husband
        if husband.parent_id == husband.id:
            for i in range(len(husband_family.children)):
                family.children.append(husband_family.children[i])
                husband_family.children[i].family_id = family.family_id
                husband_family.children[i].parent_id = husband.id

        husband.family_id = family.family_id

    else:
        id = len(families)
        families.append(Family(id, husband.id, husband, wife, 0, [], 0, 100))
        family = families[-1]
        husband.family_id = id

        wife.family_id = id



    husband.married = True
    wife.married = True
    wife.parent_id = husband.id
    husband.parent_id = husband.id
    family.mother = wife
    family.father = husband
    added_familis.append(family.family_id)



def select_wife(wifes, man):
    #TODO select wife based on probability

    return wifes[0]


def marriage():
    for i in range(len(people)):

        if people[i].gender == 0 and not people[i].married and people[i].alive: #bachelors
            if random.random() < 0.1: #TODO fix probabilty
                neighbors = []
                for j in range(len(people)):

                    if province_neighbor(people[i], people[j]) and  economic_neighbor(people[i], people[j])  :
                        if i != j:
                            neighbors.append(people[j])

                social_network = []

                b = random.randint(people[i].age - gammaBar, people[i].age + gammaBar)


                for j in range(len(neighbors)):

                    if b - gammaBar <= neighbors[j].age <= b + gammaBar and  religion_neighbor(people[i], neighbors[j]) and education_neighbor(people[i], neighbors[j]):
                        if i != j:
                            social_network.append(people[j])
                potential_wives = []

                if len(social_network) == 0:
                    continue
                social_pressure = math.exp(beta * (probability_of_marriage(social_network) - alpha)) / (1 + math.exp(beta * (probability_of_marriage(social_network) - alpha)))

                set_parameters(social_pressure)
                for j in range(len(social_network)):
                    if social_network[j].gender == 1 and not social_network[j].married and social_network[j].alive: #bachelors
                        if religion_neighbor(people[i], social_network[j], 1) and \
                                people[i].age - 2 <= social_network[j].age <= people[i].age + 2 and \
                                education_neighbor(people[i], social_network[j], 1) and \
                                economic_neighbor(people[i], social_network[j], 1) and \
                                province_neighbor(people[i], social_network[j], 1):
                            potential_wives.append(social_network[j])

                if len(potential_wives) > 0:

                    wife = select_wife(potential_wives, people[i])
                    create_family(people[i], wife)

alive = 0

def print_population():
    num = 0
    for i in people:
        if i.alive:
            num += 1
    print("population in this iteration: ", num)





def simulate():
    global alive
    step = 0
    num_iter = 3
    while step < num_iter:

        print('iteration: ' + str(step))
        print_population()

        step += 1



        #marriage()
        print(len(added_familis), ' marriages occurred.')
        #reproduce()
        #educate()

        #age()  # age and death


simulate()



