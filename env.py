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
currentSword = 0

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
        self.previousPlayerMapLocation = 0
        # Define action and observation space
        # They must be gym.spaces objects
        # Example when using discrete actions:
        self.action_space = spaces.Discrete(6)
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
        currentSword = numbers[5]

        enemy1xPos = numbers[6]
        enemy2xPos = numbers[7]
        enemy3xPos = numbers[8]
        enemy4xPos = numbers[9]
        enemy5xPos = numbers[10]
        enemy6xPos = numbers[11]

        enemy1xPos = numbers[12]
        enemy2yPos = numbers[13]
        enemy3yPos = numbers[14]
        enemy4yPos = numbers[15]
        enemy5yPos = numbers[16]
        enemy6yPos = numbers[17]

        enemy1Dir = numbers[18]
        enemy2Dir = numbers[19]
        enemy3Dir = numbers[20]
        enemy4Dir = numbers[21]
        enemy5Dir = numbers[22]
        enemy6Dir = numbers[23]

        enemy1xProjectil = numbers[24]
        enemy2xProjectil = numbers[25]
        enemy3xProjectil = numbers[26]
        enemy4xProjectil = numbers[27]

        enemy1yProjectil = numbers[28]
        enemy2yProjectil = numbers[29]
        enemy3yProjectil = numbers[30]
        enemy4yProjectil = numbers[31]

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
            p.stdin.write(b"64\n")
        elif action == 5:
            p.stdin.write(b"128\n") 
        

        self.reward = 0
        
        p.stdin.flush()
        self.terminated = False
        if int(playerLife) <= 0:
            self.terminated = True


        
            
        self.truncated = False
        info = {}

        self.observation = [playerXPos, playerYPos, playerDir, playerMapLocation, playerLife, currentSword, enemy1xPos, enemy2xPos, enemy3xPos, enemy4xPos,
                             enemy5xPos, enemy6xPos, enemy1yPos, enemy2yPos, enemy3yPos, enemy4yPos, enemy5yPos, enemy6yPos,
                             enemy1Dir, enemy2Dir, enemy3Dir, enemy4Dir, enemy5Dir, enemy6Dir, enemy1xProjectil, enemy2xProjectil,
                             enemy3xProjectil, enemy4xProjectil, enemy1yProjectil, enemy2yProjectil, enemy3yProjectil, enemy4yProjectil]
        
        self.observation = [int(x) for x in self.observation]
        self.observation = np.array(self.observation)

        print(int(playerMapLocation) - 100)
        print(int(self.previousPlayerMapLocation) - 100)

        if int(playerMapLocation) - 100 < int(self.previousPlayerMapLocation) - 100:
            self.reward += 1
        if int(playerMapLocation) == 100:
            self.close()

        if self.terminated:
            self.reward = -5
            observation = self.reset()
            return observation, self.reward, self.terminated, self.truncated, info
    
        self.previousPlayerMapLocation = playerMapLocation

        print(self.reward)
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
        currentSword = numbers[5]

        enemy1xPos = numbers[6]
        enemy2xPos = numbers[7]
        enemy3xPos = numbers[8]
        enemy4xPos = numbers[9]
        enemy5xPos = numbers[10]
        enemy6xPos = numbers[11]

        enemy1xPos = numbers[12]
        enemy2yPos = numbers[13]
        enemy3yPos = numbers[14]
        enemy4yPos = numbers[15]
        enemy5yPos = numbers[16]
        enemy6yPos = numbers[17]

        enemy1Dir = numbers[18]
        enemy2Dir = numbers[19]
        enemy3Dir = numbers[20]
        enemy4Dir = numbers[21]
        enemy5Dir = numbers[22]
        enemy6Dir = numbers[23]

        enemy1xProjectil = numbers[24]
        enemy2xProjectil = numbers[25]
        enemy3xProjectil = numbers[26]
        enemy4xProjectil = numbers[27]

        enemy1yProjectil = numbers[28]
        enemy2yProjectil = numbers[29]
        enemy3yProjectil = numbers[30]
        enemy4yProjectil = numbers[31]
        p.stdin.flush()
        self.observation = [playerXPos, playerYPos, playerDir, playerMapLocation, playerLife, currentSword, enemy1xPos, enemy2xPos, enemy3xPos, enemy4xPos,
                             enemy5xPos, enemy6xPos, enemy1yPos, enemy2yPos, enemy3yPos, enemy4yPos, enemy5yPos, enemy6yPos,
                             enemy1Dir, enemy2Dir, enemy3Dir, enemy4Dir, enemy5Dir, enemy6Dir, enemy1xProjectil, enemy2xProjectil,
                             enemy3xProjectil, enemy4xProjectil, enemy1yProjectil, enemy2yProjectil, enemy3yProjectil, enemy4yProjectil]
        
        self.observation = [int(x) for x in self.observation]
        self.observation = np.array(self.observation)
        info = {}
        return self.observation, info
