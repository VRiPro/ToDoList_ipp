"""
This script is used for package setup and distribution of the ToDoList library.

The ToDoList library is a comprehensive Python package that allows users to
create and manage personal tasks. It is designed based on the concepts covered
in the Kit for Big Data course.

Package Information:
- Name: ToDoList
- Version: 1.0.0

Authors:
- Ahmed Belaaj
- Nour Ben Rejeb
- Victor Rivière
- Mathieu Sauveur

Dependencies:
- pytest (required for testing)

For more information and usage instructions, please refer to the
package documentation.

"""

from setuptools import setup, find_packages

setup(
    name="ToDoList",
    version="1.0.0",
    description="""A comprehensive Python library for creating and managing
    personal tasks using concepts covered in the Kit for Big Data course.""",
    author="Ahmed Belaaj, Nour Ben Rejeb, Victor Rivière, Mathieu Sauveur",
    packages=find_packages(),
    install_requires=[
        "pytest"
    ],
)
