# A* Maze Solver
Create your own mazes and watch them be solved in real-time using the A* maze solving algorithm

![](preview.gif)

## Installation
Install python and install the pygame library by running;

```pip install pygame```

## Quickstart
```python astar.py FILENAME [-optional]```

To run the demo maze shown run;

```python astar.py mazes/maze2.txt```

---

## Customisation
Values for the maze program can be changed in the config file & passed as optional parameters.

The properties that can be changed in `astar.ini` are;

- **Size**; The size of the window in pixels
- **Speed**; The speed the solving executes at
- **Colours**; Colours for all the screen elements can be customised in the format `R,G,B`

Size & Speed can also be overwridden as arguments by adding `-Size ___` and `-Speed ___` to the end of the `python astar.py FILE` command.

---

## A* Explained

A* is a very well known graph traversal algorithm. 

It explores the mazes empty cells, prioritising those that get the player closer to the goal.

These discovered empty cells are typically called 'Nodes' and are assessed in a queue based on their score.

[Here's a good video explaining this process](https://www.youtube.com/watch?v=ySN5Wnu88nE)

---

## How to create your own maze
Mazes are defined as text files with different characters representing different cells.

- `o` = Empty space
- `x` = Wall 
- `s` = Start
- `e` = End

For example the following text file;

```
sxe
oxo
ooo
```

Would produce the following maze;

![](maze.png)

More examples can be found in the mazes folder.

---

## Code Walkthrough

- **Graphics**
    - **Window:** Class for the pygame screen 
    - **Grid:** Classes for rendering cells & the grid and storing their colours/ values
- **AStar_Logic**
    - **Components:** Classes used in the A* structure
        - CellType: Enum for values representing different cell types
        - Node: Represents discovered cell in the maze & its score
        - PriorityQueue: Orders the nodes & prioritises them based on score
    - **Maze:** Stores the grid & player/ goal positions
    - **Decision_Handler:** Implements the A* decision making updating the node queue and current position
- **Tools**
    - **Load_Arguments:** Loads configuration from ini file and command line
    - **Load_Maze:** Loads the maze from the given text file
    - **Vector:** Class representing a position with helper methods
