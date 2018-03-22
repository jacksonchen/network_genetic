import argparse

from iterator import iterate

# Takes the user input and checks for invalidity
# Input: Args object
# Output: The best graph given by GA
def initialize(args):
    if (args.a > 1 or args.a < 0):
        raise ValueError('Alpha value is not between 0 and 1')
    elif (args.p < 2):
        raise ValueError('Parent pool size must be at least 2')
    elif (args.n < 2):
        raise ValueError('Number of nodes must be at least 2')
    elif (args.e < 1):
        raise ValueError('Number of edges must be at least 1')

    return iterate(args)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='''A genetic algorithm that generates network topologies based on user input''')
    parser.add_argument('--n', type=int, default=10, help='The number of nodes in the network: [2, INF)')
    parser.add_argument('--e', type=int, default=30, help='The number of edges in the network: [1, INF)')
    parser.add_argument('--p', type=int, default=10, help='Parent pool size for the GA: [2, INF)')
    parser.add_argument('--a', type=float, default=0, help='Alpha value for evaluation: [0, 1]')
    parser.add_argument('--c', type=bool, default=True, help='Whether the graph should be connected (default: true)')
    parser.add_argument('--w', type=bool, default=False, help='Whether the graph should be weighted (default: false) [TODO]')
    parser.add_argument('--d', type=bool, default=False, help='Whether the graph should be directed (default: false)')

    print(initialize(parser.parse_args()))
