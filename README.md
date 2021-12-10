# Tic Tac Toe
[![PyTest](https://github.com/msgross/tic-tac-toe/actions/workflows/pytest.yml/badge.svg)](https://github.com/msgross/tic-tac-toe/actions/workflows/pytest.yml) [![Pylint](https://github.com/msgross/tic-tac-toe/actions/workflows/pylint.yml/badge.svg)](https://github.com/msgross/tic-tac-toe/actions/workflows/pylint.yml) [![codecov](https://codecov.io/gh/msgross/tic-tac-toe/branch/main/graph/badge.svg?token=STQ2O7WIGC)](https://codecov.io/gh/msgross/tic-tac-toe)

## Overview
Standard game of 3x3 tic-tac-toe, aim for 3 in a row.

## How To Use
This project is maintained in [Poetry](https://python-poetry.org/).

Pull down the project and run the following within the directory
```
poetry install 
```
to grab the dependencies
```
poetry build
```
to build the wheel file
## Notes
This implementation just maintains the state as a bit-state per player. Defined in two bytes over 9 squares, and 
do some bit operations to figure out potential win conditions and current state. The initial go at this was going 
to make use of numpy arrays with masks, but no need to add complexity to a simple problem

## Possible Extensions
An *n* x *n* game where the rule is still 3 in a row might be fun to implement, in which case these rules would 
essentially represent a frame, and we'd crawl over the grid and see if any victory conditions are available. 
We'd need to make the scoring more flexible or open to variability than it is. 

