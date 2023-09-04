from subprocess import Popen, PIPE
import gymnasium as gym
import numpy as np
from gymnasium import spaces

playerXPos = 0
playerYPos = 0
playerDir = 0
playerMapLocation = 0

playerBtnPressed = 0

enemy1xPos = 0
enemy2xPos = 0
enemy3xPos = 0
enemy4xPos = 0
enemy5xPos = 0
enemy6xPos = 0

enemy1yPos = 0
enemy2yPos = 0
enemy3yPos = 0
enemy4yPos = 0
enemy5yPos = 0
enemy6yPos = 0

enemy1Dir = 0
enemy2Dir = 0
enemy3Dir = 0
enemy4Dir = 0
enemy5Dir = 0
enemy6Dir = 0

enemy1xProjectil = 0
enemy2xProjectil = 0
enemy3xProjectil = 0
enemy4xProjectil = 0

enemy1yProjectil = 0
enemy2yProjectil = 0
enemy3yProjectil = 0
enemy4yProjectil = 0

class CustomEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 30}

    def __init__(self, arg1, arg2, ...):
        super().__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(N_CHANNELS, HEIGHT, WIDTH), dtype=np.uint8)

    def step(self, action):
        ...
        return observation, reward, terminated, truncated, info

    def reset(self, seed=None, options=None):
        ...
        return observation, info

    def render(self):
        ...

    def close(self):
        ...



p = Popen(['D:\\projects\\ZeldaML\\ZeldaHook\\x64\\Debug\\ZeldaHook.exe'], shell=True, stdout=PIPE, stdin=PIPE)
while True:
    #value = bytes(value, 'UTF-8')  # Needed in Python 3.
    result = p.stdout.readline().strip()
    print(result)
    result = result.decode('utf-8')
    result = result.replace('Player:', '').replace('Enemies:', '')

    numbers = result.split(';')

    playerXPos = numbers[0]
    playerYPos = numbers[1]
    playerDir = numbers[2]
    playerMapLocation = numbers[3]

    enemy1xPos = numbers[4]
    enemy2xPos = numbers[5]
    enemy3xPos = numbers[6]
    enemy4xPos = numbers[7]
    enemy5xPos = numbers[8]
    enemy6xPos = numbers[9]

    enemy1xPos = numbers[10]
    enemy2yPos = numbers[11]
    enemy3yPos = numbers[12]
    enemy4yPos = numbers[13]
    enemy5yPos = numbers[14]
    enemy6yPos = numbers[15]

    enemy1Dir = numbers[16]
    enemy2Dir = numbers[17]
    enemy3Dir = numbers[18]
    enemy4Dir = numbers[19]
    enemy5Dir = numbers[20]
    enemy6Dir = numbers[21]

    enemy1xProjectil = numbers[22]
    enemy2xProjectil = numbers[23]
    enemy3xProjectil = numbers[24]
    enemy4xProjectil = numbers[25]

    enemy1yProjectil = numbers[26]
    enemy2yProjectil = numbers[27]
    enemy3yProjectil = numbers[28]
    enemy4yProjectil = numbers[29]


    
    p.stdin.write(b"8\n")
    p.stdin.flush()

