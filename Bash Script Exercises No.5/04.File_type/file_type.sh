#!/bin/bash

# Prompt the user for a file or directory name
read -p "Enter a file or directory name: " name

# Check if the file or directory exists
if [ -e "$name" ]; then
    # Check if the file or directory is a regular file
    if [ -f "$name" ]; then
        echo "$name is a regular file"
    # Check if the file or directory is a directory
    elif [ -d "$name" ]; then
        echo "$name is a directory"
    else
        echo "$name is not a regular file or directory"
    fi
    
    # Perform an ls command with the long listing option
    ls -l "$name"
else
    echo "$name does not exist"
fi

