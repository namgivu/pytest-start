# prerequisite
install pyenv to install python 3.6 and then pipenv ref. bit.ly/nnpipenv

# run code
```bash
cd :THIS
    # install dependencies
    pipenv sync

    # app config
    cp .env-sample .env
    please_do='edit .env file to fill in your setting' 

    # run test 
    pipenv run  pytest                                            # run all
    pipenv run  pytest -x                                         # stop after 1st failed test
    pipenv run  pytest -s tests/path/to/your_test.py              # run tests in a file
    pipenv run  pytest -k tests/path/to/your_test.py:test_method  # run a specific test method

    #TODO How to get PyCharm test run working with pytest-dotenv? ref. https://github.com/quiqua/pytest-dotenv/issues/10
```

# run test parallel
ref. :THIS/doc/run-test-parallel.md
