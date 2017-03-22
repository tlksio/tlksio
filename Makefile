clean:
	find . -name "*.pyc" -delete
	find . -name ".DS_Store" -delete

deps:
	pip install django-taggit

migrate:
    ./manage.py makemigrations
	./manage.py migrate
