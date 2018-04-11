#!/bin/bash
echo "Installing packages"
pip install -r requirements.txt --no-index --find-links file:///tmp/packages
echo "Finished installing packages"