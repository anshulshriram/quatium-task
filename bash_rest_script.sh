#!/bin/bash

# Activate the virtual environment
source ./qenv/Scripts/activate  # Modify the path to your virtual environment as needed

# Run the test suite using pytest
pytest test_RadioDashApp.py

# Check if tests passed or failed
if [ $? -eq 0 ]; then
    echo "All tests for test_RadioDashApp.py passed."
    exit 0
else
    echo "Some tests for test_RadioDashApp.py failed."
    exit 1
fi


# Run the test suite using pytest
pytest test_.py

# Check if tests passed or failed
if [ $? -eq 0 ]; then
    echo "All tests for test_.py passed."
    exit 0
else
    echo "Some tests for test_.py failed."
    exit 1
fi

