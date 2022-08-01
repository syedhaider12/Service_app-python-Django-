import random
from string import digits

def randon_str(n=5):
    return "".join([random.choice(digits) for s in range(5)])