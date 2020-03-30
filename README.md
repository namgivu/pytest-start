# prerequisite
install pyenv to install python 3.6 and then pipenv ref. bit.ly/nnpipenv

# run code
```bash
cd :THIS
    # install dependencies
    pipenv sync -d
    #           #also install dev-package

    # app config
    cp .env-sample .env
    please_do='edit .env file to fill in your setting' 

    # run test 
    pipenv run  pytest tests/path/to/your_test.py -k 'test_method'  # run a specific test method
    pipenv run  pytest tests/path/to/your_test.py                   # run tests in a file
    pipenv run  pytest -x                                           # stop after 1st failed test
    pipenv run  pytest                                              # run all
```


# can also get PyCharm test run working with pytest-dotenv 
ref1. https://github.com/quiqua/pytest-dotenv/issues/10
    lead to ref2. https://github.com/namgivu/pytest-start/pull/1
    
01 must use **dev-package version** for pytest and pytest-dotenv
02 must use -d pip install i.e. `pipenv sync -d`


# run test parallel
ref. :THIS/doc/run-test-parallel.md
