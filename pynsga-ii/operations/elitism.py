from .pareto_tools import *
from .evaluate import evaluate


# Perform
def elitism(num_obj, X_parent, X_daughter, num_params):

    X_pool = X_parent + X_daughter

    pop_size = len(X_parent)

    # STEP 1 : Create fronts of all 2 x pop_size individuals in the combined pool of parent and daughter

    # F_evaluated is a 2D list, with elements as [Objective][Individual]
    # F_evaluated[i][j] implies the value of the (i)th objective for the (j)th individual
    F_evaluated = [[0 for x in range(0, num_obj, 1)] for y in range(2*pop_size)]
    for f in range(0, num_obj, 1):
        for i in range(0, len(X_pool), 1):
            F_evaluated[i][f] = X_pool[i][num_params + f]

    [Fronts, Individuals] = ranking(F_evaluated, X_pool)


    # elite_population = [[0 for x in range(0, num_params, 1)] for y in range(pop_size)]
    elite_population = []
    counter = 2*pop_size
    for front in Fronts:
        front_size = len(Fronts[front])
        if front_size<=counter:
            counter = counter - front_size
            for i in Fronts[front]:
                elite_population.append(Individuals[i].X)

        else:
            # Sort the individuals of the current front on the basis of crowding distance
            # and select the allowed number of individuals with higher crowding distances
            sorter_dict = {}
            front_unsorted = Fronts[front]
            for i in front_unsorted:
                sorter_dict[i] = Individuals[i].crowding_distance

            buf = sorted(sorter_dict, key=sorter_dict.__getitem__, reverse=True)
            for i in range(0, counter, 1):
                elite_population.append(Individuals[buf[i]].X)

    return [elite_population[:pop_size], Fronts, F_evaluated]









