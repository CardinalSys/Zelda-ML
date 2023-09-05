from subprocess import Popen, PIPE
import gymnasium as gym
import numpy as np
from gymnasium import spaces
import time

playerXPos = 0
playerYPos = 0
playerDir = 0
playerMapLocation = 0
previousPlayerMapLocation = 0
playerLife = 0

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

p = Popen(['D:\\projects\\ZeldaML\\ZeldaHook\\x64\\Debug\\ZeldaHook.exe'], shell=True, stdout=PIPE, stdin=PIPE)

class ZeldaEnv(gym.Env):
    """Custom Environment that follows gym interface."""

    metadata = {"render_modes": ["human"], "render_fps": 60}

    def __init__(self):
        super(ZeldaEnv, self).__init__()
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(7)
        # Example for using image as input (channel-first; channel-last also works):
        self.observation_space = spaces.Box(low=0, high=255,
                                            shape=(31,), dtype=np.int32)

    def step(self, action):
        
        result = p.stdout.readline().strip()
        print(result)
        result = result.decode('utf-8')
        result = result.replace('Player:', '').replace('Enemies:', '')

        numbers = result.split(';')

        playerXPos = numbers[0]
        playerYPos = numbers[1]
        playerDir = numbers[2]
        playerMapLocation = numbers[3]
        playerLife = numbers[4]

        enemy1xPos = numbers[5]
        enemy2xPos = numbers[6]
        enemy3xPos = numbers[7]
        enemy4xPos = numbers[8]
        enemy5xPos = numbers[9]
        enemy6xPos = numbers[10]

        enemy1xPos = numbers[11]
        enemy2yPos = numbers[12]
        enemy3yPos = numbers[13]
        enemy4yPos = numbers[14]
        enemy5yPos = numbers[15]
        enemy6yPos = numbers[16]

        enemy1Dir = numbers[17]
        enemy2Dir = numbers[18]
        enemy3Dir = numbers[19]
        enemy4Dir = numbers[20]
        enemy5Dir = numbers[21]
        enemy6Dir = numbers[22]

        enemy1xProjectil = numbers[23]
        enemy2xProjectil = numbers[24]
        enemy3xProjectil = numbers[25]
        enemy4xProjectil = numbers[26]

        enemy1yProjectil = numbers[27]
        enemy2yProjectil = numbers[28]
        enemy3yProjectil = numbers[29]
        enemy4yProjectil = numbers[30]

        # do whatever you do

        if action == 0:
            p.stdin.write(b"1\n")
        elif action == 1:
            p.stdin.write(b"2\n")
        elif action == 2:
            p.stdin.write(b"4\n")
        elif action == 3:
            p.stdin.write(b"8\n")
        elif action == 4:
            p.stdin.write(b"16\n")
        elif action == 5:
            p.stdin.write(b"64\n")
        elif action == 6:
            p.stdin.write(b"128\n")
   
        
        print(int(playerLife))

        self.reward = 0
        
        p.stdin.flush()
        self.terminated = False
        if int(playerLife) <= 0:
            self.terminated = True

        if self.terminated:
            self.reward = -10
        elif int(playerMapLocation) - 66 < int(previousPlayerMapLocation) - 66:
            self.reward += 1
        
        
            
        self.truncated = False
        info = {}

        self.observation = [playerXPos, playerYPos, playerDir, playerMapLocation, playerLife, enemy1xPos, enemy2xPos, enemy3xPos, enemy4xPos,
                             enemy5xPos, enemy6xPos, enemy1yPos, enemy2yPos, enemy3yPos, enemy4yPos, enemy5yPos, enemy6yPos,
                             enemy1Dir, enemy2Dir, enemy3Dir, enemy4Dir, enemy5Dir, enemy6Dir, enemy1xProjectil, enemy2xProjectil,
                             enemy3xProjectil, enemy4xProjectil, enemy1yProjectil, enemy2yProjectil, enemy3yProjectil, enemy4yProjectil]
        
        self.observation = [int(x) for x in self.observation]
        self.observation = np.array(self.observation)

        return self.observation, self.reward, self.terminated, self.truncated, info

    def reset(self, seed=None, options=None):
        self.done = False
        p.stdin.write(b"99\n")
        result = p.stdout.readline().strip()
        print(result)
        result = result.decode('utf-8')
        result = result.replace('Player:', '').replace('Enemies:', '')

        numbers = result.split(';')

        playerXPos = numbers[0]
        playerYPos = numbers[1]
        playerDir = numbers[2]
        playerMapLocation = numbers[3]
        playerLife = numbers[4]

        enemy1xPos = numbers[5]
        enemy2xPos = numbers[6]
        enemy3xPos = numbers[7]
        enemy4xPos = numbers[8]
        enemy5xPos = numbers[9]
        enemy6xPos = numbers[10]

        enemy1xPos = numbers[11]
        enemy2yPos = numbers[12]
        enemy3yPos = numbers[13]
        enemy4yPos = numbers[14]
        enemy5yPos = numbers[15]
        enemy6yPos = numbers[16]

        enemy1Dir = numbers[17]
        enemy2Dir = numbers[18]
        enemy3Dir = numbers[19]
        enemy4Dir = numbers[20]
        enemy5Dir = numbers[21]
        enemy6Dir = numbers[22]

        enemy1xProjectil = numbers[23]
        enemy2xProjectil = numbers[24]
        enemy3xProjectil = numbers[25]
        enemy4xProjectil = numbers[26]

        enemy1yProjectil = numbers[27]
        enemy2yProjectil = numbers[28]
        enemy3yProjectil = numbers[29]
        enemy4yProjectil = numbers[30]
        p.stdin.flush()
        self.observation = [playerXPos, playerYPos, playerDir, playerMapLocation, playerLife, enemy1xPos, enemy2xPos, enemy3xPos, enemy4xPos,
                             enemy5xPos, enemy6xPos, enemy1yPos, enemy2yPos, enemy3yPos, enemy4yPos, enemy5yPos, enemy6yPos,
                             enemy1Dir, enemy2Dir, enemy3Dir, enemy4Dir, enemy5Dir, enemy6Dir, enemy1xProjectil, enemy2xProjectil,
                             enemy3xProjectil, enemy4xProjectil, enemy1yProjectil, enemy2yProjectil, enemy3yProjectil, enemy4yProjectil]
        
        self.observation = [int(x) for x in self.observation]
        self.observation = np.array(self.observation)
        info = {}
        return self.observation, info



def GetVariables():
    result = p.stdout.readline().strip()
    print(result)
    result = result.decode('utf-8')
    result = result.replace('Player:', '').replace('Enemies:', '')

    numbers = result.split(';')

    playerXPos = numbers[0]
    playerYPos = numbers[1]
    playerDir = numbers[2]
    playerMapLocation = numbers[3]
    playerLife = numbers[4]

    enemy1xPos = numbers[5]
    enemy2xPos = numbers[6]
    enemy3xPos = numbers[7]
    enemy4xPos = numbers[8]
    enemy5xPos = numbers[9]
    enemy6xPos = numbers[10]

    enemy1xPos = numbers[11]
    enemy2yPos = numbers[12]
    enemy3yPos = numbers[13]
    enemy4yPos = numbers[14]
    enemy5yPos = numbers[15]
    enemy6yPos = numbers[16]

    enemy1Dir = numbers[17]
    enemy2Dir = numbers[18]
    enemy3Dir = numbers[19]
    enemy4Dir = numbers[20]
    enemy5Dir = numbers[21]
    enemy6Dir = numbers[22]

    enemy1xProjectil = numbers[23]
    enemy2xProjectil = numbers[24]
    enemy3xProjectil = numbers[25]
    enemy4xProjectil = numbers[26]

    enemy1yProjectil = numbers[27]
    enemy2yProjectil = numbers[28]
    enemy3yProjectil = numbers[29]
    enemy4yProjectil = numbers[30]

    p.stdin.flush()

