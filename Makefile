runserver:
	python3 manage.py runserver vps123446.vps.ovh.ca:8080

clean:
	find . -name "__pycache__" -exec rm -r "{}" \;
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete

distclean: clean
	rm -rf db.sqlite3

deps:
	pip3 install Django
	pip3 install django-taggit
	pip3 install django-haystack
	pip3 install pymongo
	pip3 install whoosh
	pip3 install oauth2
	pip3 install pytz
	pip3 install django-lint
	pip3 install flake8

shell:
	python3 manage.py shell

test:
	python3 manage.py test --keepdb -v2

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate
