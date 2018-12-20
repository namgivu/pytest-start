ref. https://stackoverflow.com/questions/45733763/pytest-run-tests-parallel

register project folder with PYTHONPATH
```bash
prj=`pwd` # put here /path/to/your/project/folder
export PYTHONPATH="$prj:$PYTHONPATH"
```

run parallel with 02 cpu
TODO how to detect optimized number of cpu?
```bash
       #stop if error  #cpu number  #show elapsed  #verbose elapsed  #turn off warning         
pytest -x              -n 2         --durations=0  -vv               --disable-pytest-warning  
```

normally test run with no parallel
```bash
pytest -x
```

run log
```bash
pytest -x -n 3 --durations=0  --disable-pytest-warning  
```
