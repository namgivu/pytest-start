# use pytest-xdist
ref. https://stackoverflow.com/questions/45733763/pytest-run-tests-parallel

```bash
pipenv run pytest -p no:warnings   --tb=short        --durations=6666           -n 2           
#                 #no warning      #traceback short  #show test execution time  #worker count
```

# how to tell if there is a failed test
sample log when test failed
> ======= 1 failed, 3 passed in 5.41s ======

```bash
grep -c  -E '=+.+failed'  /tmp/t
```
