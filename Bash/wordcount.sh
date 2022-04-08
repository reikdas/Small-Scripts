#!/bin/bash

# Count the number of occurrences of all the words in all files in the specified directory
find $1 -type f -exec cat {} \; | tr '[:space:]' '[\n*]' | grep -v "^\s*$" | sort | uniq -c | awk '{print $2,$1}' | sort
