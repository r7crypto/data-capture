### Data Capture for Team International

This test was coded with python 3, without using any external library,
I left a main.py file with the steps indicated on the test document provided
by you.

Some unit tests where added.

The build_stats method could have some O(n2) time complexity to get the main 
'less, greater and between' processes, but dictionaries where used due to the
fact that this data structures are O(1) avoiding the use of lists that could 
be increasing the time complexity.

I omit the requirements file and all the 'cookiecutter' stuff, to maintain this
test straightforward.