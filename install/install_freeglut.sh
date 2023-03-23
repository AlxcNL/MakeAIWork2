#!/usr/bin/env sh

echo "Generate directory accessories"
python -m simpylc -a

echo "Copy freeglut dll"
cp -f accessories/freeglut64.vc14.dll /c/Windows/System32/ && rm -rf accessories

echo "Install packages"
pip install --upgrade pip \
    PyOpenGL==3.1.6 \
    PyOpenGL-accelerate==3.1.6 \
    SimPyLC==3.10.0