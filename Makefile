VENV_PATH := $(HOME)/venv/bin

runserver:
	$(VENV_PATH)/python manage.py runserver 0.0.0.0:8000

pep8:
	$(VENV_PATH)/pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  mywed/

pyflakes:
	$(VENV_PATH)/pylama --skip=*migrations* -l pyflakes mywed/

lint: pep8 pyflakes

test:
	$(VENV_PATH)/python manage.py test mywed -v 2

ci_test:
	coverage run --source='.' manage.py test mywed -v 2
	coverage report
	make lint

syncdb:
	$(VENV_PATH)/python manage.py syncdb

pip_install:
	$(VENV_PATH)/pip install --no-index -f wheels/ -r requirements.txt
