# SudokuSolver in Python

DESCRIPTION:
Creates a fully solved sudoku board, randomly inserts blank spaces 
on the board and then solves it again using a backtracking algorithm.

The blank spaces are represented as 0's on the board. By then end of
the program, the program's initial solved board should match the 
board outputted by using the backtrack algorithm.

For example, one output was:

THIS IS THE INITIAL SOLVED BOARD
      1 7 4 |6 3 2 |5 9 8 
      6 3 2 |5 8 9 |1 4 7 
      5 8 9 |1 7 4 |6 2 3 
      -------------------
      9 1 8 |4 6 7 |2 3 5 
      2 5 3 |9 1 8 |4 7 6 
      4 6 7 |2 5 3 |9 8 1 
      -------------------
      7 2 6 |3 9 5 |8 1 4 
      3 9 5 |8 4 1 |7 6 2 
      8 4 1 |7 2 6 |3 5 9 

THIS IS AFTER ADDING EMPTY SPACES
      1 7 0 |6 3 2 |0 0 8 
      6 3 2 |5 0 0 |1 4 0 
      5 0 0 |0 0 4 |0 0 0 
      -------------------
      9 0 0 |0 6 7 |2 3 0 
      2 5 3 |0 1 0 |0 7 6 
      0 6 7 |0 0 3 |0 0 1 
      -------------------
      7 2 6 |3 9 5 |8 1 4 
      3 9 5 |8 4 1 |7 6 2 
      8 4 1 |7 2 6 |3 5 9 

SOLVED BOARD USING BACKTRACK ALGORITHM
      1 7 4 |6 3 2 |5 9 8 
      6 3 2 |5 8 9 |1 4 7 
      5 8 9 |1 7 4 |6 2 3 
      -------------------
      9 1 8 |4 6 7 |2 3 5 
      2 5 3 |9 1 8 |4 7 6 
      4 6 7 |2 5 3 |9 8 1 
      -------------------
      7 2 6 |3 9 5 |8 1 4 
      3 9 5 |8 4 1 |7 6 2 
      8 4 1 |7 2 6 |3 5 9

