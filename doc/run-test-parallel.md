use pytest-xdist
ref. https://stackoverflow.com/questions/45733763/pytest-run-tests-parallel

```bash
pytest -n 2        --durations=0 -vv  --disable-pytest-warning
#      #of worker  #show elapsed      #turn off warning
```
