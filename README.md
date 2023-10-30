# ToDoList

A comprehensive Python library for creating and managing personal tasks using concepts covered in the "Kit Big Data" course at télécom paris (2023-2024).

**Contributers:** 
* Ahmed Belaaj (MS IA)
* Nour Ben Rejeb (MS IA)
* Victor Rivière (MS BGD)
* Mathieu Sauveur (MS BGD)


## Description

The main purpose of this project is to provide hands-on experience and get familiar with concepts and best practices required for coding a python project in a "production" context. 
The objective of this project is to put into practice the concepts and skills  learned in the course to create a comprehensive Python library for personal tasks (To-Do List). This project focuses on various aspects:

- **Project Structure:** A well-organized project structure.
- **Python Environment Management:** Using Poetry for Python environment management.
- **Object-Oriented Programming:** Implementing object-oriented programming principles.
- **Type Hinting:** Utilizing type hinting for clear and robust code.
- **Logging:** Effective log management for debugging and monitoring.
- **PEP 8 Compliance:** Ensuring adherence to Python's PEP 8 coding style guidelines.
- **Exception Handling:** Properly managing exceptions for robustness.
- **Security:** Implementing security best practices.
- **Unit Testing:** Comprehensive unit tests using pytest.
- **Test Coverage:** Measuring and improving test coverage.
- **Documentation:** Creating documentation using Sphinx.
- **CI/CD Pipeline:** Setting up a CI/CD pipeline with GitHub Actions.


## Requirements
To run this repo locally, It's necessary to have python installed on your computer, preferably with a version supporting regular security updates (for example python 3.9 that we've used to implement this project).
It's also advisable to `poetry` to make environment and packages versionning management more efficient: 
```shell
pip install poetry
```
## Getting started

1. Clone the repository:

```shell
git clone https://github.com/ahmedbellaaj10/ToDoList.git
```

2. Navigate to the Cloned Directory:

Use the cd command to change your current directory to the cloned repository's directory:

```bash
cd ToDoList
```

3. Install the project dependencies:

```shell
poetry install
```
This will create a virtual environment and install the required packages following the instructions in `pyproject.toml` file.

*NB: *If you're not willing to use *poetry*, you can just install the requirements using this command:
```shell
pip install -r requirements.txt
``` 
However, It is always advisable to use a virtual environment to provide isolation and control over project-specific dependencies, ensuring a clean and consistent development environment while reducing the risk of conflicts and security issues.

4. Activate the virtual environment:

```shell
poetry shell
``` 
5. To simulate some scenarios proposed by our module, you can run `example.py` file:

```shell
poetry python run example.py
``` 
You can play around with this file and use the different functions provided in the documentation to explore the functionnalities provided by our library.

## Features:
### Project structure:
```
ToDoList
¦   .gitignore                   # Git ignore file
¦   example.py                   # Example Python script (To manually test the 
¦                                                         functions)
¦   logger.py                    # Contains logger configurations
¦   pyproject.toml               # Python project configuration file
¦   README.md                    # Project description (you are here)
¦   requirements.txt             # List of project dependencies
¦   setup.py                     # Python package setup script
¦   
+---.github                      # GitHub-related configuration
¦   +---workflows                # GitHub Actions workflows
¦           pipeline.yaml        # GitHub Actions pipeline configuration
¦           
+---docs                         # Project documentation 
¦                                (contains many sub-folders / files to configure
¦                                and generate the documentation)
¦
¦                       
+---logs                         # Log files
¦       info.txt                 # Just a palceholder :) 
¦       
+---test                         # Unit tests
¦       run_tests.py             # Script to run tests and lunch coverage report
¦       test_task.py             # Unit tests for the 'task' module
¦       __init__.py
¦       
+---todoproject                  # Main project package
        task.py                  # Task-related module
        __init__.py        
```

### Documentation
here we say that you can refer to the documentation to know more about the code (insert instructions about opening the already existing doc as well as instruction on how to generate a new doc)

### Concepts Applied:
#### OOP Concepts: inheritance, encapsulation : 
In our project, we've harnessed Object-Oriented Programming (OOP) principles to extend the functionality of our task management system:

* **Inheritance:** We've introduced a `CriticalTask` class, inheriting attributes and methods from the base `Task` class. This enables the creation of specialized tasks with additional features.

* **Encapsulation:** For enhanced data control, the `CriticalTask` class includes a `deadline` attribute, marked as protected. Access and modification are managed through designated methods, ensuring data integrity. Additionally, the `Priority` attribute is always set to `critical`, providing a default value for crucial tasks.

#### PEP8 Compliance, Type Hinting, and docstrings :
* **PEP8 Compliance:** Our codebase strictly follows the Python Enhancement Proposal 8 (PEP8) style guide. This ensures consistency in code formatting, naming conventions, and structure, making it easier to collaborate and maintain. We use `autopep8` and `flake8` to ensure this.

* **Type Hinting:** To improve code clarity, we've used type hints extensively throughout the project. Type hints make it clear what types of data are expected and returned by functions and methods, aiding developers in understanding and using our code effectively.

* **Docstrings:** For comprehensive documentation, we've employed docstrings to describe classes, methods, and functions. These docstrings provide detailed explanations of their purpose, parameters, and return values. Our approach ensures that developers have access to clear, on-the-fly documentation, facilitating the use of our library, helps in the generation of the documentation with `sphinx`. We use `Pydocstyle` to keep track of any unconsistencies in the docstrings.

#### Security: 
We prioritize the security of our library. Key security points:

* **Vulnerability Assessment:** We regularly assess our code for evident security vulnerabilities.

* **Data Handling:** We do not use sensitive data during development to prevent data exposure.

* **Secure Dependencies:** Our project relies on secure and well-maintained dependencies.

* **Up-to-Date Python:** We use a Python version with regular security updates to enhance security.

#### Logging: 
We use the `logger.py` file to configure our loggers. In a nutshell, we have two loggers, the first is responsible for logging debug messages and the other is for the error messages. Each logger writes messages in a seperate file under the `/logs` folder.
#### Exceptions handling:
In our project, we've introduced a custom exception class, `ToDoErrors`, which inherits from the built-in `Exception` class. This custom exception is designed to capture and handle exceptional situations that could impact the proper functioning of the code. By using `ToDoErrors`, we provide clear and meaningful error messages to assist developers in identifying and addressing issues.
#### Testing
Our project includes a robust testing framework to ensure the reliability and functionality of our code. Testing is a critical aspect of our development process, and we've implemented two key components:

##### <u>Unit testing</u>
We've incorporated unit tests using `pytest`, which allow us to systematically test individual units or components of our code. Unit tests help identify and rectify issues at an early stage, enhancing the stability and accuracy of our project.

##### <u>Coverage report</u>
In addition to unit testing, we measure the code coverage of our tests using `coverage.py`. This tool provides insights into which parts of our code are exercised by our tests. Our goal is to maintain a test coverage of at least 90%, ensuring that most of our code is thoroughly tested and reliable.


#### CI/CD pipeline
Our project includes a CI/CD pipeline that automates various checks and tests, ensuring code quality and reliability. Here's an overview of the pipeline's key steps:

* **Trigger:** The pipeline is triggered on each push to the "main" branch.

* **Environment:** It runs on an Ubuntu-based environment using GitHub Actions.

* **Steps:**

    * **Checkout repository:** The pipeline checks out the code from the repository.
    * **Set up Python:** It sets up the Python environment, specifically Python 3.9.
    * **Install Poetry:** Poetry, a Python dependency management tool, is installed.
    * **Install project dependencies:** The project's dependencies are installed using Poetry.
    * **Check dependencies with safety:** We use the 'Safety' tool to scan project dependencies for known security vulnerabilities, enhancing the overall security of our software.
    * **Check PEP8 compliance and auto-format:** PEP8 compliance is verified, and code is auto-formatted.
    * **Check docstrings:** The pipeline checks the documentation strings in the code.
    * **Run unit tests:** It executes unit tests using pytest.
    * **Calculate code coverage:** Code coverage is calculated and must meet a minimum threshold of 90%.
    * **Upload coverage report:** The coverage report is uploaded as an artifact when coverage meets the threshold. *PS*: The artifact is in the form of a binary file `.coverage`. To be able to read it, you need to have `coverage` installed locally, then in the same level of the file run this command in the terminal:
    ```shell
    coverage report -i
    ``` 
    This will print the coverage report in the console.

This CI/CD pipeline helps maintain code quality, ensures PEP8 compliance, and verifies test coverage, enhancing the reliability of our project.

### Upcoming:
add a web app using streamlit to imporve the user experience
