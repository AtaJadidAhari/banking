import Person


from helper_functions import *

families = Person.families
people = Person.people


def g(a):
    return (3 / 2) * math.exp((-(a - 3) ** 2) / 11)


def create_people(father, mother):
    #TODO spouse?
    spouse = None
    gender = 0
    if random.random() < 1 / 2:
        gender = 1
    people.append(people(len(people), 0, gender, False, False, 0, -1, father.religion, 0, 0, spouse, mother, father,
                         father.family_number, 0, None, 0, None, None, None, father.ostan))


def reproduce():
    bpr = 0
    for i in range(len(people)):
        if people[i].gender == 0 or not people[i].alive:
            continue
        neighbors = []
        for j in range(len(people)):
            if people[j].gender == 1 and people[j].alive and province_neighbor(people[i],
                                                                               people[j]) and economic_neighbor(
                    people[i], people[j]) and i != j:
                neighbors.append(people[j])

        social_network = []
        b = random.randint(people[i].age - gammaBar, people[i].age + gammaBar)
        for j in range(len(neighbors)):
            if b - gammaBar <= neighbors[j].age <= b + gammaBar and religion_neighbor(people[i],
                                                                                      neighbors[j]) and education_neighbor(
                    people[i], neighbors[j]) and i != j:
                social_network.append(neighbors[j])

        pi = 0
        pi_star = 0

        if families[people[i].family_id].childnum == 0:
            #TODO p = ?
            p = 0
            sumation = 0
            for j in range(len(social_network)):
                if families[social_network[j].family_id].childnum > 0:
                    sumation += math.exp(1 / families[social_network[j].family_id].maxChildAge) - 1
            counted = len(social_network)
            if counted != 0:
                pi = sumation / counted
            #TODO else?
            sumation = 0
            counted = 0
            for j in range(len(social_network)):
                if families[social_network[j].family_id].childnum > 0 and social_network[j].age == people[i].age:
                    sumation += math.exp(1 / families[social_network[j].family_id].maxChildAge) - 1

            for j in range(len(social_network)):
                if social_network[j].age == people[i].age:
                    counted += 1
            if counted != 0:

                pi_star = sumation / counted

            #TODO else?

        else:
            p = families[people[i].family_id].childnum + 1
            sumation = 0
            for j in range(len(social_network)):
                if families[social_network[j].family_id].childnum > p:
                    sumation += 1
            counted = 0
            for j in range(len(social_network)):
                if families[social_network[j].family_id].childnum > 0:
                    counted += 1
            pi = sumation / counted

            sumation = 0
            for j in range(len(social_network)):
                if families[social_network[j].family_id].childnum > p and social_network[j].age == people[i].age:
                    sumation += 1
            counted = 0
            for j in range(len(social_network)):
                if families[social_network[j].family_id].childnum > 0 and social_network[j].age == people[i].age:
                    counted += 1
            pi_star = sumation / counted

        si = 1 + xi * (math.exp(beta * (pi - pi_star)) / (1 + math.exp(beta * (pi - pi_star))) - 1 / 2)

        maried_same = 0
        for j in range(len(social_network)):
            if people[i].age == social_network[j].age and families[social_network[j].family_id].childnum == p + 1:
                maried_same += 1

        maried_women = 0
        for j in range(len(people)):
            if people[j].age == people[i].age and people[j].married and people[j].gender == 1:
                maried_women += 1
        if maried_women > 0:

            bpr = (maried_same / maried_women) * si


        if p > 0:
            bpr *= g(families[people[i].family_id].maxChildAge)
        else:
            #TODO married_women == 0 --> bpr = ?
            bpr = 0
        if random.random() < bpr:
            family = families[people[i].family_id]
            create_people(family.mother, family.father)

