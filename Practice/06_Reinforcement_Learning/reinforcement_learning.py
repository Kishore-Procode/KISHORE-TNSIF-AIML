# reinforcement learning practice

# rl = agent learns by interacting with environment
# takes actions, gets rewards or penalties
# goal: maximize total reward over time

# key concepts:
# agent -> the learner
# environment -> world the agent interacts with
# state -> current situation
# action -> what the agent can do
# reward -> feedback from environment
# policy -> strategy for choosing actions
# q-value -> expected reward for action in a state

# q-learning update rule:
# Q(s,a) = Q(s,a) + lr * [reward + gamma * max(Q(s',a')) - Q(s,a)]

import numpy as np
import random


# grid world with q-learning
# 4x4 grid:
# S = start (0,0), X = wall, G = goal (3,3)
# reward: goal=+100, step=-1

GRID_SIZE = 4
ACTIONS = ["up", "down", "left", "right"]
ACTION_MAP = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

WALLS = [(1, 1), (2, 3), (3, 1)]
GOAL = (3, 3)
START = (0, 0)

# hyperparameters
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.9
EPSILON = 0.2
EPISODES = 500


def get_next_state(state, action):
    dr, dc = ACTION_MAP[action]
    new_r = state[0] + dr
    new_c = state[1] + dc

    # boundary check
    if new_r < 0 or new_r >= GRID_SIZE or new_c < 0 or new_c >= GRID_SIZE:
        return state

    # wall check
    if (new_r, new_c) in WALLS:
        return state

    return (new_r, new_c)


def get_reward(state):
    if state == GOAL:
        return 100
    elif state in WALLS:
        return -10
    else:
        return -1


# initialize q-table
q_table = np.zeros((GRID_SIZE, GRID_SIZE, len(ACTIONS)))

print(f"hyperparameters:")
print(f"  learning rate: {LEARNING_RATE}")
print(f"  discount factor: {DISCOUNT_FACTOR}")
print(f"  epsilon: {EPSILON}")
print(f"  episodes: {EPISODES}")
print(f"\ntraining...\n")

# training
rewards_per_episode = []
steps_per_episode = []

for episode in range(EPISODES):
    state = START
    total_reward = 0
    steps = 0
    max_steps = 100

    while state != GOAL and steps < max_steps:
        r, c = state

        # epsilon-greedy
        if random.random() < EPSILON:
            action_idx = random.randint(0, len(ACTIONS) - 1)  # explore
        else:
            action_idx = np.argmax(q_table[r, c])  # exploit

        action = ACTIONS[action_idx]
        next_state = get_next_state(state, action)
        reward = get_reward(next_state)

        # q-learning update
        nr, nc = next_state
        old_q = q_table[r, c, action_idx]
        max_future_q = np.max(q_table[nr, nc])
        new_q = old_q + LEARNING_RATE * (reward + DISCOUNT_FACTOR * max_future_q - old_q)
        q_table[r, c, action_idx] = new_q

        state = next_state
        total_reward += reward
        steps += 1

    rewards_per_episode.append(total_reward)
    steps_per_episode.append(steps)

    if (episode + 1) % 100 == 0:
        avg_reward = np.mean(rewards_per_episode[-100:])
        avg_steps = np.mean(steps_per_episode[-100:])
        print(f"  episode {episode + 1}: avg reward = {avg_reward:.1f}, avg steps = {avg_steps:.1f}")


# showing learned policy
print("\nlearned policy (best action at each state):\n")

arrows = {"up": "^", "down": "v", "left": "<", "right": ">"}

for r in range(GRID_SIZE):
    row_str = ""
    for c in range(GRID_SIZE):
        if (r, c) == GOAL:
            row_str += " G "
        elif (r, c) in WALLS:
            row_str += " X "
        elif (r, c) == START:
            best = ACTIONS[np.argmax(q_table[r, c])]
            row_str += f" S{arrows[best]}"
        else:
            best = ACTIONS[np.argmax(q_table[r, c])]
            row_str += f" {arrows[best]} "
    print(row_str)


# testing the trained agent
print("\ntesting trained agent:")

state = START
path = [state]
steps = 0

print(f"start: {state}")
while state != GOAL and steps < 20:
    r, c = state
    action_idx = np.argmax(q_table[r, c])
    action = ACTIONS[action_idx]
    state = get_next_state(state, action)
    path.append(state)
    steps += 1
    print(f"  step {steps}: {action} -> {state}")

if state == GOAL:
    print(f"\ngoal reached in {steps} steps!")
    print(f"path: {' -> '.join([str(p) for p in path])}")
else:
    print(f"\ndid not reach goal within 20 steps")


# q-table max values
print("\nq-table max values per state:")
for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
        if (r, c) in WALLS:
            print("  wall ", end="")
        elif (r, c) == GOAL:
            print("  goal ", end="")
        else:
            max_q = np.max(q_table[r, c])
            print(f" {max_q:5.1f} ", end="")
    print()
