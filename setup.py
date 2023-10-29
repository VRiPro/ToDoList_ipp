from setuptools import setup, find_packages

setup(
    name="ToDoList",
    version="1.0.0",
    description="""Création d'une bibliothèque Python complète pour la
            création et la gestion de tâches personnelles en utilisant
            les notions vues dans le cours de Kit pour le Big Data""",
    author=["Ahmed Belaaj, Nour Ben Rejeb, Victor Rivière, Mathieu Sauveur"],
    packages=find_packages(),
    install_requires=[
        "pytest"
    ],
)
