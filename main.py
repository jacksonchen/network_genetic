from generator import generate
from iterator import iterate
from classes.graph import Graph

def initialize(params):
    seed = generate()
    best = iterate(seed)
    return best
