# Zelda-ML
A Machine Learning agent for The Legend of Zelda

Requirements for contribute <br>
-Zelda USA Nes ROM <br>
-Mesen emulator 0.9.9 <br>
<br>
Workflow:
-A cpp application hook the emulator a get the necesary variables. <br>
-Send the variables to a python application using sockets. <br>
-The pyton application using PPO of Stable Baselines 3 train the agent on complete checkpoints until he kill the first boss.
