# A Python Repository Template

This is a template Python repository, including the tools and development aids I use in most of my projects set up and ready to go.

The repository itself can be used as a template by either clicking the "Use this template" button on GitHub, or by using the [GitHub CLI](https://cli.github.com/):

```bash
gh repo create --template "moredatarequired/python-repository-template"
```

## Features

### Packaging and dependency management

- [poetry](https://python-poetry.org/) for dependency management

### Code quality

- [black](https://black.readthedocs.io/en/stable/) for code formatting
- [isort](https://pycqa.github.io/isort/) for sorting imports
- [prospector](https://prospector.landscape.io/en/master/) for static analysis, including:
    - [pylint](https://pylint.org/) for linting
    - [pycodestyle](https://pycodestyle.pycqa.org/en/latest/) for PEP8 compliance
    - [pyflakes](https://pypi.org/project/pyflakes/) for basic syntax errors
    - [mccabe](https://pypi.org/project/mccabe/) for cyclomatic complexity
    - [dodgy](https://pypi.org/project/dodgy/) for security issues
    - [pydocstyle](https://www.pydocstyle.org/en/stable/) for docstring linting
    - [mypy](https://mypy.readthedocs.io/en/stable/) for static type checking
    - [bandit](https://bandit.readthedocs.io/en/latest/) for security linting
    - [vulture](https://pypi.org/project/vulture/) for unused code detection


### Testing

- [pytest](https://docs.pytest.org/en/stable/) for testing

### Automation

- [pre-commit](https://pre-commit.com/) for linting and formatting

## Steps to recreate

Especially if you just want only some of these tools, or if you want to apply them to a repository that already exists, here are the steps I took to set up this repository.

### Initialize a new poetry project

```bash
poetry new python-repository-template
cd python-repository-template
poetry shell
```

### Create a new repository

```bash
gh repo create "moredatarequired/python-repository-template" --public --description "A Python Repository Template" --license unlicense --source=.
git push --set-upstream origin main
git add .
git commit -m "Initialize repository with poetry"
git push
```

### Add pre-commit

```bash
poetry add pre-commit --group dev
```

Create a [`.pre-commit-config.yaml`](.pre-commit-config.yaml) file with the following contents:

```yaml
repos:
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v2.3.0
    hooks:
      - id: check-added-large-files
      - id: check-ast
      - id: check-builtin-literals
      - id: check-byte-order-marker
      - id: check-case-conflict
      - id: check-docstring-first
      - id: check-json
      - id: check-merge-conflict
      - id: check-toml
      - id: check-vcs-permalinks
      - id: check-yaml
      - id: detect-aws-credentials
      - id: detect-private-key
      - id: end-of-file-fixer
      - id: name-tests-test
      - id: trailing-whitespace
```

Install pre-commit and run against all files:

```bash
pre-commit install
pre-commit run --all-files
```

### Add black and isort

```bash
poetry add black[jupyter] blacken-docs isort --group dev
```

Add the following to [`pyproject.toml`](pyproject.toml):
```toml
[tool.isort]
profile = "black"
```

And extend the pre-commit config to include black and isort:

```yaml
  - repo: https://github.com/psf/black
    rev: 22.8.0
    hooks:
      - id: black-jupyter
        language_version: python3.10
  - repo: https://github.com/asottile/blacken-docs
    rev: v1.12.1
    hooks:
      - id: blacken-docs
        additional_dependencies: [black==22.8.0]
  - repo: https://github.com/pycqa/isort
    rev: 5.10.1
    hooks:
      - id: isort
        name: isort (python)
```

### Add prospector

```bash
poetry add prospector[with_bandit,with_mypy,with_vulture] --group dev
```

And extend the pre-commit config to include prospector:

```yaml
  - repo: https://github.com/PyCQA/prospector
    rev: 1.7.5
    hooks:
    -   id: prospector
        additional_dependencies:
        - ".[with_bandit,with_mypy,with_vulture]"
```

## TODO

### Testing

- [coverage](https://coverage.readthedocs.io/en/stable/) for measuring test coverage

### Documentation

- [sphinx](https://www.sphinx-doc.org/en/master/) for documentation
- [sphinx-rtd-theme](https://sphinx-rtd-theme.readthedocs.io/en/stable/) for documentation theme
- [readthedocs](https://readthedocs.org/) for documentation hosting

### Automation

- [GitHub Actions](https://docs.github.com/en/actions) for CI/CD

## FAQ

### Why not use [cookiecutter](https://pypi.org/project/cookiecutter/)?

This absolutely could have been a cookiecutter template, but it was more important to me to create a working demo respository and document the steps I took to set it up. I may create a cookiecutter template in the future, and if I do, I'll link to it here.

## See also

[hypermodern-python](https://github.com/cjolowicz/hypermodern-python) with the associated [guide](https://cjolowicz.github.io/posts/hypermodern-python-01-setup/) is a more in-depth setup guide. The tool chain Claudio chooses is a bit different than mine, but is an excellent set of choices. Claudio Jolowicz has also written a [cookiecutter template](https://github.com/cjolowicz/cookiecutter-hypermodern-python) that implements the guide, which is maybe even easier to use.
