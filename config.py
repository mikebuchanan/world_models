import numpy as np
import random


# steer, gas, brake
def generate_data_action(t, prev_action):
    # action = env.action_space.sample()
    # return action

    # accelerate at beginning
    if t < 50:
        return np.array([0, 1, 0])

    # stick with an action for a few time steps
    if t % 5 > 0:
        return prev_action

    # choose a random discrete action
    rn = random.randint(0, 9)
    # Coast
    if rn in [0]:
        return np.array([0, 0, 0])
    # Accelerate straight
    if rn in [1, 2, 3, 4, 5]:
        return np.array([0, random.random(), 0])
    # Turn left
    if rn in [6, 7]:
        return np.array([-random.random(), 0, 0])
    # Turn right
    if rn in [8]:
        return np.array([random.random(), 0, 0])
    # Brake
    if rn in [9]:
        return np.array([0, 0, random.random()])


def normalize_observation(observation):
    return observation.astype('float32') / 255.


def adjust_obs(obs):
    return normalize_observation(obs)


train_envs = ['car_racing']
test_envs = ['car_racing']
