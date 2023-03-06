#!/bin/bash

# Check the number of arguments
if [ "$#" -gt 3 ]; then
    echo "Error: Too many arguments"
    exit 
fi

# Print the arguments
echo "Argument 1: ${1:-<not provided>}"
echo "Argument 2: ${2:-<not provided>}"
echo "Argument 3: ${3:-<not provided>}"
