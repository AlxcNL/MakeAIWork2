#!/usr/bin/env bash

export PYTHONPATH=simulations/car
export LIBGL_ALLOW_SOFTWARE=1

python simulations/car/control_client/hardcoded_client.py
