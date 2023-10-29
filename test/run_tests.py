"""runs a series of tests using the pytest framework.

Collecting and reporting code coverage data,
generating a coverage report in both text and HTML formats.
"""

import sys
import os
import coverage
import pytest


def run_tests():
    """Run pytest tests and generates code coverage reports.

    Returns:
        int: The exit code from the pytest tests.
    """
    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))

    # Initialize a coverage object with the
    # data_file set to .coverage in the script's directory
    cov = coverage.Coverage(data_file=os.path.join(script_dir, '.coverage'))

    # Start collecting coverage data
    cov.start()

    # Run the pytest tests
    result = pytest.main(sys.argv[1:])

    # Stop collecting coverage data
    cov.stop()

    # Save the coverage data to .coverage file
    cov.save()

    # Print a simple coverage report to the console
    print("\n\nCoverage Report:")
    cov.report()

    # Generate a more comprehensive HTML coverage report
    cov.html_report(directory=os.path.join(script_dir, 'htmlcov'))

    # Open the HTML report in the web browser
    cov.report()

    return result


if __name__ == "__main__":
    sys.exit(run_tests())
