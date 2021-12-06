# Contributing

Feel free to if you want! I don't think there's much to be done, but if you see something that needs to be improved / fixed / added\
by all means, toss a pull request my way. 

## Requirements
* Make sure an issue is opened for the feature / bug / improvement
* Make sure automated tests pass on your branch
    * Don't run down the pylint score, if that action is failing, it's because it's below 8.0 in pylint\
    try to keep the score steady or improve on it
    * Makes sure unit tests still pass (or reflect adjustments if a fix is needed)
    * Make sure test coverage doesn't tank (if it's a new feature, that probably means it needs some unit tests--I use pytest for these,
    refer to the ```tests``` directory to see how those are set up
* Open a pull request and assign it to me to review, note the issue it resolves
* Presumably something else I think of later
