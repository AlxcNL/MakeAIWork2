#!/usr/bin/env bash

# # Activate virtual environment env
# source env/bin/activate

function install_without_conda {
  # Upgrade pip
  python3 -m pip install --upgrade pip

  # Install setuptools
  python3 -m pip install setuptools
  python3 -m pip install virtualenv
  python3 -m venv env 
  env/Scripts/activate
  python -m pip install --no-cache-dir -r install/pip/no_conda.txt

}  

function install_with_conda {
  if (! command -v "conda" &> /dev/null ) then
    echo "Try to install basic Python requirements without Miniconda\n"
    install_without_conda
  else
    conda install --yes -c conda-forge \
      beautifulsoup4 \
      jupyter_core \
      jupyterlab \
      keras \
      Keras-Preprocessing \
      matplotlib-base \
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

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     
      machine="Linux"
      install_with_conda
    ;;
    Darwin*)
      machine="Mac"
      install_with_conda
    ;;
    MINGW*)     
      machine="Git Bash"
      install_without_conda
    ;;
    *)          
      machine="UNKNOWN:${os}"
esac

# Install all required libraries t
function install_with_pip {
  # Upgrade pip
  python -m pip install --upgrade pip

  # Install setuptools
  python -m pip install setuptools
  python -m pip install --no-cache-dir -r install/pip/requirements.txt

}

install_with_pip
