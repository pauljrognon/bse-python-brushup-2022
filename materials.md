---
title: Materials
---
{% include navigation.html %}

On this page I will be posting and updating lectures, exercises and materials for the current year brushup.

## How to complete the tests
To complete the test:  
1. Accept the assignment.
2. Clone the repository to your local machine using `git clone`.
3. Complete the exercises\[.R / .py\] script.
4. Add, commit and push your changes using `git` commands.
5. Check that your push is successful. 
6. **IMPORTANT** Check that the autograder graded your submission correctly!!! Do not leave any leftovers in your scripts (like variables you added to check the correctness of your functions etc.)!!! To see the autograder feedback and logs, open the "Actions" tab in your GitHub repo. You will see a "workflow" with a message of your commit, just click on it and there you will find your grade and a button that says "Autograding". If you want to see more informative logs, just click on this button.  
Only the latest push before the deadline is taken into account!

*ATTENTION:* do not use `setwd()` in your code in R.

## Shell (Command Line Interfaces)
Have a look at the shell exercises [here](https://classroom.github.com/a/3d8BeanH). 

The repo contains 3 folders corresponding to different assignments, one handout "handout_bash.html", and one ".gitignore" file (it makes git to omit several files from consideration at all). In the handout you can find a lot of information not only about Bourne again Shell, but also about Git and GitHub, and Servers.

Solutions: [scripting](./docs/shell-solutions/scripting.tar.gz), [whodunit](./docs/shell-solutions/whodunit-solution.sh).

## Python
### Lectures
Class 1: [Introduction, Variables, Basic Data Types, Expressions, Comparisons](./docs/python-lectures/class_1.ipynb)  
Class 2: [Functions, Catching Exceptions](./docs/python-lectures/class_2.ipynb); [Conditionals and Raising Exceptions](./docs/python-lectures/class_2_conditionals.html)  
Class 3: [Sequence Types, Loops, List Comprehensions, Dictionaries, Set Types](./docs/python-lectures/class_3.ipynb)  
Class 4: [Handling Parameters: zip, itertools, Handling Functions: map, lambda](./docs/python-lectures/class_4.ipynb); [Object Oriented Programming in Python](./docs/python-lectures/class_4_oop.html); [Script: Car Example](./docs/python-lectures/class_4_oop_example.py)  
Class 5: [OOP (cont'd) and Modules](./docs/python-lectures/class_5_oop_modules.tar.gz); [JSON, numpy, pandas](./docs/python-lectures/class_5_json_pandas.ipynb)

### Exercises
[Hello World](./python/python-1-hello-world.md),[Functions](https://classroom.github.com/a/dAjlnfKT) ([solution](./docs/python-solutions/python-functions-solution.py)), [Conditionals](https://classroom.github.com/a/Yow3m5e2) ([solution](./docs/python-solutions/python-conditionals-solution.py)), [Loops](https://classroom.github.com/a/ShzbLvYq) ([solution](./docs/python-solutions/python-loops-solution.py)), [Dictionaries](https://classroom.github.com/a/ZuujAbfK) ([solution](./docs/python-solutions/python-dictionaries-solution.py)), [Classes](https://classroom.github.com/a/Kuke8ppB) ([solution](./docs/python-solutions/python-classes-solution.py)), [JSON](https://classroom.github.com/a/mWPvThPo) ([solution tweet_data.py](./docs/python-solutions/python-json-tweet-data-solution.py), [solution exercises.py](./docs/python-solutions/python-json-solution.py)).

Extra materials on Pandas: [Intro](https://classroom.github.com/a/sTKrRW90), [Grouping](https://classroom.github.com/a/_c0BuLuZ), [Project](https://classroom.github.com/a/19jd2Tx8). I recommend you to complete these assignments since it will help you to get comfortable with Pandas. There are also some notebooks with tutorial materials for pandas. I will do a coding review for these assignments upon requests.

### Test Python
Complete the test: ["Python: Test"](https://classroom.github.com/a/369Bl5Gk)  
Deadline: 20/09/22 23:59  
Grading: each exercise gives 10 points  
Passing grade: 60 / 110

## R
All the main materials are incorporated into a GitHub Classroom assignment: ["R: Tutorial"](https://classroom.github.com/a/j3WyUiaa). 

You can find the in-class handouts there together with some practical exercises. For more information, please read the README file in the repo.

You can access the materials on linear models in R from [this archive](./docs/Rextra.tar.gz).

### Test R
Complete the test: ["R: Test"](https://classroom.github.com/a/tJNTB1Bx)  
Deadline: 20/09/22 23:59  
Grading: each exercise gives 10 points  
Passing grade: 50 / 100