#!/usr/bin/env bash

function createVirtualEnv {    
    if [[ -d "env" ]]
    then
        echo "Virtual environment env already exists"
    else
        echo "Create virtual environment env"
        python -m pip install virtualenv || python2 -m pip install virtualenv
        python -m venv env || python3 -m venv env 
    fi	

    echo "Activate virtual environment env"
    source env/Scripts/activate

    # Make sure ~/.bashrc exists
    touch ~/.bashrc 
    (cat ~/.bashrc | grep env) && exit 1
    echo "Add virtual environment actionvation to bashrc"
    activationPath=$(cygpath ${PWD}/env/Scripts/activate)
    echo "${activationPath}"
    echo "source ${activationPath}" >> ~/.bashrc    

    echo "Create alias pptyhon for ptpython which starts with winpty"
    alias ppython="winpty ptpython"

}

function createCondaEnv {
    if (! command -v "conda" &> /dev/null ) then
        createVirtualEnv
    else
        conda init zsh && conda activate miw    
    fi

}

echo "Detect OS"
unameOut="$(uname -s)"
os="${unameOut:0:7}"

case "${os}" in
    Linux*)     
        createCondaEnv
    ;;
    # MacOS
    Darwin*)
        createCondaEnv
    ;;
    # Git Bash
    MINGW*)     
        createVirtualEnv
    ;;
    *)          
        createVirtualEnv
    ;;

esac
