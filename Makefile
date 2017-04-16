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

uwsgi:
	/usr/local/bin/uwsgi --chdir=/home/raul/tlksio \
		--module=wsgi:application \
		--master --pidfile=/tmp/project-master.pid \
		--socket :8080 \
		--processes=5 \
		--max-requests=5000 \
		--vacuum \
		--home=/home/raul/tlksio/env
		# --http 127.0.0.1:8080
		# daemonize=/home/raul/tlksio/yourproject.log


