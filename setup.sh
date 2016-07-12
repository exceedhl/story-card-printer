#!/bin/bash

set -e

if [ ! -d venv ]; then
    virtualenv -p $(which python3.4) venv
fi

source ./venv/bin/activate

pip_home=$HOME/.pip
pip install --upgrade pip
pip install --cache-dir $pip_home/download-cache wheel
pip wheel --cache-dir $pip_home/download-cache --use-wheel \
    -w $pip_home/wheelhouse -f file://$pip_home/wheelhouse -r requirements.txt
pip install --no-index -f file://$pip_home/wheelhouse -r requirements.txt
