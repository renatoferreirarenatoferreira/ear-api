# EAR-API

Quick and dirty, so :ear: can learn to code.

---

# Working with this project

## Preparing the environment

1. Install Python

Download it from https://www.python.org/ and install.

**It requires version 3.10!**

2. Install Poetry

Make sure that Python installation directory is in your system path.

Run the following script using PowerShell:

`(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -`

3. Install dependencies

Use Poetry to install the dependencies:

`poetry install`

## Run the project

Start uvicorn:

`uvicorn app.main:app --reload`
