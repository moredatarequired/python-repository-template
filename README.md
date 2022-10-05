# A Python Repository Template

This is a template Python repository, including the tools and development aids I use in most of my projects set up and ready to go.

The repository itself can be used as a template by either clicking the "Use this template" button on GitHub, or by using the [GitHub CLI](https://cli.github.com/):

```bash
gh repo create --template "moredatarequired/python-repository-template"
```

## Features

- [poetry](https://python-poetry.org/) for dependency management
- [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
- [black](https://black.readthedocs.io/en/stable/) for code formatting
- [isort](https://pycqa.github.io/isort/) for sorting imports
- [flake8](https://flake8.pycqa.org/en/latest/) for linting
- [bandit](https://bandit.readthedocs.io/en/latest/) for security linting
- [pytest](https://docs.pytest.org/en/stable/) for testing
- [coverage](https://coverage.readthedocs.io/en/stable/) for measuring test coverage
- [sphinx](https://www.sphinx-doc.org/en/master/) for documentation
- [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/) for documentation theme
- [readthedocs](https://readthedocs.org/) for documentation hosting
- [pre-commit](https://pre-commit.com/) for linting and formatting
- [GitHub Actions](https://docs.github.com/en/actions) for CI/CD

## Steps to recreate

Especially if you just want only some of these tools, or if you want to apply them to a repository that already exists, here are the steps I took to set up this repository.

### Initialize a new poetry project

```bash
poetry new python-repository-template
cd python-repository-template
```

### Create a new repository

```bash
gh repo create "moredatarequired/python-repository-template" --public --description "A Python Repository Template" --license unlicense --source=.
git push --set-upstream origin main
git add .
git commit -m "Initialize repository with poetry"
git push
```
