runserver:
	venv/bin/python manage.py runserver 0.0.0.0:8000

pep8:
	pep8 --exclude=*migrations*,*settings_local.py* --max-line-length=119 --show-source  mywed/

pyflakes:
	pylama --skip=*migrations* -l pyflakes mywed/

lint:
	make pep8
	make pyflakes

test:
	venv/bin/python manage.py test mywed -v 2

ci_test:
	coverage run --source='.' manage.py test mywed -v 2
	coverage report
	make lint

syncdb:
	venv/bin/python manage.py syncdb

pip_install:
	pip install --no-index -f wheels/ -r requirements.txt
