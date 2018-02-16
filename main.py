from generator import generate
from iterator import iterate

def initialize(params):
    seed = generate()
    best = iterate(seed)
    return best
