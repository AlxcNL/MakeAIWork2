#!/usr/bin/env bash

version="$1"

if [ -z "$version" ]; then
    version="3.10.9"
    exit 1;
fi

package="Python-${version}"
tarfile="${package}.tar.xz"

function installPython { 

    printf "Download %s" ${tarfile}
    # https://www.python.org/ftp/python/3.10.5/
    wget https://www.python.org/ftp/python/${version}/${tarfile}

    printf "Extract %s\n" ${package}
    tar -xf ${tarfile}

    printf "Install %s\n" ${tarfile}
    (cd ${package}; ./configure --enable-optimizations && make && make install)

    printf "Set python %s as default" ${version}
    alias python=$(realpath ./python)

    echo "Clean installation files"
    rm_cmd="rm ${tarfile}"
    echo ${rm_cmd}
    eval ${rm_cmd}

}

(cd /usr/local; installPython)
python --version
