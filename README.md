# prerequisite
install pyenv to install python 3.6 and then pipenv ref. bit.ly/nnpipenv

# run code

## run from command line
```bash
cd :THIS
    # install dependencies
    pipenv sync

    # app config
    cp .env-sample .env
    please_do='edit .env file to fill in your setting' 

    # run test 
    pipenv run  pytest tests/test_dotenv.py
    pipenv run  pytest -x 
```

## run with PyCharm 
ref. https://github.com/quiqua/pytest-dotenv/issues/10


# run test parallel
ref. :THIS/doc/run-test-parallel.md
