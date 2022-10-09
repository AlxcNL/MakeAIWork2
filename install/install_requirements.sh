#!/usr/bin/env bash

# # Activate virtual environment env
# source env/bin/activate

function createVirtualEnv {
  echo "Create virtualenv"
  python -m pip install virtualenv
  python -m venv env 
  echo "Activate virtualenv"
  source env/Scripts/activate

  echo "Add virtual environment actionvation to bashrc"
  activationPath=$(cygpath ${PWD}/env/Scripts/activate)
  echo "source ${activationPath}" > ~/.bashrc

}

function installWithoutConda {
  echo "Install without conda"
  createVirtualEnv

  # Upgrade pip
  python -m pip install --upgrade pip

  # Install setuptools
  python -m pip install setuptools
  python -m pip install --no-cache-dir -r install/pip/no_conda.txt

}  

function installWithConda {
  echo "Install with conda"
  
  if (! command -v "conda" &> /dev/null ) then
    echo "Try to install basic Python requirements without Miniconda\n"
    installWithoutConda
  else
    conda install --yes -c conda-forge \
      beautifulsoup4 \
      jupyter_core \
      jupyterlab \
      keras \
      Keras-Preprocessing \
      matplotlib-base \
      nodejs \
      Pillow \
      pandas \
      py-cpuinfo \
      pyopengl \
      pytables \
      scikit-image \
      scikit-learn \
      scipy \
      seaborn \
      selenium \
      statsmodels \
      sympy \
      tensorflow
  fi

}

# Install all required libraries t
function installWithPip {
  echo "Install with pip"

  # Upgrade pip
  python -m pip install --upgrade pip

  # Install setuptools
  python -m pip install setuptools
  python -m pip install --no-cache-dir -r install/pip/requirements.txt

}

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     
      installWithConda \
        && installWithPip
    ;;
    # MacOS
    Darwin*)
      installWithConda \
        && installWithPip
    ;;
    # Git Bash
    MINGW*)     
      createVirtualEnv && installWithoutConda && installWithPip
    ;;
    *)          
      installWithoutConda \
        && installWithPip
esac