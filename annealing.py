import random
import math

def calculate_cost(state):
    conflicts = 0
    n = len(state)

    for i in range(n):
        for j in range(i + 1, n):
            if state[i] == state[j] or abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    return conflicts


def get_neighbor(state):
    next_state = state[:]

    col = random.randint(0, 7)
    row = random.randint(0, 7)

    while next_state[col] == row:
        row = random.randint(0, 7)

    next_state[col] = row
    return next_state


def simulated_annealing():
    current = [random.randint(0, 7) for _ in range(8)]
    best = current[:]

    T = 100
    cooling_rate = 0.99

    while T > 0.001:
        current_cost = calculate_cost(current)

        if current_cost == 0:
            return current

        next_state = get_neighbor(current)
        next_cost = calculate_cost(next_state)

        delta_E = current_cost - next_cost

        if delta_E > 0:
            current = next_state
        else:
            probability = math.exp(delta_E / T)

            if random.random() < probability:
                current = next_state

        if calculate_cost(current) < calculate_cost(best):
            best = current[:]

        T *= cooling_rate

    return best


result = simulated_annealing()

print("Final Solution:", result)
print("Conflicts:", calculate_cost(result))

print("\nChessboard:")
for row in range(8):
    for col in range(8):
        if result[col] == row:
            print("Q", end=" ")
        else:
            print(".", end=" ")
    print()