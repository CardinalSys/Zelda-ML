from stable_baselines3.common.env_checker import check_env
from run import ZeldaEnv

env = ZeldaEnv()

episodes = 50

for episode in range(episodes):
	done = False
	obs = env.reset()
	while True:#not done:
		random_action = env.action_space.sample()
		obs, reward, truncated, terminated, info = env.step(random_action)