#Cave Solver
This program was created for my Algorithms class at Malone University (fall 2023).
This program takes in a text file of a maze layout (detailed below) and spits out the path to solve the maze or tells the user the maze isn't solvable.

##How does it work?
input: a text file with the following structure

XZX
X A
XXX

Where
'A' = the entrance 
'Z' = the exit
'X' = wall
' ' = path

Output: 
[[1, 2], [1, 1], [0, 1]]

The program does this by transforming the text file into a 2D array and solving it with a depth-first-search

The following line is how the path is found and stored in the "path" variable
path = findPathFromEntranceToExit(loadCaveFromFile('alphacave.txt'))

Feel free to make your own mazes and play around with the code, there is some extra fluff in there from when I was developing it but I'll have that all commented out.