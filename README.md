# Zelda-ML
A Machine Learning agent for The Legend of Zelda

Requirements for contribute <br>
-Zelda USA Nes ROM <br>
-Mesen emulator 0.9.9 <br>
-For cpp application: Visual Studio 2022 Desktop Develpment with C++ <br>
-For python: just python, I use 3.8.2. Required version > 3.6 <br>
<br>
Workflow: <br>
-A cpp application hooks the emulator a get the necesary variables. <br>
-Send the variables to a python application using sockets. <br>
-The pyton application using PPO of Stable Baselines 3 trains the agent on complete checkpoints until he kills the first boss. <br>
<br>
Useful links: <br>
https://datacrystal.romhacking.net/wiki/The_Legend_of_Zelda:RAM_map
