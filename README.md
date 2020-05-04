# How to use
- clone the program
- open the command line
- `cd 505_puzzle`
- Enter `python puzzle.py 1 4 2 6 3 5 _ 7 8`
- You will see the output of normal A* search, with the sum of the Manhattan distances of each square from its
current to its goal position as heuristic
- However, you can change the mode to "zero mode" with 0 as heuristic by adding a "zero" in the beginning of parameters. For example `python puzzle.py 1 4 2 6 3 5 _ 7 8`
