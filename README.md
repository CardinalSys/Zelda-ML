# Zelda-ML
A Machine Learning agent for The Legend of Zelda

Requirements for contribute
-Zelda USA Nes ROM
-Mesen emulator 0.9.9

Workflow:
-A cpp application hook the emulator a get the necesary variables.
-Send the variables to a python application using sockets.
-The pyton application using PPO of Stable Baselines 3 train the agent on complete checkpoints until he kill the first boss.
