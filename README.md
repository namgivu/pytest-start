# install pyenv for ubuntu 16
```bash
sudo apt update -y
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev \
  libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
  xz-utils tk-dev libffi-dev

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

echo 'export PYENV_ROOT="$HOME/.pyenv"'    >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc

# restart shell & aftermath check
exec "$SHELL"
pyenv --version
```

# install python 3.6.7
```bash
pyenv install 3.6.7
pyenv global 3.6.7
python --version # should be 3.6.7
```

# install pipenv
```bash
# install pipenv
curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python
echo "
# pipenv setup"                                   >> ~/.bashrc
echo 'export PATH="~/.local:$PATH"'               >> ~/.bashrc
echo 'export PIPENV_VENV_IN_PROJECT=1'            >> ~/.bashrc # project's venv location will be in the project folder as .venv ref. https://pipenv.readthedocs.io/en/latest/advanced/#pipenv.environments.PIPENV_VENV_IN_PROJECT
echo 'export PIPENV_DEFAULT_PYTHON_VERSION=3.6.7' >> ~/.bashrc # project's venv location will be in the project folder as .venv ref. https://pipenv.readthedocs.io/en/latest/advanced/#pipenv.environments.PIPENV_VENV_IN_PROJECT
echo 'eval "$(pipenv --completion)"'              >> ~/.bashrc # shell auto-completion ref. https://pipenv.readthedocs.io/en/latest/advanced/#shell-completion

#restart shell & aftermath check
exec "$SHELL"
pipenv --version
```

# install requirements.txt
```bash
cd $THIS_PROJECT
pipenv install
pipenv shell # activate venv

prj=`pwd` # put here /path/to/your/project/folder
export PYTHONPATH="$prj:$PYTHONPATH"
pytest -x # should run testcases in $THIS_PROJECT/tests
```

# more docs
Please view more at [doc/](doc)
