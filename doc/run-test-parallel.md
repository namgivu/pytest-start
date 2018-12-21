ref. https://stackoverflow.com/questions/45733763/pytest-run-tests-parallel

register project folder with PYTHONPATH
```bash
prj=`pwd` # put here /path/to/your/project/folder
export PYTHONPATH="$prj:$PYTHONPATH"
```

run parallel with 02 cpu
```bash
#run with pytest-xdist
       #stop if error  #cpu number  #show elapsed  #verbose elapsed  #turn off warning         
pytest -x              -n 2         --durations=0  -vv               --disable-pytest-warning  
pytest -x              -n 2         --durations=0                    --disable-pytest-warning  

#run with pytest-parallel
       #stop if error  #worker number  #test per worker         #show elapsed  #verbose elapsed  #turn off warning         
pytest -x              --workers 2     --tests-per-worker 2     #--durations=0  -vv               --disable-pytest-warning  
```

normally test run with no parallel
```bash
pytest -x
```

misc commands log
```bash
pytest -x -n 3 --durations=0  --disable-pytest-warning  
```
