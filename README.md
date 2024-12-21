[![Python version](https://badgen.net/badge/python/3.10/yellow)](Pipfile)
[![License](https://img.shields.io/github/license/octopusinvitro/bunny)](https://github.com/octopusinvitro/bunny/blob/main/LICENSE.md)
[![Maintainability](https://api.codeclimate.com/v1/badges/0252c4822ca6da42bc60/maintainability)](https://codeclimate.com/github/octopusinvitro/bunny/maintainability)


# README

This project uses `pipenv` for dependency management and `unittest` as a testing framework.


## Setup

The `bin` folder has scripts for basic commands.

Create an environment in your preferred way and then:

```sh
pipenv install
```


## Testing

```sh
. bin/test                    # all tests
. bin/test tests/test_file.py # single test
```


## Linting

```sh
. bin/lint
```
