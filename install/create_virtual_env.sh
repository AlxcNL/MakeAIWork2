#!/usr/bin/env bash

if (! command -v "conda" &> /dev/null ) then
    python -m pip install virtualenv
    python -m venv env 

    echo "Add virtual environment actionvation to bashrc"
    activationPath=$(cygpath ${PWD}/env/Scripts/activate)
    echo "${activationPath}"
    echo "source ${activationPath}" > ~/.bashrc
else
    conda init zsh
fi

zsh || bash


