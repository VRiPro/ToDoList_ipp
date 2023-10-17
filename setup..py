from setuptools import setup, find_packages

setup(
    name="ToDoList",
    version="0.1",
    description="Création d'une bibliothèque Python complète pour la création et la \
        gestion de tâches personnelles en utilisant les notions vues dans le cours de Kit pour le Big Data",
    author=["Ahmed", "Nour", "Victor", "Mathieu"],
    packages=find_packages(),
    install_requires=[
        "datetime"
    ],
)
