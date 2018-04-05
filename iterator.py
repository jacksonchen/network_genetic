from generator import generate
from evaluator import evaluate
from mutator import mutate

from functools import reduce
from multiprocessing import Pool

alpha = 0

def runFitness(graph):
    fitness = []
    score = evaluate(graph, alpha)
    return score

# Takes input args, generates a seed pool and then runs the GA
# Input: Args object
# Output: The best graph
def iterate(args):
    global alpha

    fitness = []
    gens = 1
    gensWithoutChange = 0
    maxScore = 0
    alpha = args.a
    best = None

    pool = generate(args.n, args.e, args.p, args.c, args.w, args.d)
    print("Generated")
    for seed in pool:
        fitness.append(evaluate(seed, args.a))

    # Autostopping mechanism
    while gensWithoutChange <= len(pool) * args.s:
        pool = mutate(pool, fitness, args.c, args.d) # Set pool with next generation
        fitness = [] # Reset fitness

        # Now populate fitness array
        with Pool(4) as p:
            fitness = p.map(runFitness, pool)

        for i in range(len(fitness)):
            if fitness[i] > maxScore:
                maxScore = fitness[i]
                best = pool[i]
                gensWithoutChange = 0 # Reset autostop counter
            else:
                gensWithoutChange += 1

        print("Gen", gens,
              "Best", maxScore,
              "Avg", reduce(lambda x, y: x + y, fitness) / len(fitness))
        gens += 1
    return best
