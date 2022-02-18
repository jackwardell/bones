from pathlib import Path

from setuptools import find_packages
from setuptools import setup

__version__ = "0.1.0"
ROOT_DIR = Path(".")

setup(
    name="magus",
    version=__version__,
    packages=find_packages(),
    include_package_data=True,
    author="Jack",
    author_email="jack@mizar.ai",
    url="https://github.com/jackwardell/magus",
    description="todo",
    long_description="todo",
    long_description_content_type="text/markdown",
    test_suite="tests",
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
        "Natural Language :: English",
        "Intended Audience :: Developers",
    ],
    keywords="python",
    python_requires=">=3.6",
)
