import pytest

import {{ cookiecutter.module_name }}


def test_version():
    assert hasattr({{ cookiecutter.module_name }}, '__version__')
    assert {{ cookiecutter.module_name }}.__version__ is not None

    # If this fails, then it probably means that the library is not
    # installed via `pip install -e .` or equivalent.
    assert {{ cookiecutter.module_name }}.__version__ != "unknown"
