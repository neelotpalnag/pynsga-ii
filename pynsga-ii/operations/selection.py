from .pareto_tools import ranking
from random import random


def selection(num_obj, X_parent, pop_size, num_params, seed):

    X_sel = [[0 for x in range(num_params)] for y in range(pop_size)]

    # Perform TOURNAMENT SELECTION
    # For this,
    # 1. Perform Ranking & find crowding distances
    # 2. Pick two solutions randomly from the population & perform tournament to pick one,
    #    until NP members are obtained

    F_evaluated = [[0 for x in range(0, num_obj, 1)] for y in range(pop_size)]
    for f in range(0, num_obj, 1):
        for i in range(0, len(X_parent), 1):
            F_evaluated[i][f] = X_parent[i][num_params + f]

    ranking_results = ranking(F_evaluated, X_parent)
    individuals = ranking_results[1]

    X_winners = []
    for i in range(0, pop_size, 1):
        # Choose 2 members randomly:
        random.seed(seed)
        rn = random.sample(range(0, pop_size-1), 2) # List of 2 random numbers

        # Now compare the two members:
        if individuals[rn[0]].rank < individuals[rn[1]].rank:
            X_winners.append(X_parent[rn[0]])
        elif individuals[rn[0]].rank > individuals[rn[1]].rank:
            X_winners.append(X_parent[rn[1]])
        else:
            if individuals[rn[0]].crowding_distance <= individuals[rn[1]].crowding_distance:
                X_winners.append(X_parent[rn[1]])
            else:
                X_winners.append(X_parent[rn[0]])

    return X_winners
