#!/bin/bash

# Define the path to the virtual environment
VENV_PATH='./venv/bin/activate'

# Activate the virtual environment
source "$VENV_PATH"

# Execute the test suite
python -m pytest test_all.py

# Check the exit code of pytest
PYTEST_EXIT_CODE=$?

if [ $PYTEST_EXIT_CODE -eq 0 ]; then
  echo "All tests passed successfully! :)"
  exit 0
else
  echo "Some tests failed. :("
  exit 1
fi