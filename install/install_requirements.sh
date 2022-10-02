#!/usr/bin/env bash

# # Activate virtual environment env
# source env/bin/activate

# Detect OS
unameOut="$(uname -s)"
os="${unameOut:0:7}"
case "${os}" in
    Linux*)     
      machine="Linux"
    ;;
    Darwin*)
      machine="Mac"
      ;;
    CYGWIN*)    machine="Cygwin";;
    MINGW*)     machine="Git Bash";;
    *)          machine="UNKNOWN:${os}"
esac

function install_with_conda {
  if (! command -v "conda" &> /dev/null ) then
    echo "Install Miniconda first\n" && exit 0
  fi

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
}

# Install all required libraries t
function install_with_pip {
  # Upgrade pip
  python3 -m pip install --upgrade pip

  # Install setuptools
  python3 -m pip install setuptools
  python3 -m pip install --no-cache-dir -r install/pip/requirements.txt

}

# install_with_conda
install_with_pip
