import os
import pathlib

import pytest

expected_dirs = [
    '',  # base directory
    'analysis',
    'data',
    'data/external',
    'data/interim',
    'data/processed',
    'data/raw',
    'docs',
    'examples',
    'models',
    'src',
    'src/project_name',
    'tests',
    'tasks',
]
template_files = [
    'README.md',
    'setup.py',
    'setup.cfg',
    '.gitignore',
    'tests/test_about.py',
    'tasks/internal.py',
]


def test_folders(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    baked_project = pathlib.Path(result.project)
    abs_expected_dirs = {baked_project / d for d in expected_dirs}
    abs_observed_dirs = {pathlib.Path(x[0]) for x in os.walk(baked_project)}

    missing_dirs = abs_expected_dirs - abs_observed_dirs
    assert not missing_dirs

    extra_dirs = abs_observed_dirs - abs_expected_dirs
    assert not extra_dirs


def test_no_pinned_environment(cookies):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    # pinned dependencies file not created yet
    baked_project = pathlib.Path(result.project)
    reqs_path = baked_project / 'environment.yml'
    assert not reqs_path.exists()


@pytest.mark.parametrize('filename', template_files)
def test_no_curlies(cookies, filename):
    result = cookies.bake()

    assert result.exit_code == 0
    assert result.exception is None

    # files with known curlies
    baked_project = pathlib.Path(result.project)
    full_path = baked_project / filename

    assert full_path.exists()
    assert no_curlies(full_path)


def no_curlies(filepath):
    """
    Utility to make sure no curly braces appear in a file.
    That is, was jinja able to render everthing?
    """
    with open(filepath, 'r') as f:
        data = f.read()

    template_strings = [
        '{{',
        '}}',
        '{%',
        '%}'
    ]

    template_strings_in_file = [s for s in template_strings if s in data]
    return not template_strings_in_file
