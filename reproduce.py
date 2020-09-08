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
        summative = 0
        for j in social_network:
            if len(families[j].children) > 0:
                summative += math.exp(1 / max(families[j].maxChildAge, 1)) - 1
        counted = len(social_network)

        if counted != 0:
            pi = summative / counted

        summative = 0
        counted = 0
        for j in social_network:
            if len(families[j].children) > 0 and families[j].mother.age == mother.age:
                summative += math.exp(1 / max(1, families[j].maxChildAge)) - 1

        for j in social_network:
            if families[j].mother.age == mother.age:
                counted += 1
        if counted != 0:
            pi_star = summative / counted

        # TODO else?
    else:
        p = families[i].childnum + 1
        summative = 0
        for j in social_network:
            if len(families[j].children) > p:
                summative += 1
        counted = 0
        for j in social_network:
            if len(families[j].children) > 0:
                counted += 1
        if counted != 0:
            pi = summative / counted

        summative = 0
        for j in social_network:
            if len(families[j].children) > p and families[j].mother.age == mother.age:
                summative += 1
        counted = 0
        for j in social_network:
            if len(families[j].children) > 0 and families[j].mother.age == mother.age:
                counted += 1
        if counted != 0:
            pi_star = summative / counted
    return pi, pi_star


def create_people(i):
    mom = families[i].mother
    gender = 0
    if random.random() < 0.5:
        gender = 1
    child = mom
    child.id = len(people)
    child.gender = gender
    added_people.append(child)
    families[i].children.append(added_people[-1])


def reproduce():
    print(len(families))
    for i in range(len(families)):
        mom = families[i].mother
        if mom is None:
            continue

        neighbors = []
        for j in range(len(families)):
            if families[j].mother is not None and province_neighbor(mom, families[j].mother) and \
                    economic_neighbor(mom, families[j].mother) and mom != families[j].mother:
                neighbors.append(j)

        social_network = []
        b = random.randint(mom.age - gammaBar, mom.age + gammaBar)
        for j in neighbors:
            if b - gammaBar <= families[j].mother.age <= b + gammaBar and \
                    religion_neighbor(mom, families[j].mother) and \
                    education_neighbor(mom, families[j].mother) and i != j:
                social_network.append(j)

        pi, pi_star = calc_p(i, mom, social_network)
        si = 1 + xi * ((math.exp(beta * (pi - pi_star)) / (1 + math.exp(beta * (pi - pi_star)))) - 0.5)

        married_same = 0
        for j in range(len(families)):
            if families[j].mother is not None and families[j].mother.age == mom.age and len(
                    families[j].children) == len(families[i].children) + 1:
                married_same += 1

        married_women = 0
        for j in range(len(families)):
            if families[j].mother is not None and families[j].mother.age == mom.age:
                married_women += 1

        bpr = 0
        if married_women > 0:
            bpr = (married_same / married_women) * si

        if families[i].childnum > 0:
            bpr *= g(families[i].maxChildAge)

        if random.random() < bpr:
            create_people(i)
