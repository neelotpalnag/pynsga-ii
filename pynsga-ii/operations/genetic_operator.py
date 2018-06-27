import random
from operations.evaluate import evaluate


def genetic_operator(num_objectives, X_pool, X_hi, X_lo, cxi, mui, pop_size, num_params, seed):

    mutated = 0
    crossed = 0
    p = 1

    random.seed(seed)
    X_daughters = []
    for i in range(0, pop_size, 1):
        # Performing Crossover with 90% probability
        cxp = random.uniform(0, 1)
        rn = random.sample(range(0, pop_size - 1), 3)  # List of 3 random numbers
        if cxp < 0.9:


            xd1 = []
            xd2 = []

            for j in range(0, num_params, 1):
                rn_beta = random.random()
                beta = beta_calculator(rn_beta, cxi)
                xd1_val = (0.5 * ((1 - beta) * X_pool[rn[0]][j] + (1 + beta) * X_pool[rn[1]][j]))
                if xd1_val > X_hi[j]:
                    xd1_val = X_hi[j]
                elif xd1_val < X_lo[j]:
                    xd1_val = X_lo[j]
                xd2_val = (0.5 * ((1 + beta) * X_pool[rn[0]][j] + (1 - beta) * X_pool[rn[1]][j]))
                if xd2_val > X_hi[j]:
                    xd2_val = X_hi[j]
                elif xd2_val < X_lo[j]:
                    xd2_val = X_lo[j]

                xd1.append(xd1_val)
                xd2.append(xd2_val)

                mup = random.uniform(0, 1)
                if mup < 0.1:
                    xd1[j] = X_lo[j] + random.uniform(0, 1) * (X_hi[j] - X_lo[j])
                    xd2[j] = X_lo[j] + random.uniform(0, 1) * (X_hi[j] - X_lo[j])

            xev1 = xd1
            xev2 = xd2
            for k in range(0, num_objectives, 1):
                xd1.append(evaluate(k, xev1))
                xd2.append(evaluate(k, xev2))

            crossed = 1
            mutated = 0

        else:
            XM = []
            XP = X_pool[rn[2]]
            for j in range(0, num_params, 1):
                rn = random.random()
                val = XP[j] + delta_calculator(rn, mui)
                if val > X_hi[j]:
                    val = X_hi[j]
                elif val < X_lo[j]:
                    val = X_lo[j]
                XM.append(val)

            x_ev = XM
            for k in range(0, num_objectives, 1):
                XM.append(evaluate(k, x_ev))

            mutated = 1
            crossed = 0

        if crossed:
            X_daughters.append(xd1)
            X_daughters.append(xd2)
            crossed = 0

        elif mutated:
            X_daughters.append(XM)
            mutated = 0

    return X_daughters


def beta_calculator(rn, cxi):
    if rn < 0.5:
        return pow(2*rn, (1/(cxi+1)))
    else:
        return 1/pow(2*(1-rn), (1/(cxi+1)))


def delta_calculator(rn, mui):
    if rn < 0.5:
        return pow((2*rn), (1/(mui+1))) -1
    else:
        return 1 - 1/pow((2 -2*rn), (1/(mui+1)))