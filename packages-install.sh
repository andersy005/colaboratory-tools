#!/bin/bash
echo "Installing packages"
pip install -r requirements.txt --quiet --no-index --find-links file:///tmp/packages
echo "Finished installing packages"