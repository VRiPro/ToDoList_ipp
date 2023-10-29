import coverage
import pytest
import sys

def run_tests():
    # Initialize a coverage object
    cov = coverage.Coverage()

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
    cov.html_report(directory='htmlcov')

    # Open the HTML report in the web browser
    cov.report()

    return result

if __name__ == "__main__":
    sys.exit(run_tests())
