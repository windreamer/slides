#!/bin/bash

CWD=$(pwd)
PYTHONPATH=$PYTHONPATH:$CWD/extensions \
    landslide -x graphviz,asciimathml -t $CWD/themes -i -d $CWD/keepers.html $CWD/keepers.md
