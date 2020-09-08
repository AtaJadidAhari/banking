import Person
import random

families = Person.families
people = Person.people


def death(p):
    p.alive = False
    family = families[p.family_id]

    if family.father is not None and p.id == family.father.id:
        family.father = None
        if family.mother is None and len(family.children) == 0:
            family.alive = False
        elif family.mother is None:
            Person.set_parent_to_orphans(family)
    elif family.mother is not None and p.id == family.mother.id:
        family.mother = None
        if family.father is None and len(family.children) == 0:
            family.alive = False
        elif family.father is None:
            Person.set_parent_to_orphans(family)
    else:

        family.children.remove(p)


def age():
    for i in range(len(people)):
        if people[i].alive:
            people[i].age += 1
            if people[i].age >= 100:
                people[i].age = 99
            if people[i].gender == 0:  # man:

                if random.random() <= Person.death_probs_male[people[i].age - 1]:
                    death(people[i])

            else:
                if random.random() <= Person.death_probs_female[people[i].age - 1]:
                    death(people[i])

    for i in range(len(families)):
        if len(families[i].children) > 0:
            families[i].maxChildAge += 1
