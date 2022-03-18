#!/bin/bash
# Get the byte size of the HTTP response header for a given URL.
curl -sI GET "$1" | grep -i "Content-Length" | cut -d " " -f2
