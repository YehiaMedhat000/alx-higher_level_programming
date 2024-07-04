#!/usr/bin/env bash
# Bash script that takes in a URL, sends a GET request to the URL
# and displays the body of the response

RESPONSE=$(curl -s -o /dev/null -w "%{http_code}" "$1") 

if [ "$RESPONSE" == 200 ]; then
    curl -sL "$1"
fi
