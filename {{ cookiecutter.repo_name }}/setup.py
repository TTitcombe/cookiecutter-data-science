from setuptools import setup

# Metadata in setup.cfg
setup(use_scm_version={"write_to": "src/{{ cookiecutter.module_name }}/_version.py"})
