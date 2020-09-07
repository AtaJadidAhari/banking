import math

# print('Helper function')
marriage_probs = [0.1 for i in range(100)]

r = 1  # religion difference
e = 2  # education difference
d = 4  # province distance
w = 2  # economic distance

gammaBar = 2  # in calculating social network
alpha = 0  # in calculating social pressure
beta = 1  # in calculating social pressure

xi = 2

r_low = -1
r_high = 2
w_low = -1
w_high = 2
e_low = -1
e_high = 2

added_familis = []

alive = 0


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
    if math.fabs(p1.x - p2.x) ** 2 + math.fabs(p1.y - p2.y) ** 2 <= d:
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
