# Cookiecutter Data Science (with Docker)

The objective of this project is
to bundle together lots of best practice for data science
into a convenient [cookiecutter][cookiecutter] template
that can be use to accelerate the start of your project.

Development (and testing) of projects created with this template are intended to be used with containerisation to keep
local environments clean. Environments can be built locally using [Docker][docker], or [Binder][binder] can be used to generate a multi-user instance of the project.

## Features

- Data directory structure
- Installable Python package for project code
- Invoke tasks for automation
- pytest for Python unit testing
- flake8 and pylint for Python linting
- Dockerfile with jupyter notebook and python installation
- black for automatic Python code formatting
- Comprehensive suggested stack of Python 3.7 data science libraries
- gitignore for Python
- binder support
- pre-commit hooks for code quality

## Using the template

### Requirements

The requirements to use the cookiecutter template are:

- Python >= 3.6
- Python packages (See [`requirements.txt`](requirements.txt)):
  - [cookiecutter][cookiecutter-install] >= 1.6.0 (from PyPI or conda-forge)

**These requirements are independent of the project that will use the template.**

The simplest way to install the required Python packages
is to download the [`requirements.txt`](requirements.txt) file from this repository
and install with pip, either globally or in an isolated environment:

``` bash
python -m pip install -r requirements.txt
```

### Starting a new project

To start a new project:

1. Run the following in the directory where you want to create the project.

    ``` bash
    cookiecutter https://github.com/TTitcombe/cookiecutter-data-science
    ```

2. Review project files and amend as required. For example:

    1. Remove files/directories that won't be used.

    2. Rename files/directories to make the purpose more specific.

    3. Review [`setup.py`][project-setup-py] and [`setup.cfg`][project-setup-cfg]
      and update the configuration of the Python code module.
      _NOTE_: you will need to update the project URL.

    4. Review [`tasks/internal.py`][project-tasks-internal]
      and update the settings as required.
      These settings will be used by [invoke][invoke]
      in the automated tasks.

    5. Review [`README.md`][project-readme]
      and update with information on how the project is organised
      and how it will operate,
      such as the sections on set-up and data.

    6. Review [`binder/requirements.txt`][project-docker-requirements] and add or remove packages
      as required.

5. Initialise a git repo and commit all of the files to git,
   excluding the `.gitignore`d files,
   but including the ignored files in `/data`.
   It is recommended to include the template repo URL and commit ID used
   in the commit message for the first commit:
   see below for an example message and
   the generated project [README][project-readme] for the necessary information.
   Add the project repository as the origin and push the new master branch.

   ```bash
   git init
   git add .
   git add data/* -f
   git commit -m "Initialise project from {URL of cookiecutter repo} at {commit ID}."
   git remote add origin {URL of project repo}
   git push -u origin master
   ```

6. Create a Docker image from the project's [`docker/Dockerfile`][project-dockerfile] by either running
   ```bash
   invoke docker.build-image image_name
   ```
   or 
   ```bash
   docker build --tag=image_name -f docker/Dockerfile .
   ```
   if [`invoke`][invoke] is not installed. `image_name` is the name you wish to give the Docker image.
   
   Alternatively, you can pull an image with `docker pull image_name`.

### Resulting directory structure

The directory structure of your new project is described in the project [README][project-readme].

## Contributing

Contributions are welcome! Just fork the repository, make your updates and open a pull request.

### Installing development requirements

``` bash
python -m pip install -r dev-requirements.txt
```

### Running the cookiecutter tests

``` bash
pytest tests
```

## Background

This template is based on the popular [DrivenData Cookiecutter Data Science][cookiecutter-driven-data]:
_A logical, reasonably standardized, but flexible project structure for doing and sharing data science work._

This builds upon professional experience working on data science projects to provide a versatile template for 
data science.

[project-dockerfile]: %7B%7B%20cookiecutter.repo_name%20%7D%7D/docker/Dockerfile
[project-docker-requirements]: %7B%7B%20cookiecutter.repo_name%20%7D%7D/binder/requirements.txt
[project-readme]: %7B%7B%20cookiecutter.repo_name%20%7D%7D/README.md
[project-setup-py]: %7B%7B%20cookiecutter.repo_name%20%7D%7D/setup.py
[project-setup-cfg]: %7B%7B%20cookiecutter.repo_name%20%7D%7D/setup.cfg
[project-tasks-internal]: %7B%7B%20cookiecutter.repo_name%20%7D%7D/tasks/internal.py

[binder]: https://mybinder.org/
[cookiecutter]: https://cookiecutter.readthedocs.io/
[cookiecutter-install]: https://cookiecutter.readthedocs.org/en/latest/installation.html
[cookiecutter-driven-data]: https://drivendata.github.io/cookiecutter-data-science/
[docker]: https://www.docker.com/
[invoke]: https://www.pyinvoke.org/
