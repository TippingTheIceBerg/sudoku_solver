# sudoku_solver
A fun solver for when I was stuck in a game
To play, there is typically a  9 x 9 grid where numbers do not repeat in the rows, verticals, or in a square 3 x 3
every square has 9 possible numbers.
try all numbers, and find one that works that doesn't break the rules.
then repeat this rule. 
As soon as we get to the last number, and it turns out the last number is not a valid number, but is the only number left, we must now perform backtracking, which is, the last number we go to the number before that one, and continue the search starting off where that number started off, and if it reaches 9 and doesn't work, we will do it again. IE

last two was a 6 and 8. 8 fails, we remove 8, , go to space 6, and try 7,8,9, if that fails we go to the one before 6, and do the same process, if a new number is found here, we start the beginning processs starting at 1 and seeing if any of the numbers match

first thing, pick an empty square, loop through for empty or 0
second, for each square, we need to see if the number is valid after placing a number into the space
third, if not valid, we backtrack