from marriage import *
from educate import *
from age import *
from reproduce import *


# print('simulate')
def print_population():
    num = 0
    for i in people:
        if i.alive:
            num += 1
    print("population in this iteration: ", num)


def simulate(num_iter):
    for step in range(num_iter):
        print('iteration: ' + str(step))
        print_population()
        marriage()
        print(len(added_familis), ' marriages occurred.')
        reproduce()
        educate()
        age()  # age and death


simulate(1)
