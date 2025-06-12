#!/usr/bin/env bash
# Script to run The Matrix Resurrections Terminal Movie

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

# Main Python script for the movie
MOVIE_SCRIPT="matrix_resurrections_terminal_movie.py"

# Check if the movie script exists in the same directory as run.sh
if [ ! -f "${SCRIPT_DIR}/${MOVIE_SCRIPT}" ]; then
    echo "Error: Movie script not found at ${SCRIPT_DIR}/${MOVIE_SCRIPT}"
    echo "Please ensure '${MOVIE_SCRIPT}' is in the same directory as 'run.sh'."
    exit 1
fi

echo "Launching The Matrix Resurrections: Terminal Movie..."
echo "Ensure your terminal is maximized for the best experience."
echo "Press Ctrl+C to exit at any time."
sleep 2

# Change to the script's directory to ensure relative paths in Python script work
# and that the Python script can be called by its name.
cd "${SCRIPT_DIR}" || exit # Exit if cd fails

# Try python3 first
if command -v python3 &>/dev/null; then
    echo "Attempting to run with python3..."
    if python3 "${MOVIE_SCRIPT}"; then
        echo "Movie finished (using python3)."
        exit 0 # Success
    else
        echo "Execution with python3 failed or was interrupted."
        # We fall through to try 'python' in case python3 had an issue but python might work
        # (e.g. script error specific to python3 version, or user interrupted)
    fi
else
    echo "python3 command not found."
fi

# If python3 command not found or its execution failed/was interrupted, try python
if command -v python &>/dev/null; then
    echo "Attempting with 'python'..."
    if python "${MOVIE_SCRIPT}"; then
        echo "Movie finished (using python)."
        exit 0 # Success
    else
        echo "Execution with 'python' also failed or was interrupted."
    fi
else
    echo "python command not found."
fi

# If both python3 and python attempts did not lead to a successful exit(0)
echo "Error: Could not successfully execute the movie script with python3 or python."
echo "Please ensure Python is installed, in your PATH, and the Python script itself has no errors."
exit 1
```
