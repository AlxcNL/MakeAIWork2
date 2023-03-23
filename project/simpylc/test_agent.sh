#!/usr/bin/env bash

export PYTHONPATH=simulations/car
export LIBGL_ALLOW_SOFTWARE=1

(sleep 3; ./start_agent.sh)&
./start_world.sh