#!/bin/bash

# Script to run the entire application

cleanup() {
    echo "Caught Ctrl-C - cleaning up..."

    # Move back to parent directory on kill
    cd ..
}

trap cleanup INT
trap cleanup EXIT

echo "Running webapp..."
cd ./qgames || exit 1

# Run Python in the background
python -m server.app
# PY_PID=$!

# Wait on the Python process
# wait $PY_PID

echo "Finished."
