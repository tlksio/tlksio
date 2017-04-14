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
	pip install -r requirements.txt

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
