import os
import pathlib

import pytest


@pytest.fixture(scope="function")
def in_tmp_dir(tmp_path_factory) -> pathlib.Path:
    current_dir = os.getcwd()
    tmp_dir = tmp_path_factory.mktemp("project")
    os.chdir(tmp_dir)
    yield tmp_dir
    os.chdir(current_dir)
