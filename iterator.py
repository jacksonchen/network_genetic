from generator import generate
from evaluator import evaluate
from mutator import mutate

from functools import reduce

# Takes input args, generates a seed pool and then runs the GA
# Input: Args object
# Output: The best graph
def iterate(args):
    best = None
    maxScore = 0
    gensWithoutChange = 0
    fitness = []
    gens = 1

    pool = generate(args.n, args.e, args.p, args.c, args.w, args.d)
    print("Generated")
    for seed in pool:
        fitness.append(evaluate(seed, args.a))

    # Autostopping mechanism
    while gensWithoutChange <= len(pool) * 250:
        pool = mutate(pool, fitness, args.c, args.d) # Set pool with next generation
        fitness = [] # Reset fitness

        # Now populate fitness array
        for graph in pool:
            score = evaluate(graph, args.a)
            fitness.append(score)
            if score > maxScore:
                maxScore = score
                best = graph
                gensWithoutChange = 0 # Reset autostop counter
            else:
                gensWithoutChange += 1

        print("Gen", gens,
              "Best", maxScore,
              "Avg", reduce(lambda x, y: x + y, fitness) / len(fitness))
        gens += 1
    return best
