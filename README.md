# Neuro 140 Final Report: Variations on examining impact of changing transition function in Deep RL

# Running the code:
Run a model on `trickyClassic.lay` layout for 20,000 episodes, of which 10,000 episodes are used for training.

Shell command:
```
$ python3 pacman.py -p PacmanDQN -n 20,000 -x 10,000 -l trickyClassic
```

# Layouts
Different layouts in `layouts` directory

# Parameters
* Parameters in the `params` dictionary in `pacmanDQN_Agents.py`.
* Models are saved as "checkpoint" files in the `/saves` directory.
* Load and save filenames can be set using the `load_file` and `save_file` parameters.


# Acknowledgements
Deep Reinforcement Learning in Pac-man
* [van der Ouderaa, Tycho (2016). Deep Reinforcement Learning in Pac-man.](https://moodle.umons.ac.be/pluginfile.php/404484/mod_folder/content/0/Pacman_DQN.pdf)

DQN Framework by  (made for ATARI / Arcade Learning Environment)
* [deepQN_tensorflow](https://github.com/mrkulk/deepQN_tensorflow) ([https://github.com/mrkulk/deepQN_tensorflow](https://github.com/mrkulk/deepQN_tensorflow))

Pac-man implementation by UC Berkeley:
* [The Pac-man Projects - UC Berkeley](http://ai.berkeley.edu/project_overview.html) ([http://ai.berkeley.edu/project_overview.html](http://ai.berkeley.edu/project_overview.html))
