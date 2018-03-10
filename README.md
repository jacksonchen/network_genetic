# Genetic Algorithm for Network Topology

## Usage

```
usage: main.py [-h] [--n N] [--e E] [--p P] [--a A] [--c C] [--w W]

A genetic algorithm that generates network topologies based on user input

optional arguments:
  -h, --help  show this help message and exit
  --n N       The number of nodes in the network
  --e E       The number of edges in the network
  --p P       Parent pool size for the GA
  --a A       Alpha value for evaluation: [0, 1]
  --c C       Whether the graph should be connected (default: true)
  --w W       Whether the graph should be weighted
```

## Pipeline

This GA will be split into the following components, with each interaction described:

`main.py`
  - Purpose: To initiate and to end the entire process
  - Input: User execution or kill notification, any custom parameters (such as alpha)
  - Output: Best networks and their scores

`generator.py`
  - Purpose: Generate a seed network
  - Input: Custom parameters for network constraints (if any)
  - Output: A network described in an object

`iterator.py`
  - Purpose: Begin and maintain a loop of evaluating and mutating networks
  - Input: Seed network from `generator`
  - Output: A best network given certain specified stopping mechanisms

`evaluator.py`
  - Purpose: Runs fitness simulations on networks to evaluate them
  - Input: A network
  - Output: A score

`mutator.py`
  - Purpose: Mutate the networks that performed the best
  - Input: A set of networks (or a network)
  - Output: A mutated network
