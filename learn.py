import time
import gymnasium as gym
from env import ZeldaEnv
from stable_baselines3 import PPO
from stable_baselines3.common.env_util import make_vec_env

# Parallel environments
vec_env = ZeldaEnv()
logdir = f"logs/{int(time.time())}/"
model = PPO('MlpPolicy', vec_env, verbose=1, tensorboard_log=logdir)
model.learn(total_timesteps=25000)
model.save(f"models/{int(time.time())}/")


obs = vec_env.reset()
while True:
    action, _states = model.predict(obs)
    obs, rewards, dones, info = vec_env.step(action)
    vec_env.render("human")