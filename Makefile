runserver:
	python manage.py runserver vps123446.vps.ovh.ca:8080

clean:
	find . -name "__pycache__" -exec rm -rf "{}" \;
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete
	rm -rf .coverage

distclean: clean
	rm -rf db.sqlite3

deps:
	pip install Django
	pip install django-taggit
	pip install django-haystack
	pip install pymongo
	pip install whoosh
	pip install oauth2
	pip install pytz
	pip install django-lint
	pip install flake8
	pip install coverage

shell:
	python manage.py shell

test:
	python manage.py test --keepdb -v2

cover:
	coverage run --source=tlksio,talks manage.py test
	coverage report

migrate:
	python manage.py makemigrations
	python manage.py migrate
