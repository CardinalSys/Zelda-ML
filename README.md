# Zelda-ML
A Machine Learning agent for The Legend of Zelda

<strong>For make a pull request do it to the "develop" branch</strong>

Requirements for contribute <br>
-Zelda USA Nes ROM <br>
-Mesen emulator 0.9.9 <br>
<br>
Workflow: <br>
-A cpp application hook the emulator a get the necesary variables. <br>
-Send the variables to a python application using sockets. <br>
-The pyton application using PPO of Stable Baselines 3 train the agent on complete checkpoints until he kill the first boss. <br>
<br>
Useful links: <br>
https://datacrystal.romhacking.net/wiki/The_Legend_of_Zelda:RAM_map
