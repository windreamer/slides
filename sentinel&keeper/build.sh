#!/bin/bash

CWD=$(dirname $(readlink -f $0))
COMMON=$(dirname $CWD)/common
DEST=$(basename $CWD)
PYTHONPATH=$PYTHONPATH:$COMMON/extensions \
    landslide -x graphviz,asciimathml -t $COMMON/themes/shower -i -d $DEST.html $CWD
