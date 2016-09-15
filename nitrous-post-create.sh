#!/bin/bash
rm -rf ~/code/example

sudo apt-get update
sudo apt-get install -y --no-install-recommends imagemagick
sudo apt-get clean

pip install pattern