#!/usr/bin/env sh

echo "Generate directory accessories"
python3 -m simpylc -a

echo "Install packages"
pip install --upgrade pip \
    PyOpenGL==3.1.6 \
    PyOpenGL-accelerate==3.1.6 \
    SimPyLC==3.10.0
