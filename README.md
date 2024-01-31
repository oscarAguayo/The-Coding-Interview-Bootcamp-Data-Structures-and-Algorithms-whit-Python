# The Coding Interview Bootcamp Data Structures and Algorithms with Python

This is a "fork" repo from [https://github.com/StephenGrider/AlgoCasts](https://github.com/StephenGrider/AlgoCasts) but with exercises in Python instead Javascript.

## Instructions

### Clone the repo

```shell
git clone https://github.com/oscarAguayo/The-Coding-Interview-Bootcamp-Data-Structures-and-Algorithms-with-Python.git
```

### Create and activate virtual environment

Set virtual environment with `python -m venv venv`.

Activate virtual environment (linux and macOS):

```shell
source venv/bin/activate
```

### Install dependencies

```shell
(venv) $ pip install -r requirements.txt
```

## Exercises

The exercises will be enumerated in the root folder. Inside each folder will be have a `main.py` file with instructions inside comments and `test_main.py` file, with the test functions necessary to validate the solution.

### Solving exercises

Each exercise contain a `main.py` file with functions with `pass` statements, you need to implement the solution to solve the specified problem in comments.

Each `main.py` can be executed to test the solution with

```shell
(venv) $ python <folder_exercise>/main.py
```

But this is only for test inside the file, the real test will be made like specified in the next section.

### Run tests

To validate the solution of the problem, you will be run specific test with

```shell
(venv) $ pytest <folder_exercise>/test_main.py
```

Or you can execute all tests with

```shell
(venv) $ pytest
```

## Branches

The project will have two branches, the `main` branch is where the exercises are, and you will implemented the solution to each exercise. And the `solutions` branch is where the solutions are will be. Don't cheat, try to solve yourself each exercise.

Happy coding!
