import Person
import random

from helper_functions import *

families = Person.families
people = Person.people


def g(a):
    return (3 / 2) * math.exp((-(a - 3) ** 2) / 11)


def calc_p(i, mother, social_network):
    pi, pi_star = 0, 0
    if families[i].childnum == 0:
        # TODO p = ?
        p = 0
        sumation = 0
        for j in range(len(social_network)):
            if families[social_network[j].family_id].childnum > 0:
                sumation += math.exp(1 / families[social_network[j].family_id].maxChildAge) - 1
        counted = len(social_network)
        if counted != 0:
            pi = sumation / counted
        # TODO else?
        sumation = 0
        counted = 0
        for j in range(len(social_network)):
            if families[social_network[j].family_id].childnum > 0 and social_network[j].age == mother.age:
                sumation += math.exp(1 / families[social_network[j].family_id].maxChildAge) - 1

        for j in range(len(social_network)):
            if social_network[j].age == mother.age:
                counted += 1
        if counted != 0:
            pi_star = sumation / counted

        # TODO else?

    else:
        p = families[i].childnum + 1
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
            if families[social_network[j].family_id].childnum > p and social_network[j].age == mother.age:
                sumation += 1
        counted = 0
        for j in range(len(social_network)):
            if families[social_network[j].family_id].childnum > 0 and social_network[j].age == mother.age:
                counted += 1
        pi_star = sumation / counted
    return pi, pi_star


def create_people(father, mother):
    print("create_people")
    gender = 0
    if random.random() < 0.5:
        gender = 1
    people.append(Person.Person(len(people), "Id", mother.id, gender, "BirthDate", "PostalCode", mother.IsUrban,
                                mother.ProvinceName, mother.CountyName, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, "IsBehzisti_Malool", "IsBimarkhas", "SenfName",
                                "IsTamin_Karfarma", "Tamin_KargarCount", "IsBazneshaste_Sandoghha",
                                "IsBimePardaz_Sandoghha", 0))


def reproduce():
    for i in range(len(families)):
        mother = families[i].mother
        if mother is None:
            continue

        neighbors = []
        for j in range(len(people)):
            if people[j].gender == 1 and people[j].alive and province_neighbor(mother, people[j]) and \
                    economic_neighbor(mother, people[j]) and mother != people[j]:
                neighbors.append(people[j])

        social_network = []
        b = random.randint(mother.age - gammaBar, mother.age + gammaBar)
        for j in range(len(neighbors)):
            if b - gammaBar <= neighbors[j].age <= b + gammaBar and religion_neighbor(mother, neighbors[j]) and \
                    education_neighbor(mother, neighbors[j]) and mother != people[j]:
                social_network.append(neighbors[j])

        pi, pi_star = calc_p(i, mother, social_network)
        si = 1 + xi * (math.exp(beta * (pi - pi_star)) / (1 + math.exp(beta * (pi - pi_star))) - 1 / 2)

        married_same = 0
        for j in range(len(social_network)):
            if mother.age == social_network[j].age and \
                    families[social_network[j].family_id].childnum == families[i].childnum + 1:
                married_same += 1

        married_women = 0
        for j in range(len(people)):
            if people[j].age == mother.age and people[j].married and people[j].gender == 1:
                married_women += 1

        bpr = 0
        if married_women > 0:
            bpr = (married_same / married_women) * si

        if families[i].childnum > 0:
            bpr *= g(families[i].maxChildAge)

        if random.random() < bpr:
            create_people(families[i].mother, families[i].father)
