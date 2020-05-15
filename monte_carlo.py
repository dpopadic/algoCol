# monte carlo prototype -----------------------------------------------------------------------------------------------
# intro ----------------
# When one has a generative model of a domain but no analytical solution, one uses monte-carlo simulation. It's a
# class of techniques using random sampling a draw from a distribution. Solutions for problems can be calculated
# using repeated draws and aggregating the results.
# 1. create domain model
# 2. generate random draws from the distribution
# 3. deterministic output calculation
# 4. compute aggregate statistics
import numpy as np
import random

# simulation: roll pair of dice ---------------------------------------------------------------------------------------
# Thinking of the dice as a probability distribution helps. For every roll, there's some probability of getting
# each possible number. Collectively, these probabilites represent the distribution for the dice-rolling domain.
# Imagine you want to know what this distribution looks like, having only the knowledge that you have two dice and
# each one can roll a 1-6 with equal probability. Using MC-simulation, one can simulate the distribution.

# distribution
def sim_die_pair():
    return random.randint(1, 6) + random.randint(1, 6)

n = 1000
xi = []
for _ in range(n):
    xi.append(sim_die_pair())

# expected value
print("expected value of rolling a pair of die is ", np.round(np.mean(xi), 0))

# probability of getting 5 or higher
def pair_prob_kplus(k, n):
    x = []
    for _ in range(n):
        x.append(sim_die_pair() >= k)
    p = sum(x) / n
    return p

pair_prob_kplus(k=5, n=1000)


# simulation: estimating pi -------------------------------------------------------------------------------------------











