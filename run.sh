#!/bin/bash
SH=$(cd `dirname $BASH_SOURCE` && pwd)
cd $SH
    PYTHONPATH=$SH pipenv run pytest
