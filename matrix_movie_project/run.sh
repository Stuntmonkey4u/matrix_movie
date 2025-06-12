#!/bin/bash
# Script to run The Matrix Resurrections Terminal Movie

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Python interpreter to use (python3 is generally preferred)
PYTHON_CMD="python3"

# Check if python3 is available, fallback to python if not
if ! command -v python3 &> /dev/null
then
    echo "python3 could not be found, trying with python..."
    PYTHON_CMD="python"
    if ! command -v python &> /dev/null
    then
        echo "Error: Neither python3 nor python command found. Please ensure Python is installed and in your PATH."
        exit 1
    fi
fi

# Main Python script for the movie
MOVIE_SCRIPT="matrix_resurrections_terminal_movie.py"

# Full path to the movie script
FULL_SCRIPT_PATH="${SCRIPT_DIR}/${MOVIE_SCRIPT}"

# Check if the movie script exists
if [ ! -f "${FULL_SCRIPT_PATH}" ]; then
    echo "Error: Movie script not found at ${FULL_SCRIPT_PATH}"
    echo "Please ensure you are running this from the 'matrix_movie_project' directory or that the script structure is correct."
    exit 1
fi

echo "Launching The Matrix Resurrections: Terminal Movie..."
echo "Ensure your terminal is maximized for the best experience."
echo "Press Ctrl+C to exit at any time."
sleep 2 # Brief pause before launching

# Execute the main movie script using the determined Python command
cd "${SCRIPT_DIR}" && "${PYTHON_CMD}" "${MOVIE_SCRIPT}"

echo "Movie finished. Exiting."
