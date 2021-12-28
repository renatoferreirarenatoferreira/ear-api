# EAR-API

Quick and dirty, so :ear: can learn to code.

Project based on [fastapi-realworld-example-app](https://github.com/nsidnev/fastapi-realworld-example-app).

---

# Working with this project

## Preparing the environment

1. Install Python

Download it from https://www.python.org/ and install.

**It requires version 3.10!**

Make sure that all the required modules is installed using the following *pip* syntax:"

`pip install cleo tomlkit poetry.core requests cachecontrol cachy html5lib pkginfo virtualenv lockfile pexpect shellingham`

2. Install Poetry

Make sure that Python installation directory is in your system path.

Run the following script using PowerShell:

`(Invoke-WebRequest -Uri https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py -UseBasicParsing).Content | python -`

3. Install dependencies

Use Poetry to install the dependencies:

`poetry install`

## Running the project

Start Uvicorn:

`uvicorn app.main:app --reload`

## Visual Studio Code integration

When the environment is properly configured, this project must run from *Run / Start Debugging* or by pressing *F5* key.
